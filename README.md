# dpda-ones-double-zeros

DPDA recognizing the language L = { w ∈ {0, 1}* | n₁(w) = 2 · n₀(w) }

This repository contains a PDA, DPDA and a formal DPDA specifically constructed to recognize the binary language where the count of ones is exactly double the count of zeros.  

**UPDATE (August 24, 2026)** 

I have integrated the last three papers into the monograph. After making some additional revisions and improvements, I uploaded the updated version as  
**monograph/Deterministic_Pushdown_Normalization_v2.pdf:** Mathematical Monograph v2

**UPDATE (August 23, 2026)** 
  
I have three more papers ready:  

**Farey_Recursive_Shortest_Completions_Universal_Spectra.pdf:** This paper develops a Farey-recursive theory of shortest completion profiles for rational balance languages, motivated by the completion-aware 2:1 DPDA. Its main contribution is an exact cross-parameter ordered Farey recursion that reconstructs mediant completion profiles from their parents, together with local parent recovery and universal scalar completion spectra depending only on p+q.  

**Barrier_Compression_and_Composition-Refined_Enumeration.pdf:** This paper develops a contact-preserving barrier-compression method, proposed here as a new reduction framework for refined lattice-path enumeration, motivated by the residual viewpoint of the earlier 2:1 DPDA work. It gives explicit determinant formulas for four fixed-composition rational Dyck path problems involving run, ratio-run, exact returns, and fixed ratio-signatures, with applications to arbitrary-boundary/partial Dyck paths and rational parking functions.  

**Explicit_Run_Return_Enumeration_Rational_Dyck_Paths.pdf:** This work derives from my original (2:1) DPDA solution, especially from its p:q generalization, and solves the explicit enumeration problem left open by Dai–Fu–Qiu: determining the number of rational Dyck paths with prescribed values of run and return, and likewise of ratio-run and return. The key bridge is the residual viewpoint: the (p) residual is identified with rational-path rank, and returns are shown to be exactly upper-barrier contacts in the coarea sequence. Combining forbidden coarea values, weighted LGV determinants, and inclusion–exclusion then yields a fully explicit formula involving only finite subset sums and integer determinants.  
  
**UPDATE (August 19, 2026)** 

I have added the final three papers in this research series:

**Write_Search_Cancel_Structural_Theory.pdf:** Structural Theory. Develops the Write–Search–Cancel framework for real-time pushdown normalization. It shows how writing, searching, and cancellation arise from a common semantic completion demand, while separating semantic information from its physical LIFO representation.  

**Semantic_Uniqueness_LIFO_Lift_Theory.pdf:** Uniqueness Theory. Establishes that the underlying semantic normalization behavior can be unique even when multiple physical LIFO representations realize it. It characterizes this separation through semantic lifts, representation freedom, and the conditions under which physical implementations preserve the same semantic evolution.  

**General_Theory_Real_Time_Pushdown_Normalization.pdf:** General Theory  

In addition, I wrote a book (actually, a 549-page mathematical monograph), which I have also uploaded. 

**Deterministic_Pushdown_Normalization.pdf:** Monograph (The synthesis of all the research) 

**UPDATE (August 15, 2026)**  

Three more papers are ready.  

**Real_Time_pq_DPDA_Generalization.pdf:** This is the paper that has excited me the most so far. Starting from my original 2:1 DPDA solution, I developed a general p:q DPDA construction. What makes the result particularly interesting to me is that the same general definition covers the other p:q cases and, when specialized back to p=2 and q=1, it reconstructs my original 2:1 DPDA.  

**Chronological_Carry_Refinement_and_pAdic_Root_Geometry.pdf:** This paper develops a third-order arithmetic refinement inspired by chronological correction events arising from a deterministic pushdown computation. It connects the resulting carry structure to Hessenberg operators, Stirling-type congruences, p-adic root lifting, valuation laws, and ramified quadratic extensions. The main theme is that a local computation-derived ordering can generate unexpectedly rich algebraic and p-adic structure.  

**From_Pushdown_Cancellation_to_Defect_Geometry_on_Fuss_Catalan_Paths.pdf:** This paper develops a defect-based geometry from ordered cancellation events in a deterministic pushdown computation and connects that structure to Fuss–Catalan paths. It gives an exact realization theory for correction signatures, identifies a Catalan zero-defect boundary, and derives a universal algebraic generating structure for higher defect levels. The main theme is how local pushdown cancellation dynamics can induce a precise combinatorial geometry.  

**UPDATE (August 15, 2026)**  

Three more papers have been developed.  

**binary_stack_alphabet_hierarchy_dpda.pdf:** This paper shows that, for general DPDAs with a fixed number of states, increasing the stack-alphabet size yields a genuine hierarchy, resolving the problem left open by Masopust for the model with epsilon moves. Its main technical result is a representation-independent lower bound, ∣Q∣∣Γ∣≥mk+1, obtained through a completion-slope argument.  

**exact_resource_frontiers_dpda.pdf:** This paper determines exact state–stack resource frontiers for DPDA representations that must faithfully realize the residual dynamics of rational binary counting languages. In particular, it shows that p+q states are necessary and sufficient with one work-stack symbol, while max(p,q) states are necessary and sufficient with two or more work-stack symbols, and it extends the analysis to bounded-push and other structured representation models.  

**higher_dimensional_completion_geometry_dpda.pdf:** This paper extends the shortest-completion viewpoint from binary counting to higher-dimensional linear counting languages and studies the resulting algebraic and topological geometry of shortest paths. It characterizes quotient structures arising from optimal Parikh completions, proves a contractible-versus-circle dichotomy in rank one, identifies the emergence of local holes at higher rank, and derives eventual periodic geodesic behavior along residual rays.  

**UPDATE (August 10, 2026)**  
I developed two papers using my DPDA solution.  
The First paper: **completion_frontiers_dpda.pdf**  
The Second paper: **exact_structure_resource_bounds_dpda.pdf**

**UPDATE (August 8, 2026)**  
Following an email discussion with an academic person with a PhD working in the field of Theory of Computation at a leading research institution, I learned that the problem has been solved before, meaning my DPDA solution is not the first. As a result, I removed the earlier Proposal document because it contained novelty claims that I could no longer support confidently.  

Instead of pursuing those claims, I reworked the project from a mathematical analysis perspective. The resulting manuscript develops the structure of the DPDA and its generalization using residuals, prefix quotients, shortest completions, quotient geometry, completion frontiers, and related deterministic pushdown constructions.  

The current manuscript is available in this repository as: **completion_frontiers_dpda.pdf**  
The computational validation material referenced in the manuscript is also included as: **paper_validation_suite.py**  

The validation script is intended as supplementary reproducibility material and does not replace the mathematical proofs in the manuscript.  

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
