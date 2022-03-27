Purpose:  
                We are going to program Monte Carlo simulation in Python for computing the values of an
                American call and put. The call or put option is written on an underlying asset, which follows a
                geometric Brownian motion,

	                 dSt = (mu-delta)*St*dt + sigma*St*dW
	           
                where St is the time t value of the underlying asset, mu is mean return, delta is a continuously compounded
                dividend yield, sigma is volatility, and Wt is a Wiener process with W0 = 0.
                Then values of the two American options are determined by their discounted risk-neutral expectations:
	            
	Algorithm: The computation involves a built-in fucntion, scipy.stats.norm.cdf(x), to compute standard cumulative normal
	           distribution  and change in weiner process. 
                We generate sample paths for St,and we  have used explicit Euler method.
	
	Arguments: S - Price of underlying asset at time t = 0.
	           K - Strike price
	           T - Maturity date, measured in fraction (or a multiple) of a year. T > 0
	           sigma - Standard deviation of log (S)
	           delta - Dividend yield rate (dividends are paid continuously over time)
                 r - interest rate
	
	Usage:	   
                   S0 = 100 # initial stock price
                   K = 100  # strike price
                   T = 1.0 # maturity time
                   sigma = 0.75 # volatility
                   delta= 0.025 # time continous dividend yield
                   r = 0.03 # interest rate
                   mu = 0.08 #return rate
                   
    Analytical Solution: We got value of the American Call and Put price is increasing with decreasing number of time steps. 
	---------------------------------------------------------------------------------------------"""

# Monter Carlo Simulations for the valuation of American Option
# by regression Method
import numpy as np
from polynomial import *
from Euler import *
from Max import *
from regression import*
def main():
    S0 = 100 # initial stock price
    K = 100  # strike price
    T = 1.0 # maturity time
    sigma = 0.75 # volatility
    delta= 0.025 # time continous dividend yield
    r = 0.03 # interest rate
    N= 1000 # number of simulations path
    seed (123) # seed generator
    print ('\n%15s   %12s   %20s' %('Time Step', 'American Call Price', 'American Put Price'))
    for n in range(1,3):
        M = 10*pow(10,n)
        dt =float( T)/M
        V0_Call  = RegressionCALL(S0, T, M, r, N, delta, sigma, K)
        V0_Put  = RegressionPUT(S0, T, M, r, N, delta, sigma, K)
        print ('%12.1f %16.6f %22.6f' % (M, V0_Call, V0_Put))
main()
