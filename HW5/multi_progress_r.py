import numpy as np
def progress_rate_multi(v_ij_reac,v_ij_proc,x,k):
    """Returns the progress rate of a set of reactions
    
    INPUTS
    =======
    v_ij_reac: vector of stochiometric coefficients of reactants
    v_ij_proc: vector of stochiometric coefficients of products
    x: vector of concentrations (first dimension needs to match v_i),second dimension is 1
    k: float
        
    RETURNS
    ========
    Progress rates of the reactions (a string based on number of reactions)
       according to the formula k*[A]^v_i[a]*[B]*v_i[b]*[C]^v_i[c]
       unless v_ij = v_ij_proc-v_ij_reac has the first dimension not matching
       the first dimension of x which returns a ValueError
       unless shape of v_ij_proc does not match the shape of x, which will return ValueError as well
       
    
    EXAMPLES
    =========
    >>> import numpy as np
    >>> progress_rate_multi(np.array([[1.0,2.0],[2.0,0.0],[0.0,2.0]]),np.array([[0.0,0.0],[0.0,1.0],[2.0,1.0]]),np.array([1.0,2.0,1.0]),10)[0]
    40.0
    >>> progress_rate_multi(np.array([[1.0,2.0],[2.0,0.0],[0.0,2.0]]),np.array([[0.0,0.0],[0.0,1.0],[2.0,1.0]]),np.array([1.0,2.0,1.0]),10)[1]
    10.0

    """
    import numpy as np
    #calculate the effective stochiometric coefficients on the reactants side
    
    
    #check length of product coeffs and reac coeffs is the same
    if v_ij_proc.shape != v_ij_reac.shape:
        raise ValueError("Dimensions of stochiometric coeffs need to match")
    
    #check that the first dimension matches
    elif x.shape[0] != v_ij_proc.shape[0]:
        raise ValueError("First dimension of x and v_i need to match")
    
    else:
        v_ij = v_ij_reac
        product_X_to_vij = 1
        
        #loop through the rows to multiply each x by its stochiometric coeffs
        for i,j in zip(v_ij,x):
            #print("i,j")
            #print(i,j)
            #print("j**i")
            #print(j**i)
            product_X_to_vij=product_X_to_vij*(j**i)
            #print("product")
            #print(product_X_to_vij)
        progress_rate_multi=k*product_X_to_vij
        
        return progress_rate_multi

if __name__ == "__main__":
    import doctest
    doctest.testmod()