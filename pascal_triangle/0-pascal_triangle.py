#!/usr/bin/python3
"""
Module pour générer le triangle de Pascal
"""


def pascal_triangle(n):
    """
    Retourne une liste de listes d'entiers représentant
    le triangle de Pascal de n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(1, i):
            # Somme des deux éléments au-dessus
            val = prev_row[j - 1] + prev_row[j]
            current_row.append(val)

        current_row.append(1)
        triangle.append(current_row)

    return triangle
