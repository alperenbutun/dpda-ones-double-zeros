#!/usr/bin/env python3
from math import gcd, comb

checks=0

def ck(cond, payload=None):
    global checks
    assert cond, payload
    checks += 1

# ---------- arithmetic helpers ----------
def fast_min_demand(p,q,r):
    if r==0:
        return (0,0)
    if r>0:
        y=0 if p==1 else (-r * pow(q,-1,p)) % p
        x=(r+q*y)//p
        return (x,y)
    x=0 if q==1 else (r * pow(p,-1,q)) % q
    y=(p*x-r)//q
    return (x,y)

def brute_min_demand_small(p,q,r):
    # Deliberately independent bounded search, used on a smaller adversarial grid.
    B=abs(r)+p*q+p+q+8
    best=None
    for x in range(B+1):
        num=p*x-r
        if num>=0 and num%q==0:
            y=num//q
            cand=(x+y,x,y)
            if best is None or cand<best:
                best=cand
    assert best is not None
    return best[1],best[2]

def geo_first(p,q,r,mu=None):
    x,y=mu if mu is not None else fast_min_demand(p,q,r)
    return ({'0'} if x>0 else set()) | ({'1'} if y>0 else set())

def canonical(p,q,r,mu=None):
    x,y=mu if mu is not None else fast_min_demand(p,q,r)
    if r>0: return '1'*y+'0'*x
    if r<0: return '0'*x+'1'*y
    return ''

def support_depth(word):
    full=set(word)
    if not full: return 0
    seen=set()
    for d,ch in enumerate(word,1):
        seen.add(ch)
        if seen==full: return d
    raise AssertionError(word)

# ---------- original DPDA core ----------
def step_core(state, stack, a):
    top=stack[0] if stack else 'Z'; rest=stack[1:] if stack else ''
    if state=='C':
        if a=='1' and top=='0': return ('L',rest)
        if a=='0' and top=='1': return ('R',rest)
        if a=='1' and top=='1': return ('C',rest)
        if a=='0' and top=='0': return ('C',rest)
        if a=='1' and top=='Z': return ('C','10')
        if a=='0' and top=='Z': return ('C','11')
    if state=='L':
        if a=='0' and top=='0': return ('L',rest)
        if a=='0' and top=='Z': return ('C','10')
        if a=='1' and top=='0': return ('C','000'+rest)
        if a=='1' and top=='Z': return ('C','00')
    if state=='R':
        if a=='0' and top=='1': return ('C','111111'+rest)
        if a=='0' and top=='Z': return ('C','11111')
        if a=='0' and top=='0': return ('C','111'+rest)
        if a=='1' and top=='0': return ('C',rest)
        if a=='1' and top=='Z': return ('C','11')
        if a=='1' and top=='1': return ('C','111'+rest)
    return None

def run_core(c,w):
    for a in w:
        c=step_core(c[0],c[1],a)
        if c is None: return None
    return c

def D(S): return 2*S.count('0')-S.count('1')
PHI={'C':0,'L':3,'R':-3}
def residual_config(c): return D(c[1])+PHI[c[0]]

def psi(k,i,j):
    if j==0:
        if 0<=i<=k: return ('L','0'*(k-i))
        if i==k+1: return ('C','10')
        if i==k+2: return ('R','0')
    if j==1 and 0<=i<=k+2: return ('C','0'*(k+2-i))
    raise ValueError

# exact state-potential audit
transitions=[
('C','1','Z','10','C'),('C','0','Z','11','C'),('C','1','0','','L'),('L','0','0','','L'),
('L','0','Z','10','C'),('L','1','0','000','C'),('L','1','Z','00','C'),('C','0','1','','R'),
('R','0','1','111111','C'),('R','0','Z','11111','C'),('R','0','0','111','C'),('R','1','0','','C'),
('R','1','Z','11','C'),('R','1','1','111','C'),('C','1','1','','C'),('C','0','0','','C')]
for qs,a,top,repl,qt in transitions:
    rest='00111' if top!='Z' else ''
    old=('' if top=='Z' else top)+rest; new=repl+rest
    ck((D(new)+PHI[qt])-(D(old)+PHI[qs])==(1 if a=='1' else -2),(qs,a,top))

