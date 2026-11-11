#!/usr/bin/env python3
"""Compute and print the Collatz sequence starting from 27."""


def collatz_sequence(start):
    """Return the Collatz sequence from start down to 1, inclusive."""
    if start < 1:
        raise ValueError("start must be a positive integer")
    sequence = [start]
    n = start
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def verify(sequence):
    """Check that every transition follows n/2 (even) or 3n+1 (odd)."""
    for a, b in zip(sequence, sequence[1:]):
        expected = a // 2 if a % 2 == 0 else 3 * a + 1
        if b != expected:
            raise AssertionError(f"invalid transition {a} -> {b}, expected {expected}")
    if sequence[-1] != 1:
        raise AssertionError("sequence does not end at 1")


def main():
    start = 27
    sequence = collatz_sequence(start)
    verify(sequence)
    for n in sequence:
        print(n)
    print(f"Steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
