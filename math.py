#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""
Module with usefull math functions
"""

from __future__ import annotations


def get_prime_multipliers(number: int) -> list:
    """
    Returns list of prime multipliers of given number
    """
    result: list[int] = []
    multipliers = [2, 3, 5, 7]
    multipliers.append(number)
    while number > 1:
        for i in multipliers:
            if number % i == 0:
                result.append(i)
                number = int(number / i)
                multipliers[-1] = number
                break
    return result


def get_number_devisors(number: int) -> list:
    """
    Returns list of devisors of given number
    """
    multipliers = get_prime_multipliers(number)
    for x_index, x_value in enumerate(multipliers):
        for y_index, y_value in enumerate(multipliers):
            devisor = multipliers[x_index] * multipliers[y_index]
            if number % devisor == 0 and devisor not in multipliers:
                multipliers.append(devisor)
    multipliers.insert(0, 1)
    result = list(set(multipliers))
    result.sort()
    return result

