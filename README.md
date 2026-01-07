# dpda-ones-double-zeros

PDA recognizing the language L = { w ∈ {0, 1}* | n₁(w) = 2 · n₀(w) }

This repository contains a PDA and a DPDA specifically constructed to recognize the binary language where the count of ones is exactly double the count of zeros. (including the empty string)

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