# original materialization
def normalize_original(c):
    q,S=c
    if q=='C': return S
    if q=='L': return '100' if not S else '1000'+S[1:]
    if q=='R':
        if not S: return '111'
        if S[0]=='1': return '1111'+S[1:]
        ck(S=='0',c); return '1'
    raise AssertionError(c)

families=[('C',''),('C','10'),('R','0'),('L',''),('R','')]
for m in range(1,201):
    families += [('C','0'*m),('C','1'*m),('L','0'*m),('R','1'*m)]
for c in families:
    ck(normalize_original(c)==canonical(2,1,residual_config(c)),c)

# original ladder, reachability, diamonds
ladder_paths=0
for k in range(0,151):
    ck(run_core(('C',''),'1'*(2*k+3))==('L','0'*k),('reach',k))
    c=('L','0'*k); ck(residual_config(c)==2*k+3)
    ck(fast_min_demand(2,1,2*k+3)==(k+2,1))
    for i in range(k+3):
        w='0'*i+'1'+'0'*(k+2-i)
        ck(run_core(c,w)==('C',''),(k,i,w))
        ck(run_core(c,'0'*i)==psi(k,i,0))
        ck(run_core(c,'0'*i+'1')==psi(k,i,1))
        ladder_paths += 1
    for i in range(k+2):
        b=psi(k,i,0)
        ck(run_core(b,'01')==run_core(b,'10')==psi(k,i+1,1),(k,i))

# locality families
for m in range(1,201):
    for c,exp in [(('C','0'*m),{'0'}),(('C','1'*m),{'1'}),(('L','0'*m),{'0','1'}),(('R','1'*m),{'1'})]:
        ck(geo_first(2,1,residual_config(c))==exp,c)
ck(geo_first(2,1,1)=={'0','1'}); ck(geo_first(2,1,-1)=={'1'}); ck(geo_first(2,1,0)==set())

# independent brute-force cross-check of unique minimum demand
brute_cases=0
for p in range(1,13):
  for q in range(1,13):
    if gcd(p,q)!=1: continue
    for r in range(-60,61):
        ck(fast_min_demand(p,q,r)==brute_min_demand_small(p,q,r),(p,q,r))
        brute_cases+=1

# broad arithmetic checks without repeated brute force
arith_cases=0
for p in range(1,51):
  for q in range(1,51):
    if gcd(p,q)!=1: continue
    M=max(p,q)
    for r in range(-500,501):
        x,y=fast_min_demand(p,q,r)
        ck(x>=0 and y>=0 and p*x-q*y==r,(p,q,r,x,y))
        ck(not (x>=q and y>=p),(p,q,r,x,y))
        if r>0:
            ck(x>0 and y<p)
            ck(geo_first(p,q,r,(x,y))==({'0'} if r%p==0 else {'0','1'}))
        elif r<0:
            ck(y>0 and x<q)
            ck(geo_first(p,q,r,(x,y))==({'1'} if r%q==0 else {'0','1'}))
        else:
            ck((x,y)==(0,0)); ck(geo_first(p,q,r,(x,y))==set())
        ck(set(canonical(p,q,r,(x,y)))==geo_first(p,q,r,(x,y)))
        ck(support_depth(canonical(p,q,r,(x,y)))<=M)
        arith_cases+=1
    if p>1:
        ck(fast_min_demand(p,q,q)==(q,p-1)); ck(support_depth(canonical(p,q,q))==p)
    if q>1:
        ck(fast_min_demand(p,q,-p)==(q-1,p)); ck(support_depth(canonical(p,q,-p))==q)

# ---------- compact paired-sign normalized configuration graph ----------
def a_base(p,s): return 0 if s==0 else s-p
def b_base(q,t): return 0 if t==0 else q-t

