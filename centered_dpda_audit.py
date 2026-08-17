#!/usr/bin/env python3
"""Reference audit for the centered p:q DPDA draft.

This script is verification support, not a proof.  It explores distinct reachable
configurations by BFS and checks the residual invariant, depth-two qualitative
visibility, transition totality, and zero-residual characterization.
"""
from collections import deque
from math import gcd


def mu(p, q, r):
    # Unique minimum nonnegative solution of p*x-q*y=r.
    # Search only over the bounded residue coordinate y in [0,p-1] first.
    for y in range(p):
        n = r + q * y
        if n >= 0 and n % p == 0:
            return n // p, y
    # The minimum point may instead be on the x<q side for negative r.
    for x in range(q):
        n = p * x - r
        if n >= 0 and n % q == 0:
            return x, n // q
    raise AssertionError((p, q, r))


def eta(x, y):
    if x >= y:
        return "10" * y + "0" * (x - y)
    return "10" * x + "1" * (y - x)


def step(p, q, d, stack, a):
    m = p + q
    h = (m - 1) // 2
    if stack:
        z, tail = stack[0], stack[1:]
        if a == z:
            return d, tail
        if a == "1" and z == "0":
            if d < h:
                return d + 1, tail
            return 0, eta(*mu(p, q, (h + 1) * m)) + tail
        if a == "0" and z == "1":
            if d > -h:
                return d - 1, tail
            return 0, eta(*mu(p, q, -(h + 1) * m)) + tail
        raise AssertionError((d, stack, a))
    r = d * m + (-p if a == "0" else q)
    return 0, eta(*mu(p, q, r))


def conf_residual(p, q, d, stack):
    return p * stack.count("0") - q * stack.count("1") + d * (p + q)


def two_visible(stack):
    return set(stack) == set(stack[:2])


def audit_ratio(p, q, depth=80):
    start = (0, "")
    queue = deque([(start, 0, "")])
    seen = {start}
    while queue:
        (d, stack), level, word = queue.popleft()
        rho = q * word.count("1") - p * word.count("0")
        assert rho == conf_residual(p, q, d, stack), (p, q, "invariant", word, d, stack)
        assert two_visible(stack), (p, q, "visibility", word, d, stack)
        assert (rho == 0) == (d == 0 and stack == ""), (p, q, "zero", word, d, stack)
        if level == depth:
            continue
        for a in "01":
            nd, ns = step(p, q, d, stack, a)
            key = (nd, ns)
            if key not in seen:
                seen.add(key)
                queue.append((key, level + 1, word + a))
    return len(seen)


def main():
    tested = 0
    total_configs = 0
    for p in range(1, 21):
        for q in range(1, 21):
            if gcd(p, q) != 1:
                continue
            total_configs += audit_ratio(p, q, 80)
            tested += 1
    print(f"PASS: {tested} ordered coprime ratios, 1<=p,q<=20")
    print(f"Distinct reached configurations checked (summed across ratios): {total_configs}")


if __name__ == "__main__":
    main()
