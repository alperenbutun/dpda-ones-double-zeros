#!/usr/bin/env python3
"""
Reproducibility suite for:
  Completion Frontiers and Quotient Geometry in Deterministic Pushdown
  Automata for Rational Binary Counting

Author: Alp Eren Bütün
Repository: https://github.com/alperenbutun/dpda-ones-double-zeros

Quick smoke test:
  python paper_validation_suite.py

Exact paper-level validation (Section 9):
  python paper_validation_suite.py --paper

The script uses only the Python standard library. Computational checks are
supporting evidence against implementation/transcription errors and are not
premises of the mathematical proofs.
"""
from math import gcd
from itertools import product
from collections import defaultdict
import json, sys

Z0="Z0"; X="X"

def rho(p,q,w): return q*w.count("1")-p*w.count("0")
def apos(p,s): return 0 if s==0 else s-p
def bneg(q,t): return 0 if t==0 else q-t

def encode(p,q,r,endmarker=False):
    zero="R0" if endmarker else "Z"
    if r==0: return zero,[Z0]
    if r>0:
        s=r%p
        a=apos(p,s)
        k=(r-a)//p
        assert k>=1
        return f"R{s}",["0"]*k+[Z0]
    t=(-r)%q
    b=bneg(q,t)
    k=(b-r)//q
    assert k>=1
    return f"R{t}",["1"]*k+[X]

def build_abstract(p,q,endmarker=False):
    m=max(p,q)
    states=[f"R{i}" for i in range(m)]
    if not endmarker: states=["Z"]+states
    zero="R0" if endmarker else "Z"

    # Requests before helper-state overlay.
    direct={}
    long=[]  # (source tuple, target, sym, net_pushes, sentinel_or_None)
    def put(key,target,repl):
        val=(target,tuple(repl))
        if key in direct and direct[key]!=val:
            raise AssertionError(("direct conflict",p,q,endmarker,key,direct[key],val))
        direct[key]=val

    def request_same(st,a,top,target,repl):
        # same-sign unary replacement, old top retained at bottom of replacement
        if len(repl)<=2:
            put((st,a,top),target,repl)
        else:
            sym=repl[0]
            assert top==sym and all(x==sym for x in repl)
            # first step makes one net push, remaining = len(repl)-2
            long.append(((st,a,top),target,sym,len(repl)-2,None))

    def request_boundary(st,a,top,target,stack):
        # top is a sentinel being replaced. stack is canonical target encoding.
        if len(stack)<=2:
            put((st,a,top),target,stack)
            return
        sym=stack[0]
        sentinel=stack[-1]
        assert sym in ("0","1")
        assert sentinel in (Z0,X)
        assert all(x==sym for x in stack[:-1])
        k=len(stack)-1  # unary count desired
        # First bounded step creates one unary symbol and target sentinel.
        first=[sym,sentinel]
        remaining=k-1
        if remaining==0:
            put((st,a,top),target,first)
        else:
            long.append(((st,a,top),target,sym,remaining,sentinel))

    # zero moves
    for a in "01":
        target,stack=encode(p,q,q if a=="1" else -p,endmarker)
        request_boundary(zero,a,Z0,target,stack)

    # positive roles
    for s in range(p):
        st=f"R{s}"
        put((st,"0","0"),st,[])
        sp=(s+q)%p
        c=(apos(p,s)+q-apos(p,sp))//p
        assert c>=0
        request_same(st,"1","0",f"R{sp}",["0"]*(c+1))

        boundary=apos(p,s)
        target,stack=encode(p,q,boundary,endmarker)
        if endmarker and boundary==0 and st=="R0":
            # after popping last 0: already R0,Z0
            pass
        else:
            request_boundary(st,"",Z0,target,stack)

    # negative roles
    for t in range(q):
        st=f"R{t}"
        put((st,"1","1"),st,[])
        tp=(t+p)%q
        c=(p-bneg(q,t)+bneg(q,tp))//q
        assert c>=0
        request_same(st,"0","1",f"R{tp}",["1"]*(c+1))

        boundary=bneg(q,t)
        target,stack=encode(p,q,boundary,endmarker)
        if endmarker and boundary==0 and st=="R0":
            # after popping last 1: X exposed; need remove/convert X to Z0
            request_boundary(st,"",X,target,stack)
        else:
            request_boundary(st,"",X,target,stack)

    if endmarker:
        put(("R0","$",Z0),"R0",[Z0])

    return states,direct,long

