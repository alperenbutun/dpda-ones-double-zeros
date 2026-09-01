# dpda-ones-double-zeros

DPDA recognizing the language L = { w ∈ {0, 1}* | n₁(w) = 2 · n₀(w) }

This repository contains a PDA, DPDA and a formal DPDA specifically constructed to recognize the binary language where the count of ones is exactly double the count of zeros.  

**UPDATE (September 1, 2026)**  
-------------------------------  

**Deterministic_Pushdown_Normalization_v7.pdf:**  
Mathematical Monograph v7. (The synthesis of all the research)

**Universal_k_Fibers.pdf:**  
In our preceding work, alongside the finite cubical geodesic compiler, we developed a structure theory of local optimal compatibility, proving prescribed-order separation and Boolean amplification of higher-order signatures. Building on that framework, the present work introduces the $k$-fiber viewpoint and proves the **Universal $k$-Fiber Theorem**. For arbitrary integers $n \ge r \ge 2$, one fixed periodic shortest-path system admits a common exact distance and a common complete compatibility truncation through order $r-1$, while its order-$r$ layer realizes every subset of the distinguished $r$-faces—equivalently, every r-uniform hypergraph on $n$ vertices—and attains the maximal capacity $2^{\binom{n}{r}}$ The work serves as a structural component of the monograph’s broader general theory, showing that even after exact distance and all lower-order optimal-compatibility information are fixed, the next-order layer can remain completely unconstrained.


**UPDATE (September 1, 2026)**  
-------------------------------  

**Deterministic_Pushdown_Normalization_v6.pdf:**  
Mathematical Monograph v6. (The synthesis of all the research)

**Compiling_Shortest_Paths.pdf:**  
We develop a finite cubical geodesic compiler for positive-cost finite-phase periodic shortest-path systems, together with a general framework for encoding exact optimal branching, shortest-prefix membership, commuting geodesic compatibility, canonical routes, and all shortest paths implicitly from finite arithmetic data. Beyond compilation, we develop a structure theory of local optimal compatibility and prove that its hierarchy is genuinely strict. For every prescribed order (k), there exist adjacent states with the same exact shortest distance and identical optimal-compatibility data through order (k-1), yet different compatibility at order (k). Consequently, no fixed bounded-order summary consisting of distance and lower-order compatibility universally determines the full local optimal-compatibility complex. We further prove a Boolean amplification theorem showing that independent products turn this separation into exponentially many distinct higher-order signatures.  


**UPDATE (August 31, 2026)**  
-------------------------------  

Four new papers have been integrated into the monograph.  
**Deterministic_Pushdown_Normalization_v5.pdf:** Mathematical Monograph v5  

**UPDATE (August 31, 2026)**  
-------------------------------  

The following works, arising from the original 2:1 framework and the optimal DPDA derived from it, and/or from the p:q generalization, have been uploaded.  

**Lattice_Convex_Realization_and_Rank_Raising_Topology.pdf‎:**  
The paper starts from the question of how topologically complicated the spaces of optimal or shortest-completion solutions can be. Rather than merely counting optimal solutions, it develops a lattice-convex realization framework together with rank-raising constructions that transfer low-rank structures into higher dimensions. The resulting theory produces tori, prisms, apex-type constructions, and nontrivial higher-dimensional homology, showing that optimal-fiber topology can remain unexpectedly rich even at fixed rank.

**Confluence_and_Normalization_Choice_in_Exact_Pushdown_Lifts.pdf:**  
The motivation is to determine whether different admissible normalization choices in an exact pushdown lift necessarily lead to the same final outcome. The paper characterizes the structural conditions under which confluence is preserved and identifies the local configurations that make the normalization result depend on the chosen processing schedule. It therefore explains precisely when normalization is choice-independent and when the order of local operations becomes mathematically significant.

**Unrestricted_State_Stack_Pareto_Frontiers_and_Bounded_Push_Tradeoffs.pdf‎:**  
The paper begins with the question of the intrinsic computational resources required for exact pushdown normalization, beyond the mere existence of a normalizing machine. It establishes representation-independent lower bounds, studies the additional constraints imposed by bounded-push models, and organizes the tradeoff between finite-state control and stack resources through Pareto frontiers. In this way, it gives a structural account of the state-stack complexity of exact normalization. 

