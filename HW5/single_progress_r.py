
def progress_rate(v_i,x,k):
    """Returns the progress rate of a reaction
    
    INPUTS
    =======
    v_i: vector of stochiometric coefficients 
    x: vector of concentrations (first dimension needs to match v_i),second dimension is 1
    k: float, fixed value 8.314, should not change
        
    RETURNS
    ========
    Progress rate of the reaction
       k*[A]^v_i[a]*[B]*v_i[b]*[C]^v_i[c]
       unless first dimension of x does not match first dimension of v_i
       in which case a ValueError exception is raised
    
    EXAMPLES
    =========
    >>> import numpy as np
    >>> progress_rate(np.array([2,1,0]),np.array([1,2,3]),10)
    20
    """
    #v_i=np.array([2,1,0])
    #x=np.array([1,2,3])
    #k=10
    import numpy as np
    #check that the first dimension matches
    if x.shape[0] != v_i.shape[0]:
        raise ValueError("First dimension of x and v_i need to match")
    
    else:  
        product_X_to_vi=1
        #loop through the rows to multiply each x by its stochiometric coeffs
        for i,j in zip(v_i,x):
            product_X_to_vi=product_X_to_vi*(j**i)
    
        progress_rate=k*product_X_to_vi
        
        return progress_rate

if __name__ == "__main__":
    import doctest
    doctest.testmod()