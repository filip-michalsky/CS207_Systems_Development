import numpy as np
def reaction_rate_multi(v_ij_reac,v_ij_proc,x,k):
    """Returns the rection rate for a set of species
    
    INPUTS
    =======
    v_ij_reac: vector of stochiometric coefficients of reactants
    v_ij_proc: vector of stochiometric coefficients of products
    x: vector of concentrations (first dimension needs to match v_i),second dimension is 1
    k: float
        
    RETURNS
    ========
    Reaction rates of the species (a string based on number of species)
       according to the formula k*[A]^v_i[a]*[B]*v_i[b]*[C]^v_i[c] for progress rate and
       dXi/dt = sum(v_ij_proc-v_ij_reac)*progress rate
       
       unless v_ij = v_ij_proc-v_ij_reac has the first dimension not matching
       the first dimension of x which returns a ValueError
       unless shape of v_ij_proc does not match the shape of x, which will return ValueError as well
       
    
    EXAMPLES
    =========
    >>> import numpy as np
    >>> reaction_rate_multi(np.array([[1.0,2.0],[2.0,0.0],[0.0,2.0]]),np.array([[0.0,1.0],[0.0,2.0],[1.0,0.0]]),np.array([1.0,2.0,1.0]),10)[0][0]
    -50.0
    >>> reaction_rate_multi(np.array([[1.0,2.0],[2.0,0.0],[0.0,2.0]]),np.array([[0.0,1.0],[0.0,2.0],[1.0,0.0]]),np.array([1.0,2.0,1.0]),10)[1][0]
    -60.0
    >>> reaction_rate_multi(np.array([[1.0,2.0],[2.0,0.0],[0.0,2.0]]),np.array([[0.0,1.0],[0.0,2.0],[1.0,0.0]]),np.array([1.0,2.0,1.0]),10)[2][0]
    20.0
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
        product_X_to_vij=product_X_to_vij.reshape(len(product_X_to_vij),1)
        progress_rate_multi=k*product_X_to_vij
        #print(product_X_to_vij.shape)
        #print(progress_rate_multi.shape)
        #print((v_ij_proc-v_ij_reac).shape)
        #calculate reaction rates for each species
        reaction_rates=np.dot((v_ij_proc-v_ij_reac),progress_rate_multi)
        
        
        
        return reaction_rates
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()