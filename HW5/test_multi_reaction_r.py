
import multi_reaction_r as mr
import numpy as np
import doctest
doctest.testmod(verbose=True)


def test_reaction_rate_result():
    #test the result og the function
    v_ij_reac = np.array([[1.0,2.0],[2.0,0.0],[0.0,2.0]])
    v_ij_proc = np.array([[0.0,1.0],[0.0,2.0],[1.0,0.0]])
    x = np.array([1.0,2.0,1.0])
    k = 10
    assert mr.reaction_rate_multi(v_ij_reac , v_ij_proc, x , k )[0][0] == -50.0
    assert mr.reaction_rate_multi(v_ij_reac , v_ij_proc, x , k )[1][0] == -60.0
    assert mr.reaction_rate_multi(v_ij_reac , v_ij_proc, x , k )[2][0] == 20.0
    
def test_progress_rate_shapes_with_x():
    #test whether shape of coeffs v_i matches shape of concentrations x
    try:
        mr.reaction_rate_multi(np.array([2,1]),np.array([2,1]),np.array([[2,1],[2,1],[2,1]]),10)
    except ValueError as err:
        assert(type(err) == ValueError)
        
def test_progress_rate_shapes_coeffs():
    #test whether the shape of v_ij's matches
    try:
        mr.reaction_rate_multi(np.array([2,1,1]),np.array([2,1]),np.array([[2,1],[2,1],[2,1]]),10)
    except ValueError as err:
        assert(type(err) == ValueError)