def eta_compact(p,q,r):
    if r==0: return (0,'Z')
    if r>0:
        s=r%p; a=a_base(p,s); k=(r-a)//p
        ck(k>=1 and p*k+a==r)
        return (s,'0'*k+'Z')
    t=(-r)%q; b=b_base(q,t); k=(b-r)//q
    ck(k>=1 and -q*k+b==r)
    return (t,'1'*k+'X')

def compact_macro_step(p,q,r,ch):
    state,stack=eta_compact(p,q,r)
    if r==0:
        out=eta_compact(p,q,q if ch=='1' else -p)
    elif r>0:
        s=r%p; ck(state==s and stack[0]=='0')
        if ch=='0':
            rest=stack[1:]
            if rest.startswith('0'): out=(s,rest)
            else:
                ck(rest=='Z'); out=(0,'Z') if s==0 else eta_compact(p,q,a_base(p,s))
        else:
            sp=(s+q)%p; num=a_base(p,s)+q-a_base(p,sp)
            ck(num%p==0); c=num//p; ck(c>=0)
            out=(sp,'0'*(c+1)+stack[1:])
    else:
        t=(-r)%q; ck(state==t and stack[0]=='1')
        if ch=='1':
            rest=stack[1:]
            if rest.startswith('1'): out=(t,rest)
            else:
                ck(rest=='X'); out=eta_compact(p,q,b_base(q,t))
        else:
            tp=(t+p)%q; num=p-b_base(q,t)+b_base(q,tp)
            ck(num%q==0); d=num//q; ck(d>=0)
            out=(tp,'1'*(d+1)+stack[1:])
    expected=eta_compact(p,q,r+(q if ch=='1' else -p))
    ck(out==expected,(p,q,r,ch,out,expected))
    return out

macro_cases=0
for p in range(1,31):
  for q in range(1,31):
    if gcd(p,q)!=1: continue
    for r in range(-300,301):
        compact_macro_step(p,q,r,'0'); compact_macro_step(p,q,r,'1')
        macro_cases += 2

# exact configuration-level rectangle samples
rectangle_vertices=0
rectangle_diamonds=0
for p in range(1,19):
  for q in range(1,19):
    if gcd(p,q)!=1: continue
    for r in range(-80,81):
        x,y=fast_min_demand(p,q,r)
        seen=set()
        for i in range(x+1):
          for j in range(y+1):
            rr=r-p*i+q*j; c=eta_compact(p,q,rr)
            ck(c not in seen,(p,q,r,i,j,c)); seen.add(c)
            if i<x: ck(compact_macro_step(p,q,rr,'0')==eta_compact(p,q,rr-p))
            if j<y: ck(compact_macro_step(p,q,rr,'1')==eta_compact(p,q,rr+q))
            if i<x and j<y:
                target=eta_compact(p,q,rr-p+q)
                ck(compact_macro_step(p,q,rr-p,'1')==target)
                ck(compact_macro_step(p,q,rr+q,'0')==target)
                rectangle_diamonds += 1
            rectangle_vertices += 1
        ck(len(seen)==(x+1)*(y+1))

# displayed p=3,q=2,r=4 example
for r,c in [(4,(1,'00Z')),(1,(1,'0Z')),(-2,(0,'1X')),(6,(0,'00Z')),(3,(0,'0Z')),(0,(0,'Z'))]:
    ck(eta_compact(3,2,r)==c,(r,c))

# ---------- raw one-step conjugacy: four-symbol defects and three-symbol repair ----------

def compact_raw_step4(p,q,r,ch):
    """Immediate one-input transition of the four-symbol right-endmarker semantic schema.
    Returns the immediate configuration before any forced epsilon normalization.
    """
    state,stack=eta_compact(p,q,r)
    if r==0:
        return eta_compact(p,q,q if ch=='1' else -p)
    if r>0:
        s=r%p
        ck(state==s and stack[0]=='0')
        if ch=='0':
            return (s,stack[1:])
        sp=(s+q)%p
        num=a_base(p,s)+q-a_base(p,sp)
        ck(num%p==0); c=num//p; ck(c>=0)
        return (sp,'0'*(c+1)+stack[1:])
    t=(-r)%q
    ck(state==t and stack[0]=='1')
    if ch=='1':
        return (t,stack[1:])
    tp=(t+p)%q
    num=p-b_base(q,t)+b_base(q,tp)
    ck(num%q==0); d=num//q; ck(d>=0)
    return (tp,'1'*(d+1)+stack[1:])

