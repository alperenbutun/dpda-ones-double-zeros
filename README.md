# dpda-ones-double-zeros

DPDA recognizing the language L = { w ∈ {0, 1}* | n₁(w) = 2 · n₀(w) }

This repository contains a PDA, DPDA and a formal DPDA specifically constructed to recognize the binary language where the count of ones is exactly double the count of zeros.  

**UPDATE (August 8, 2026)**  
Following an email discussion with a PhD academic person working in the field of Theory of Computation at a leading research institution, I learned that my DPDA-based solution to the underlying problem was not the first approach of its kind.  

As a result, I removed the earlier Proposal document from this repository because it contained novelty claims that I could no longer support confidently.  

Instead of pursuing those claims, I reworked the project from a mathematical analysis perspective. The resulting manuscript develops the structure of the DPDA and its generalization using residuals, prefix quotients, shortest completions, quotient geometry, completion frontiers, and related deterministic pushdown constructions.  

The current manuscript is available in this repository as: **completion_frontiers_dpda_v8.pdf**  
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