def compile_push2(p,q,endmarker=False):
    states,tr,long=build_abstract(p,q,endmarker)
    m=max(p,q)

    # Suffix roles identified by stable target, unary symbol, remaining net pushes.
    roles=set()
    for key,target,sym,remaining,sentinel in long:
        # sentinel no longer matters after first step: top is sym; the sentinel is buried.
        roles.add((target,sym,remaining))
    changed=True
    while changed:
        changed=False
        for target,sym,j in list(roles):
            if j>1 and (target,sym,j-1) not in roles:
                roles.add((target,sym,j-1)); changed=True

    pos_roles=sorted(r for r in roles if r[1]=="0")
    neg_roles=sorted(r for r in roles if r[1]=="1")

    # In paired-sign states:
    # if q>p, R_p...R_{q-1} have no positive/top0 semantic role;
    # if p>q, R_q...R_{p-1} have no negative/top1 semantic role.
    free0=[f"R{i}" for i in range(p,m)]
    free1=[f"R{i}" for i in range(q,m)]
    if len(pos_roles)>len(free0):
        raise AssertionError(("top0 capacity",p,q,endmarker,len(pos_roles),len(free0),pos_roles))
    if len(neg_roles)>len(free1):
        raise AssertionError(("top1 capacity",p,q,endmarker,len(neg_roles),len(free1),neg_roles))

    role_state={}
    role_state.update(dict(zip(pos_roles,free0)))
    role_state.update(dict(zip(neg_roles,free1)))

    out=dict(tr)
    def add(key,target,repl):
        val=(target,tuple(repl))
        if key in out and out[key]!=val:
            raise AssertionError(("compiled conflict",p,q,endmarker,key,out[key],val))
        out[key]=val

    # First steps of long pushes.
    for key,target,sym,remaining,sentinel in long:
        st,a,top=key
        role=(target,sym,remaining)
        h=role_state[role]
        if top in (Z0,X):
            sent = sentinel
            add(key,h,[sym,sent])
        else:
            assert top==sym and sentinel is None
            add(key,h,[sym,sym])

    # Suffix chains.
    for target,sym,j in roles:
        st=role_state[(target,sym,j)]
        nxt=target if j==1 else role_state[(target,sym,j-1)]
        add((st,"",sym),nxt,[sym,sym])

    # Determinism and bounded push.
    actions=defaultdict(set)
    for st,a,top in out:
        actions[(st,top)].add(a)
    conflicts={k:v for k,v in actions.items() if "" in v and len(v)>1}
    if conflicts:
        raise AssertionError(("epsilon/input conflict",p,q,endmarker,conflicts))
    if max((len(r) for _,r in out.values()),default=0)>2:
        raise AssertionError(("pushbound",p,q,endmarker))

    return states,out,role_state