def defect4_expected(p,q,r,ch):
    return (ch=='0' and 1 <= r <= p-1) or (ch=='1' and -q <= r <= -1)

# Boundary-compatible three-symbol construction. Z denotes Z0.
def eta3_pgeq(p,q,r):
    ck(p>=q>=1 and gcd(p,q)==1)
    if r>=0:
        k,s=divmod(r,p)
        return (s,'0'*k+'Z')
    u=r % q
    h=(u-r)//q
    ck(h>=1 and r==u-q*h)
    return (u,'1'*h+'Z')

def raw_step3_pgeq(p,q,conf,ch):
    state,stack=conf
    top=stack[0]
    rest=stack[1:]
    if top=='0':
        if ch=='0':
            return (state,rest)
        sp=(state+q)%p
        c=(state+q-sp)//p
        ck(c in (0,1))
        return (sp,'0'*(c+1)+rest)
    if top=='Z':
        if ch=='1':
            sp=(state+q)%p
            c=(state+q-sp)//p
            ck(c in (0,1))
            return (sp,'0'*c+'Z')
        u=(state-p)%q
        h=(u+p-state)//q
        ck(h>=1)
        return (u,'1'*h+'Z')
    if top=='1':
        ck(state<q)
        if ch=='1':
            return (state,rest)
        up=(state-p)%q
        d=(up-state+p)//q
        ck(d>=1)
        return (up,'1'*(d+1)+rest)
    raise AssertionError((p,q,conf,ch))

def eta3(p,q,r):
    if p>=q:
        return eta3_pgeq(p,q,r)
    # Involution: swap 0/1 and p/q, and replace r by -r.
    state,stack=eta3_pgeq(q,p,-r)
    table=str.maketrans({'0':'1','1':'0','Z':'Z'})
    return (state,stack.translate(table))

def raw_step3(p,q,r,ch):
    conf=eta3(p,q,r)
    if p>=q:
        return raw_step3_pgeq(p,q,conf,ch)
    table=str.maketrans({'0':'1','1':'0','Z':'Z'})
    state,stack=conf
    swapped=(state,stack.translate(table))
    swapped_ch='1' if ch=='0' else '0'
    out=raw_step3_pgeq(q,p,swapped,swapped_ch)
    return (out[0],out[1].translate(table))

raw4_cases=0
raw4_defects=0
raw3_cases=0
for p in range(1,31):
  for q in range(1,31):
    if gcd(p,q)!=1: continue
    local_defects=set()
    for r in range(-500,501):
      for ch in '01':
        immediate=compact_raw_step4(p,q,r,ch)
        expected=eta_compact(p,q,r+(q if ch=='1' else -p))
        defect=(immediate!=expected)
        ck(defect==defect4_expected(p,q,r,ch),(p,q,r,ch,immediate,expected))
        if defect: local_defects.add((r,ch)); raw4_defects+=1
        raw4_cases += 1

        got3=raw_step3(p,q,r,ch)
        exp3=eta3(p,q,r+(q if ch=='1' else -p))
        ck(got3==exp3,(p,q,r,ch,got3,exp3))
        raw3_cases += 1
    # The scanned interval contains the complete finite defect set.
    ck(len(local_defects)==p+q-1,(p,q,len(local_defects),p+q-1))
    ck(local_defects==({(s,'0') for s in range(1,p)} | {(-j,'1') for j in range(1,q+1)}),(p,q,local_defects))

