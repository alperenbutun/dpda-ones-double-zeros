# dpda-ones-double-zeros
PDA recognizing the language L = { w ∈ {0, 1}* | n₁(w) = 2 · n₀(w) }

This repository contains a Pushdown Automaton (PDA) specifically constructed to recognize the binary language where the count of ones is exactly double the count of zeros. (including the empty string)

**Details**  
If the automaton reaches the Center state with empty input and an empty stack, the string is accepted. Otherwise, the string is rejected.

Additionally, the following observations may be useful:

- **When the input string is empty**
  (either the computation starts with the empty string or the input has been fully consumed):
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