**Fourth_Order_Chronological_Carry_Connected_Quadruples_Extension_Parameters_and_the_Stirling_Shadow.pdf‎:**  
The starting point is the higher-order structure suggested by lower-order chronological carry phenomena. The paper extends the theory to fourth order through connected quadruples, extension parameters, four-band transport, and explicit quartic formulas. The appearance of Stirling-type coefficient patterns, described as the Stirling shadow, indicates that the previously observed low-order identities belong to a broader higher-order arithmetic and chronological hierarchy.


**UPDATE (August 30, 2026)**  
-------------------------------  

Four papers have been integrated into the monograph.  
**Deterministic_Pushdown_Normalization_v4.pdf:** Mathematical Monograph v4  

**UPDATE (August 30, 2026)**  
-------------------------------

**Nonabelian_Completion_Holonomy_and_Sharp_LIFO_Carrier_Costs.pdf‎:**  
Arising from the existence of multiple shortest completions for the same residual in the p:q normalization, this work studies the geometry and topology of optimal completion fibers. It develops quotient complexes encoding commuting optimal actions, identifies nontrivial and nonabelian holonomy phenomena, and derives sharp carrier-cost results for their physical LIFO realization.

**Minimal_Cores_and_Pareto_Frontiers_of_Exact_Pushdown_Lifts.pdf:**  
Motivated by the passage from the original 2:1 construction to general p:q normalization, this work asks how much physical state and stack information is actually necessary to realize the same residual semantics exactly. It develops a theory of exact pushdown lifts, identifies minimal protected cores and interfaces, and establishes Pareto frontiers governing the trade-off between finite-state and stack resources.

**Causal_Hypergraphs_and_Exact_Schedule_Classification.pdf‎:** 
This work originates from the optional eager operations that appear when the operational ideas of the 2:1 DPDA are generalized to p:q normalization. It determines exactly which combinations of local scheduling modifications preserve correctness, encoding their interactions through causal hypergraphs and minimal fatal supports and thereby obtaining a complete classification of admissible schedules. 

**Operational_Enumeration_Rational_Pushdown_Normalization.pdf‎:** 
Starting from the p:q shortest-completion mechanism, this work observes that operational events such as WRITE, CANCEL, and carry behavior possess a refined combinatorial structure. It translates these events into statistics on rational lattice paths and derives refined enumeration, factorization, and explicit counting results for the resulting normalization processes.


**UPDATE (August 27, 2026)**  
-------------------------------  

The last three papers have been integrated into the monograph.  
**Deterministic_Pushdown_Normalization_v3.pdf:** Mathematical Monograph v3  

**UPDATE (August 26, 2026)**  
-------------------------------

**Unrestricted_Lower_Bounds_for_Lpq.pdf‎:**  
This work arises from our p:q generalization of the original 2:1 DPDA and the resulting residual-based study of how balance information can be represented across states and stack storage. It establishes **representation-independent lower bounds** for deterministic pushdown recognition of the rational binary balance languages Lpq. In particular, it proves the unrestricted lower bound **|Q| >= max(p,q),** and, under right-endmarker convention, determines the exact state complexity: **Qmin(Lpq) = max(p,q).** Thus the unrestricted lower bound is sharp. Also, in our earlier work, the corresponding representation-independent state-cost question was left open; the present paper resolves it completely.

**Fixed_Parikh_Random_Ordering_LIFO.pdf:**  
This work grew out of our \(p:q\) shortest-completion and physical-lift framework, where the same residual semantics can admit different stack-level realizations. This paper studies the quantitative behavior of LIFO normalization under uniformly random orderings with fixed Parikh data. It identifies distinct microscopic, mesoscopic, and macroscopic cost regimes, including Rayleigh-type rematerialization behavior and explicit asymptotic rates.

**Optimal_Fiber_Topology_Beyond_Kernel_Rank.pdf‎:** 
This work developed from our higher-dimensional shortest-completion analysis, where kernel rank first emerged as a structural parameter governing optimal-schedule fibers. The paper shows that kernel rank alone does not determine the full global geometry and gives a complete rank-two classification in terms of the active lattice translation structure of the optimal fiber.  


