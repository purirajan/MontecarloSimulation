import numpy as np
def Euler(S0, T, M, r, N, delta, sigma):
    np.random.seed(123)
    dt = float(T)/M
    S = np.zeros((M+1,N))
    S[0] = S0 
    Z = np.random.standard_normal((M,N)) 
    dW = np.sqrt(dt)*Z                                        
    for i in range(M):
        S[i+1] = S[i] * (1.0 + (r - delta)*dt + sigma* dW[i])
    return  S
