# Day 27 — Tuple Methods and Operations

## Learning goals
- Count repeated values using `count()`.
- Find a value's position using `index()`.
- Join tuples with the `+` operator.
- Get the number of items using `len()`.
- Modify tuple data indirectly by converting it to a list and back.

## Key ideas
- Tuples are immutable, so you cannot assign directly to `tuple[index]`.
- `index(value, start, stop)` searches within the specified index range; `stop` is excluded.
- Concatenation creates a new tuple and leaves the original tuples unchanged.
- Converting to a list allows item changes, but converting back creates a new tuple.
