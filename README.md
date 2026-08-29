# Smart Calculator 🧮

A command-line calculator built with Python that evaluates mathematical expressions using a restricted expression evaluator.

## Features

- Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Supports modulo (`%`), exponentiation (`**`), and parentheses.
- Handles division-by-zero errors.
- Rejects unsupported expressions instead of executing arbitrary Python code.
- Runs continuously until the user types `exit`.

## Requirements

- Python 3.11 or later recommended.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python Calculator.py
   ```

## Example

```text
===== SMART CALCULATOR =====
Enter any mathematical expression.
Use +, -, *, /, %, ** and brackets ().
Type 'exit' to close the calculator.

Enter expression: 2+3*4
Result = 14
```

## Concepts Practiced

- Python functions
- Loops and conditional statements
- Exception handling
- Abstract Syntax Trees (`ast`)
- Operator mapping with the `operator` module

## Author

Devansh Agrawal