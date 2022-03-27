Purpose:  
                We are going to program Monte Carlo simulation in Python for computing the values of an
                European call and put. The call or put option is written on an underlying asset, which follows a
                geometric Brownian motion,

	                 dSt = (mu-delta)*St*dt + sigma*St*dW
	           
                where St is the time t value of the underlying asset, mu is mean return, delta is a continuously compounded
                dividend yield, sigma is volatility, and Wt is a Wiener process with W0 = 0.
                Thenvalues of the two European options are determined by their discounted risk-neutral expectations:
	            
	Algorithm: The computation involves a built-in fucntion, scipy.stats.norm.cdf(x), to compute standard cumulative normal
	           distribution  and change in weiner process. 
                We generate sample paths for St,and we use the explicit Euler method and the Milstein method.
	
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
                   
    Analytical Solution: The outcomes of this program tells us that Milstein method is better than the Euler's method because 
                         the truncation error of the Milstein method is less than the Euler's method.
	---------------------------------------------------------------------------------------------"""

# Valuation of European Put Option
# by Monte Carlo Simulation
def d1(S, K, r, delta, sigma, T):
   return (log(S/K) + (r -delta + sigma**2 / 2) * T)/(sigma * sqrt(T))
 
def d2(S, K, r, delta, sigma, T):
    return (d1(S, K, r,delta, sigma, T) - (sigma * sqrt(T)))
    
from numpy import *
from numpy . random import standard_normal , seed
import scipy.stats as ss
## Parameters
S0 = 100 # initial stock price
K = 100  # strike price
T = 1.0 # maturity time
sigma = 0.75 # volatility
delta= 0.025 # time continous dividend yield
r = 0.03 # interest rate
## Simulation Parameters
seed (10 ) # seed generator
M = int(input(" Enter the number of time steps(M) for dt(=T/M):")) # time steps
I = 1000 # simulation paths
dt = T/M # length of time interval
df = exp (-r* dt ) # discount factor per time interval

random.seed(10)

vc= S0 * ss.norm.cdf(d1(S0, K, r, delta, sigma, T)) * exp((-delta) * T) - K * exp(-r * T) * ss.norm.cdf(d2(S0, K, r,delta, sigma, T))
vp= -S0 * ss.norm.cdf(-d1(S0, K, r, delta, sigma, T)) * exp((-delta) * T) + K * exp(-r * T) * ss.norm.cdf(-d2(S0, K, r,delta, sigma, T))

## Index Level Path Generation
S= zeros (( M+1 ,I))
MS = zeros((M+1,I)) 

S[0 ,:]= S0 # initial values for the Euler Method
MS[0 ,:]= S0 # initial values for the Milstein Method
for i in range (1 ,M+1 ,1 ): 
    ran = standard_normal (I) #  random numbers
    S[i,:]=S[i-1,:]+ S[i-1,:]*(r*dt+ sigma*ran*sqrt(dt)) # Explicit Euler method
    MS[i,:]=MS[i-1,:]+ MS[i-1,:]*(r*dt+sigma*ran*sqrt(dt)+.5*sigma**2*(ran**2*dt-dt)) # Milstein Method
######################################################################
E_call_payoff = maximum(S[-1]-K,0)
E_put_payoff= maximum (K -S[ -1], 0) 
######################################################################
M_call_payoff = maximum(MS[-1]-K,0)
M_put_payoff= maximum (K -MS[ -1], 0) 
####################################################################
Euro_put_value = exp (-r *T )* sum( E_put_payoff )/ I 
Euro_call_value = exp (-r *T )* sum( E_call_payoff )/ I
#############################################################
M_Euro_put_value = exp (-r *T )* sum( M_put_payoff )/ I 
M_Euro_call_value = exp (-r *T )* sum( M_call_payoff )/ I
############################################################
E_error1= abs( Euro_put_value -  vp) # vp denotes the exact european put price
E_error2= abs( Euro_call_value - vc) # vc denotes the exact european call price
############################################################# 
M_error1= abs(M_Euro_put_value -  vp ) # E-error denotes error by the Euler Method.
M_error2= abs(M_Euro_call_value - vc ) # M_error denotes error by the Milstein Method.
##########################################################################

print"             Parameters                      "
print " *******************************************"
print"S0 = 100 # initial stock price"
print"K = 100  # strike price"
print"T = 1.0 #  maturity time"
print"sigma = 0.75 # volatility"
print"delta= 0.025 # time continous dividend yield"
print"r = 0.03 # interest rate"
print"seed (10 ) # seed generator"
print"M = 100 or 1000 # time steps"
print"I = 1000 # simulation paths"
print " *******************************************"
## Output
print "         Euler Method                        "
print " *******************************************"

print " European Put Option Value from Euler method is %.6f" % Euro_put_value
print " ----------------------------------------"
print " European call Option Value from Euler method %.6f" % Euro_call_value
print " ----------------------------------------"
print " Truncation error for put option from Euler method is %.6f" % E_error1
print " ----------------------------------------"
print " Truncation error for call option from Euler method is %.6f" % E_error2

print " *******************************************"
print "         Milstein Method                     "
print " *******************************************"

print " European Put Option Value from Milstein method is %.6f" % M_Euro_put_value
print " ----------------------------------------"
print " European call Option Value from Milstein method %.6f" % M_Euro_call_value
print " ----------------------------------------"
print " Truncation error for put option from Milstein method is %.6f" % M_error1
print " ----------------------------------------"
print " Truncation error for call option from Milstein method is %.6f" % M_error2
print " ----------------------------------------"
##############################################################################
