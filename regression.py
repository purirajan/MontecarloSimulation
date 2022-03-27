import numpy as np
from numpy . random import standard_normal , seed
from scipy.optimize import curve_fit
from polynomial import *
from Euler import*
from Max import *
def RegressionPUT(S0, T, M, r, N, delta, sigma, K):
    S =Euler(S0, T, M, r, N, delta, sigma)
    dt = T/M
    df = np.exp (-r* dt )
    coeff = np.zeros((M,4))
    Put_coeff = np.zeros((M+1,N))
    VPut = np.zeros((M+1,N))
    V_Put = Max_Put(S0, T, M, r, N, delta, sigma, K)
    
    for i in range(M-1,-1,-1):
        popt, pcov = curve_fit(func, S[i], V_Put[i+1]*df)
        coeff[i] = popt
        Put_coeff[i] = func(S[i],coeff[i,0],coeff[i,1],coeff[i,2],coeff[i,3])
        VPut[i]= np.maximum(V_Put[i], Put_coeff[i])
    V0_Put = df*np.sum(VPut[1])/N
    return V0_Put
def RegressionCALL(S0, T, M, r, N, delta, sigma, K):
    S= Euler(S0, T, M, r, N, delta, sigma)
    V_Call = Max_Call(S0, T, M, r, N, delta, sigma, K)
    dt = T/M
    df = np.exp (-r* dt )
    coeff = np.zeros((M,4))
    VCall = np.zeros((M+1,N))
    Call_coeff = np.zeros((M+1,N))
    for t in range(M-1,-1,-1):
        popt, pcov = curve_fit(func, S[t], V_Call[t+1]*df)
        coeff[t] = popt
        Call_coeff[t] = func(S[t],coeff[t,0],coeff[t,1],coeff[t,2],coeff[t,3])
        VCall[t]= np.maximum(V_Call[t], Call_coeff[t])
    V0_Call = df*np.sum(VCall[1])/N
    return V0_Call
