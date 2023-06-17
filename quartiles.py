# quartiles.py
"""
This file contains a function to calculate quartiles of a dataset.
"""

import dataclasses


def calculate_quartiles(classes,total,n,frequency):
    """
    Calculates the quartiles of a dataset.
    """
    sorted_data = sorted(dataclasses)
    n = len(sorted_data)

    q1_index = int(n * 0.25)
    q2_index = int(n * 0.5)
    q3_index = int(n * 0.75)

    q1 = sorted_data[q1_index]
    q2 = sorted_data[q2_index]
    q3 = sorted_data[q3_index]

    return q1, q2, q3

