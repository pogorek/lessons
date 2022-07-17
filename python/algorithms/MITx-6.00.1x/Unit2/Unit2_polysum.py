# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 23:04:32 2022

@author: Piotr Ogorek
"""

import math

def polysum(n, s):
    """
    Parameters
    ----------
    n : (int)
        Regular polygon has n number of sides.
    s : (int / float)
        Each side has length s.

    Returns
    -------
    sum : (float)
        Sum of the area and square of the perimeter of the regular polygon. 
        Rounded to 4 decimal places.
    """

    area = (0.25 * n * s * s) / (math.tan(math.pi / n))
    perimeter = n * s
    
    sum = area + perimeter * perimeter
    
    
    return round(sum, 4)