def verify_compact(limit=45,max_input_length=8):
    failures=[]; pairs=0; runs=0; maxroles=0
    for p in range(1,limit+1):
        for q in range(1,limit+1):
            if gcd(p,q)!=1: continue
            pairs+=1
            for endmarker in (False,True):
                states,tr,roles=compile_push2(p,q,endmarker)
                maxroles=max(maxroles,len(roles))
                expected=max(p,q)+(0 if endmarker else 1)
                if len(states)!=expected:
                    failures.append(["state_count",p,q,endmarker,len(states),expected]); break

                def eps(st,stack):
                    guard=0
                    while (st,"",stack[0]) in tr:
                        st2,repl=tr[(st,"",stack[0])]
                        stack=list(repl)+stack[1:]; st=st2
                        guard+=1
                        if guard>4*max(p,q)+20:
                            raise AssertionError(("epsloop",p,q,endmarker,st,stack))
                    return st,stack

                def run(w):
                    st="R0" if endmarker else "Z"; stack=[Z0]; pref=""
                    st,stack=eps(st,stack)
                    for a in w:
                        key=(st,a,stack[0])
                        if key not in tr: return False,("missing",pref,st,a,stack)
                        st2,repl=tr[key]
                        stack=list(repl)+stack[1:]; st=st2; pref+=a
                        st,stack=eps(st,stack)
                        es,est=encode(p,q,rho(p,q,pref),endmarker)
                        if (st,stack)!=(es,est):
                            return False,("encoding",pref,st,stack,es,est,rho(p,q,pref))
                    if endmarker:
                        key=(st,"$",stack[0])
                        if key not in tr: return False,("blocked$",st,stack)
                        st2,repl=tr[key]; stack=list(repl)+stack[1:]; st=st2
                        st,stack=eps(st,stack)
                        return st=="R0",("end",st,stack)
                    return st=="Z",("end",st,stack)

                for n in range(max_input_length+1):
                    for bits in product("01",repeat=n):
                        w="".join(bits); runs+=1
                        acc,info=run(w); exp=(rho(p,q,w)==0)
                        if acc!=exp:
                            failures.append(["acceptance",p,q,endmarker,w,acc,exp,info]); break
                    if failures: break
                if failures: break
            if failures: break
        if failures: break

    return {
        "parameter_limit":limit,
        "coprime_pairs":pairs,
        "two_models_per_pair":True,
        "input_lengths":f"0..{max_input_length}",
        "total_machine_runs":runs,
        "all_checks_passed":not failures,
        "failures":failures,
        "max_suffix_roles_observed":maxroles,
        "verified_claims":[
            "four stack symbols suffice for the paired-sign push-at-most-2 construction",
            "no-endmarker state count is max(p,q)+1",
            "right-endmarker state count is max(p,q)",
            "negative side may use X as its sentinel directly, eliminating transient Y",
            "long push suffix roles fit in unused opposite-sign state/top cells",
            "exact paired residual encoding is restored after every forced normalization"
        ]
    }



# ---------------------------------------------------------------------------
# Paper-level reproducibility suite
# Completion Frontiers and Quotient Geometry in Deterministic Pushdown
# Automata for Rational Binary Counting — Alp Eren Bütün
# ---------------------------------------------------------------------------

from collections import deque
from functools import lru_cache
import argparse
import time


def _hist_step(state, stack, symbol):
    """One core-projected recognition step of the original 2:1 machine.

    `stack` is the logical stack (top at index 0); the physical Z0 is omitted.
    The wrapper q_s/q_f is represented through the core projection used in the paper.
    """
    top = stack[0] if stack else None
    rest = stack[1:] if stack else ""

    if state == "C":
        if top is None:
            return ("C", "10" if symbol == "1" else "11")
        if symbol == "1" and top == "0":
            return "L", rest
        if symbol == "0" and top == "1":
            return "R", rest
        if symbol == top:  # 1,1/eps or 0,0/eps
            return "C", rest

    elif state == "L":
        if top == "0" and symbol == "0":
            return "L", rest
        if top == "0" and symbol == "1":
            return "C", "000" + rest
        if top is None and symbol == "0":
            return "C", "10"
        if top is None and symbol == "1":
            return "C", "00"

    elif state == "R":
        if top == "1" and symbol == "0":
            return "C", "111111" + rest
        if top is None and symbol == "0":
            return "C", "11111"
        if top == "0" and symbol == "0":
            return "C", "111" + rest
        if top == "0" and symbol == "1":
            return "C", rest
        if top is None and symbol == "1":
            return "C", "11"
        if top == "1" and symbol == "1":
            return "C", "111" + rest

    raise AssertionError(("missing historical transition", state, stack, symbol))


