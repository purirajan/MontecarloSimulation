from Euler import *
def Max_Call(S0, T, M, r, N, delta, sigma, K):
    S  = Euler(S0, T, M, r, N, delta, sigma)
    VCall = np.zeros((M+1,N))
    Max_Call = np.maximum(S-K,0)
    V_Call = np.copy(Max_Call)
    return V_Call

def Max_Put(S0, T, M, r, N, delta, sigma, K):
    S = Euler(S0, T, M, r, N, delta, sigma)
    VPut = np.zeros((M+1,N))
    Max_Put = np.maximum(K-S,0)
    V_Put = np.copy(Max_Put)
    return V_Put