**UPDATE (August 24, 2026)** 
-------------------------------

I have integrated the last three papers into the monograph.  
After making some additional revisions and improvements, I uploaded the updated version as  
**Deterministic_Pushdown_Normalization_v2.pdf:** Mathematical Monograph v2  


**UPDATE (August 23, 2026)** 
-------------------------------

I have three more papers ready:  

**Farey_Recursive_Shortest_Completions_Universal_Spectra.pdf:** This paper develops a Farey-recursive theory of shortest completion profiles for rational balance languages, motivated by the completion-aware 2:1 DPDA. Its main contribution is an exact cross-parameter ordered Farey recursion that reconstructs mediant completion profiles from their parents, together with local parent recovery and universal scalar completion spectra depending only on p+q.  

**Barrier_Compression_and_Composition-Refined_Enumeration.pdf:** This paper develops a contact-preserving barrier-compression method, proposed here as a new reduction framework for refined lattice-path enumeration, motivated by the residual viewpoint of the earlier 2:1 DPDA work. It gives explicit determinant formulas for four fixed-composition rational Dyck path problems involving run, ratio-run, exact returns, and fixed ratio-signatures, with applications to arbitrary-boundary/partial Dyck paths and rational parking functions.  

**Explicit_Run_Return_Enumeration_Rational_Dyck_Paths.pdf:** This work derives from my original (2:1) DPDA solution, especially from its p:q generalization, and solves the explicit enumeration problem left open by Dai–Fu–Qiu: determining the number of rational Dyck paths with prescribed values of run and return, and likewise of ratio-run and return. The key bridge is the residual viewpoint: the (p) residual is identified with rational-path rank, and returns are shown to be exactly upper-barrier contacts in the coarea sequence. Combining forbidden coarea values, weighted LGV determinants, and inclusion–exclusion then yields a fully explicit formula involving only finite subset sums and integer determinants.  

  
**UPDATE (August 19, 2026)** 
-------------------------------

I have added the final three papers in this research series:

**Write_Search_Cancel_Structural_Theory.pdf:** Structural Theory. Develops the Write–Search–Cancel framework for real-time pushdown normalization. It shows how writing, searching, and cancellation arise from a common semantic completion demand, while separating semantic information from its physical LIFO representation.  

**Semantic_Uniqueness_LIFO_Lift_Theory.pdf:** Uniqueness Theory. Establishes that the underlying semantic normalization behavior can be unique even when multiple physical LIFO representations realize it. It characterizes this separation through semantic lifts, representation freedom, and the conditions under which physical implementations preserve the same semantic evolution.  

**General_Theory_Real_Time_Pushdown_Normalization.pdf:** General Theory  

In addition, I wrote a book (actually, a 549-page mathematical monograph), which I have also uploaded. 

**Deterministic_Pushdown_Normalization.pdf:** Monograph (The synthesis of all the research) 


**UPDATE (August 17, 2026)**  
-------------------------------

Three more papers are ready.  

**Real_Time_pq_DPDA_Generalization.pdf:** This is the paper that has excited me the most so far. Starting from my original 2:1 DPDA solution, I developed a general p:q DPDA construction. What makes the result particularly interesting to me is that the same general definition covers the other p:q cases and, when specialized back to p=2 and q=1, it reconstructs my original 2:1 DPDA.  

**Chronological_Carry_Refinement_and_pAdic_Root_Geometry.pdf:** This paper develops a third-order arithmetic refinement inspired by chronological correction events arising from a deterministic pushdown computation. It connects the resulting carry structure to Hessenberg operators, Stirling-type congruences, p-adic root lifting, valuation laws, and ramified quadratic extensions. The main theme is that a local computation-derived ordering can generate unexpectedly rich algebraic and p-adic structure.  

**From_Pushdown_Cancellation_to_Defect_Geometry_on_Fuss_Catalan_Paths.pdf:** This paper develops a defect-based geometry from ordered cancellation events in a deterministic pushdown computation and connects that structure to Fuss–Catalan paths. It gives an exact realization theory for correction signatures, identifies a Catalan zero-defect boundary, and derives a universal algebraic generating structure for higher defect levels. The main theme is how local pushdown cancellation dynamics can induce a precise combinatorial geometry.  