def _hist_normal_form(state, stack):
    if state == "C":
        return (not stack or set(stack) <= {"0"} or set(stack) <= {"1"} or stack == "10")
    if state == "L":
        return set(stack) <= {"0"}
    if state == "R":
        return set(stack) <= {"1"} or stack == "0"
    return False


def _hist_weight(stack):
    return 2 * stack.count("0") - stack.count("1")


_HIST_PHI = {"C": 0, "L": 3, "R": -3}


def _hist_complete(state, stack):
    """Apply the right-endmarker completion rule after core projection."""
    if state == "C":
        return stack
    if state == "L":
        if not stack:
            return "100"
        assert stack[0] == "0"
        return "1000" + stack[1:]
    if state == "R":
        if not stack:
            return "111"
        if stack[0] == "1":
            return "1111" + stack[1:]
        assert stack[0] == "0"
        return "1" + stack[1:]
    raise AssertionError(state)


def _hist_canonical_completion(residual):
    if residual >= 0:
        if residual % 2 == 0:
            return "0" * (residual // 2)
        m = (residual - 1) // 2
        return "1" + "0" * (m + 1)
    return "1" * (-residual)


@lru_cache(maxsize=None)
def _length_first_oracle(p, q, residual):
    """Independent shortest-length oracle.

    Searches total completion length L increasingly and solves
       (p+q)x - qL = residual,  y=L-x.
    It does not call the canonical two-block completion routine.
    """
    L = 0
    while True:
        num = residual + q * L
        if num % (p + q) == 0:
            x = num // (p + q)
            if 0 <= x <= L:
                return L
        L += 1


def verify_historical(max_input_length=18):
    failures = []
    inputs = 0
    prefix_checks = 0
    for n in range(max_input_length + 1):
        for bits in product("01", repeat=n):
            w = "".join(bits)
            inputs += 1
            state, stack, residual = "C", "", 0

            if not _hist_normal_form(state, stack):
                failures.append(["initial_normal_form", w, state, stack])
                break

            for i, a in enumerate(w, 1):
                state, stack = _hist_step(state, stack, a)
                residual += 1 if a == "1" else -2
                prefix_checks += 1

                if not _hist_normal_form(state, stack):
                    failures.append(["normal_form", w[:i], state, stack])
                    break
                represented = _hist_weight(stack) + _HIST_PHI[state]
                if represented != residual:
                    failures.append(["residual_invariant", w[:i], state, stack,
                                     represented, residual])
                    break
            if failures:
                break

            normalized = _hist_complete(state, stack)
            expected = _hist_canonical_completion(residual)
            if normalized != expected:
                failures.append(["completion_normalization", w, state, stack,
                                 residual, normalized, expected])
                break
            if len(normalized) != _length_first_oracle(2, 1, residual):
                failures.append(["minimum_length", w, residual, normalized,
                                 _length_first_oracle(2, 1, residual)])
                break
            if set(normalized) != set(normalized[:2]):
                failures.append(["depth_two_visibility", w, residual, normalized])
                break
        if failures:
            break

    return {
        "max_input_length": max_input_length,
        "binary_inputs": inputs,
        "prefix_transition_checks": prefix_checks,
        "all_checks_passed": not failures,
        "failures": failures,
        "verified_claims": [
            "original-machine reachable-store normal form",
            "original-machine residual invariant",
            "right-endmarker completion normalization",
            "completion length agrees with an independent length-first oracle",
            "depth-two symbol-support visibility"
        ]
    }


def _reverse_bfs_distances(p, q, max_distance):
    """Exact directed distances to zero, computed independently by reverse BFS."""
    dist = {0: 0}
    todo = deque([0])
    while todo:
        s = todo.popleft()
        d = dist[s]
        if d == max_distance:
            continue
        # Reverse of r --1--> r+q and r --0--> r-p.
        for pred in (s - q, s + p):
            if pred not in dist:
                dist[pred] = d + 1
                todo.append(pred)
    return dist


def verify_general_arithmetic(limit=60, max_length=150):
    failures = []
    pairs = 0
    sphere_cases = 0
    distance_checks = 0

    for p in range(1, limit + 1):
        for q in range(1, limit + 1):
            if gcd(p, q) != 1:
                continue
            pairs += 1
            dist = _reverse_bfs_distances(p, q, max_length)
            cycle = p + q

            for n in range(max_length + 1):
                sphere_cases += 1
                exact = 0
                residuals_at_n = set()
                for x in range(n + 1):
                    y = n - x
                    r = p * x - q * y
                    distance_checks += 1
                    d = dist.get(r)
                    if d is None:
                        failures.append(["bfs_missing", p, q, n, x, y, r])
                        break

                    geodesic_criterion = (x < q or y < p)
                    if d == n:
                        exact += 1
                        residuals_at_n.add(r)
                        if not geodesic_criterion:
                            failures.append(["criterion_false_negative", p, q, n, x, y, r])
                            break
                    else:
                        if geodesic_criterion:
                            failures.append(["criterion_false_positive", p, q, n, x, y, r, d])
                            break
                        k = min(x // q, y // p)
                        expected = n - k * cycle
                        if d != expected:
                            failures.append(["cycle_reduction", p, q, n, x, y, r, d, expected])
                            break
                if failures:
                    break

                expected_sphere = min(n + 1, cycle)
                if exact != expected_sphere or len(residuals_at_n) != expected_sphere:
                    failures.append(["sphere_size", p, q, n, exact,
                                     len(residuals_at_n), expected_sphere])
                    break
            if failures:
                break
        if failures:
            break

    return {
        "parameter_limit": limit,
        "coprime_pairs": pairs,
        "length_range": f"0..{max_length}",
        "sphere_cases": sphere_cases,
        "distance_checks": distance_checks,
        "distance_oracle": "reverse BFS in the directed quotient graph",
        "all_checks_passed": not failures,
        "failures": failures,
        "verified_claims": [
            "balanced-cycle reduction gives the minimum Parikh pair",
            "a pair is geodesic iff x<q or y<p",
            "exact quotient-sphere size is min(n+1,p+q)",
            "all checked completion distances agree with an independent graph BFS"
        ]
    }


def _apos(p, s):
    return 0 if s == 0 else s - p


def _bneg(q, t):
    return 0 if t == 0 else q - t


def verify_formula_audit(limit=80):
    failures = []
    pairs = 0
    for p in range(1, limit + 1):
        for q in range(1, limit + 1):
            if gcd(p, q) != 1:
                continue
            pairs += 1
            roles_expected = abs(p - q)

            if p > q:
                ds = []
                for u in range(q):
                    up = (u + p) % q
                    num = p - _bneg(q, u) + _bneg(q, up)
                    if num % q:
                        failures.append(["d_not_integral", p, q, u, num])
                        break
                    d = num // q
                    if d < 1:
                        failures.append(["d_nonpositive", p, q, u, d])
                        break
                    ds.append(d)
                if failures:
                    break
                if sum(ds) != p or sum(d - 1 for d in ds) != p - q:
                    failures.append(["d_sum", p, q, sum(ds),
                                     sum(d - 1 for d in ds), p, p - q])
                    break
            elif q > p:
                cs = []
                for s in range(p):
                    sp = (s + q) % p
                    num = _apos(p, s) + q - _apos(p, sp)
                    if num % p:
                        failures.append(["c_not_integral", p, q, s, num])
                        break
                    c = num // p
                    if c < 1:
                        failures.append(["c_nonpositive", p, q, s, c])
                        break
                    cs.append(c)
                if failures:
                    break
                if sum(cs) != q or sum(c - 1 for c in cs) != q - p:
                    failures.append(["c_sum", p, q, sum(cs),
                                     sum(c - 1 for c in cs), q, q - p])
                    break

            expected_rules = 3 * (p + q) + 2 + roles_expected
            for endmarker in (False, True):
                states, transitions, role_state = compile_push2(p, q, endmarker)
                if len(role_state) != roles_expected:
                    failures.append(["suffix_role_count", p, q, endmarker,
                                     len(role_state), roles_expected])
                    break
                if len(transitions) != expected_rules:
                    failures.append(["transition_count", p, q, endmarker,
                                     len(transitions), expected_rules])
                    break
                expected_states = max(p, q) + (0 if endmarker else 1)
                if len(states) != expected_states:
                    failures.append(["state_count", p, q, endmarker,
                                     len(states), expected_states])
                    break
            if failures:
                break
        if failures:
            break

    return {
        "parameter_limit": limit,
        "coprime_parameter_pairs": pairs,
        "all_checks_passed": not failures,
        "failures": failures,
        "verified_claims": [
            "exact suffix-role count is |p-q|",
            "sum identities for the heavy-direction coefficients",
            "transition count is 3(p+q)+2+|p-q| in both acceptance conventions",
            "compiled state counts agree with max(p,q)+1 / max(p,q)"
        ]
    }


def _timed(label, fn, *args):
    t0 = time.perf_counter()
    result = fn(*args)
    result["elapsed_seconds"] = round(time.perf_counter() - t0, 3)
    return label, result


def run_suite(paper=False):
    if paper:
        settings = {
            "historical": (verify_historical, (18,)),
            "general_arithmetic": (verify_general_arithmetic, (60, 150)),
            "compact_push_at_most_two": (verify_compact, (45, 8)),
            "formula_audit": (verify_formula_audit, (80,)),
        }
    else:
        settings = {
            "historical": (verify_historical, (12,)),
            "general_arithmetic": (verify_general_arithmetic, (15, 40)),
            "compact_push_at_most_two": (verify_compact, (10, 6)),
            "formula_audit": (verify_formula_audit, (20,)),
        }

    out = {
        "paper": "Completion Frontiers and Quotient Geometry in Deterministic Pushdown Automata for Rational Binary Counting",
        "author": "Alp Eren Bütün",
        "mode": "paper" if paper else "quick",
        "python_standard_library_only": True,
        "sections": {},
    }
    total_start = time.perf_counter()
    for label, (fn, args) in settings.items():
        name, result = _timed(label, fn, *args)
        out["sections"][name] = result
        if not result.get("all_checks_passed", False):
            break
    out["all_checks_passed"] = all(
        r.get("all_checks_passed", False) for r in out["sections"].values()
    ) and len(out["sections"]) == len(settings)
    out["elapsed_seconds"] = round(time.perf_counter() - total_start, 3)

    if paper and out["all_checks_passed"]:
        h = out["sections"]["historical"]
        g = out["sections"]["general_arithmetic"]
        c = out["sections"]["compact_push_at_most_two"]
        f = out["sections"]["formula_audit"]
        expected = {
            "historical_binary_inputs": 524287,
            "general_distance_checks": 25281628,
            "compact_machine_runs": 1282610,
            "formula_coprime_pairs": 3931,
        }
        observed = {
            "historical_binary_inputs": h["binary_inputs"],
            "general_distance_checks": g["distance_checks"],
            "compact_machine_runs": c["total_machine_runs"],
            "formula_coprime_pairs": f["coprime_parameter_pairs"],
        }
        out["paper_claim_counts"] = {"expected": expected, "observed": observed,
                                     "match": expected == observed}
        out["all_checks_passed"] = out["all_checks_passed"] and expected == observed
    return out


def main():
    parser = argparse.ArgumentParser(
        description="Reproduce the computational validation reported in Section 9 of the paper."
    )
    parser.add_argument(
        "--paper", action="store_true",
        help="Run the exact paper-level parameter ranges (slower)."
    )
    args = parser.parse_args()
    result = run_suite(paper=args.paper)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["all_checks_passed"] else 1)


if __name__ == "__main__":
    main()