# raw rectangle criterion for the old four-symbol positive-zero orientation
raw_rectangle_cases=0
for p in range(1,21):
  for q in range(1,21):
    if gcd(p,q)!=1: continue
    for r in range(-120,121):
        x,y=fast_min_demand(p,q,r)
        all_raw=True
        for i in range(x+1):
          for j in range(y+1):
            rr=r-p*i+q*j
            if i<x and defect4_expected(p,q,rr,'0'): all_raw=False
            if j<y and defect4_expected(p,q,rr,'1'): all_raw=False
        criterion=(r==0) or (r>0 and r%p==0)
        ck(all_raw==criterion,(p,q,r,x,y,all_raw,criterion))
        raw_rectangle_cases += 1

# three-symbol raw rectangle samples: every edge is literally one input transition
raw3_rectangle_vertices=0
raw3_rectangle_diamonds=0
for p in range(1,16):
  for q in range(1,16):
    if gcd(p,q)!=1: continue
    for r in range(-60,61):
        x,y=fast_min_demand(p,q,r)
        seen=set()
        for i in range(x+1):
          for j in range(y+1):
            rr=r-p*i+q*j; conf=eta3(p,q,rr)
            ck(conf not in seen,(p,q,r,i,j,conf)); seen.add(conf)
            if i<x: ck(raw_step3(p,q,rr,'0')==eta3(p,q,rr-p))
            if j<y: ck(raw_step3(p,q,rr,'1')==eta3(p,q,rr+q))
            if i<x and j<y:
                c01=raw_step3(p,q,rr,'0')
                c01=raw_step3(p,q,rr-p,'1')
                c10=raw_step3(p,q,rr,'1')
                c10=raw_step3(p,q,rr+q,'0')
                target=eta3(p,q,rr-p+q)
                ck(c01==c10==target,(p,q,r,i,j,c01,c10,target))
                raw3_rectangle_diamonds += 1
            raw3_rectangle_vertices += 1
        ck(len(seen)==(x+1)*(y+1))

# displayed p=3,q=2,r=4 three-symbol example
for r,c in [(4,(1,'0Z')),(1,(1,'Z')),(-2,(0,'1Z')),(6,(0,'00Z')),(3,(0,'0Z')),(0,(0,'Z'))]:
    ck(eta3(3,2,r)==c,(r,c))

# phase periods and conservation, modular direct checks
phase_samples=0
for p in range(1,31):
  for q in range(1,31):
    if gcd(p,q)!=1: continue
    M=max(p,q)
    for B in range(1,M+21):
        hp=p//gcd(B,p); hm=q//gcd(B,q); H=hp+hm
        ck(B*H*H>=4*p*q)
        for s in {0,min(1,B-1)}:
            z=2
            while s+B*z<=0: z+=1
            ys=[fast_min_demand(p,q,s+B*(z+t))[1] for t in range(hp+1)]
            ck(ys[0]==ys[-1]); ck(len(set(ys[:-1]))==hp)
            z=-2
            while s+B*z>=0: z-=1
            xs=[fast_min_demand(p,q,s+B*(z-t))[0] for t in range(hm+1)]
            ck(xs[0]==xs[-1]); ck(len(set(xs[:-1]))==hm)
            phase_samples += 1

# infinite family
for k in range(2,1001):
    p=k*k; q=k*k-1; B=k*(k+1)
    ck(gcd(B,p)==k); ck(gcd(B,q)==k+1)
    H=p//gcd(B,p)+q//gcd(B,q)
    ck(H==2*k-1); ck(B*H==2*k**3+k*k-k)

print('PASS')
print('checks',checks)
print('brute_minimum_cases',brute_cases)
print('broad_arithmetic_cases',arith_cases)
print('compact_macro_cases',macro_cases)
print('configuration_rectangle_vertices',rectangle_vertices)
print('configuration_rectangle_diamonds',rectangle_diamonds)
print('phase_samples',phase_samples)
print('raw4_cases',raw4_cases)
print('raw4_defects',raw4_defects)
print('raw3_cases',raw3_cases)
print('raw_rectangle_cases',raw_rectangle_cases)
print('raw3_rectangle_vertices',raw3_rectangle_vertices)
print('raw3_rectangle_diamonds',raw3_rectangle_diamonds)
print('ladder_paths',ladder_paths)
