
import single_progress_r
import numpy as np


#!pytest --doctest-modules

def test_progress_rate_result():
    assert single_progress_r.progress_rate(np.array([2,1,0]),np.array([1,2,3]),10) == 20

def test_progress_rate_shapes():
    try:
        single_progress_r.progress_rate(np.array([2,1]),np.array([[2,1],[2,1],[2,1]]),10)
    except ValueError as err:
        assert(type(err) == ValueError)
        
#def test_arr_result():
#       assert reaction_coeffs.arr(A=10^7,E=10^3,T=10^2) == XX