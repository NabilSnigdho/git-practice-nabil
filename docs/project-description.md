# Project Description

This project is a beginner-friendly Python calculator that covers:

- **Addition** — `add(a, b)`
- **Subtraction** — `subtract(a, b)`
- **Multiplication** — `multiply(a, b)`
- **Division** — `divide(a, b)` with zero-division guard

## Code Organization

| File | Role |
|------|------|
| `src/main.py` | Entry point; imports and calls calculator functions |
| `src/utils.py` | All arithmetic logic lives here |

## Error Handling

Division by zero raises a `ValueError` with a descriptive message instead of
crashing with an unhandled `ZeroDivisionError`.

## Purpose

Created as part of a Git practice exercise to learn version control fundamentals
including branching, merging, and resolving conflicts.
