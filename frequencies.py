"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item_str = str(item)
        if item_str not in frequencies:
            frequencies[item_str] = 0
        frequencies[item_str] += 1
    return frequencies