**UPDATE (August 15, 2026)**  
-------------------------------

Three more papers have been developed.  

**binary_stack_alphabet_hierarchy_dpda.pdf:** This paper shows that, for general DPDAs with a fixed number of states, increasing the stack-alphabet size yields a genuine hierarchy, resolving the problem left open by Masopust for the model with epsilon moves. Its main technical result is a representation-independent lower bound, ∣Q∣∣Γ∣≥mk+1, obtained through a completion-slope argument.  

**exact_resource_frontiers_dpda.pdf:** This paper determines exact state–stack resource frontiers for DPDA representations that must faithfully realize the residual dynamics of rational binary counting languages. In particular, it shows that p+q states are necessary and sufficient with one work-stack symbol, while max(p,q) states are necessary and sufficient with two or more work-stack symbols, and it extends the analysis to bounded-push and other structured representation models.  

**higher_dimensional_completion_geometry_dpda.pdf:** This paper extends the shortest-completion viewpoint from binary counting to higher-dimensional linear counting languages and studies the resulting algebraic and topological geometry of shortest paths. It characterizes quotient structures arising from optimal Parikh completions, proves a contractible-versus-circle dichotomy in rank one, identifies the emergence of local holes at higher rank, and derives eventual periodic geodesic behavior along residual rays.  


**UPDATE (August 10, 2026)**  
-------------------------------
I developed two papers using my DPDA solution.  
The First paper: **completion_frontiers_dpda.pdf**  
The Second paper: **exact_structure_resource_bounds_dpda.pdf**  


**UPDATE (August 8, 2026)**  
-------------------------------
Following an email discussion with an academic person with a PhD working in the field of Theory of Computation at a leading research institution, I learned that the problem has been solved before, meaning my DPDA solution is not the first. As a result, I removed the earlier Proposal document because it contained novelty claims that I could no longer support confidently.  

Instead of pursuing those claims, I reworked the project from a mathematical analysis perspective. The resulting manuscript develops the structure of the DPDA and its generalization using residuals, prefix quotients, shortest completions, quotient geometry, completion frontiers, and related deterministic pushdown constructions.  

-------------------------------  

**UPDATE (July 4, 2026)**  
I added a new automaton design that is rejecting the empty input. The triangle represents the start state. The automaton remains inactive as long as the input is empty; it only starts operating once a 1 or 0 is seen.

**UPDATE (January 10, 2026)**  
I have uploaded a proposal file (Proposal.pdf) to the repository, which documents and explains the work conducted during the process of reaching the Final Formal DPDA from the initial design.
  
**UPDATE (January 7, 2026)**  
In my spare time, I had spent hours trying to convert the first PDA design I shared into a formal DPDA, but I could not reach a result. However, I later discovered that it is actually possible to convert it into a DPDA using a very simple method. I applied this method and shared the file "DPDA.png".  

Subsequently, I revised the previously shared DPDA to make it more formal and uploaded it as "Formal_DPDA.png".

----------------------------------------------------------------------------------------------------------------------------------------------

**Details**  

The following observations may be useful:  

- **When the input string is empty**:
  - **In the Center state:**
    - If the stack is empty, then the original input already satisfies the condition *"the number of 1s is twice the number of 0s."*
    - If the stack is not empty, then appending the symbols currently in the stack to the original input yields a string in which the number of 1s is twice the number of 0s.
  - **In the Left state:**
    - If the stack is empty, appending `100` to the original input yields a string in which the number of 1s is twice the number of 0s.
    - If the top symbol of the stack is `1`, appending `0` to the original input yields such a string.
    - If the top symbol of the stack is `0`, appending `1000` to the original input yields such a string.
  - **In the Right state:**
    - If the stack is empty, appending `111` to the original input yields a string in which the number of 1s is twice the number of 0s.
    - If the top symbol of the stack is `1`, appending `1111` to the original input yields such a string.
    - If the top symbol of the stack is `0`, appending `1` to the original input yields such a string.
