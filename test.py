import math, glob, os
import numpy as np

def area_rect(length, width):
    return length*width

def test_area_rect_1():
   assert area_rect(3,5) == 15

def test_area_rect_2():
   assert area_rect(2.5,4) == 10.0
