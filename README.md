# Python Type Error Example
This repository demonstrates a common Python error: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. This error arises when trying to perform arithmetic operations (like summation) on a list containing both numbers and strings.  The provided code showcases the error and offers a robust solution.

## How to Reproduce
1. Clone this repository.
2. Run `bug.py`. You'll see the TypeError.
3. Run `bugSolution.py` to see the improved code handling the error.

## Solution
The solution involves adding input validation to check if all elements in the list are numbers before attempting the sum operation.  This avoids the `TypeError` and makes the code more robust.