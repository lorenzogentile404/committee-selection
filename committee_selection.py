import random
import math
import scipy.special as s

n_values = [500,1000] # numbers of parties
t_perc_values = [0.5,0.55,0.6] # percentages of honest parties
k_perc_values = [0.1,0.2,0.3] # percentages of size of the committee

def committee_analysis(n,t,k):
    ### alpha_threshold computation
    def hypergeomtric_term(i):
        term = s.binom(t,k/2+i)*s.binom(n-t,k-(k/2+i))/s.binom(n,k)
        return(term)

    alpha_threshold = 0

    for i in range(1,int(k/2)+1):
        alpha_threshold += hypergeomtric_term(i)

    ### alpha_threshold_estimated computation
    def simulate_committee_selection(n,t,k):
        N = [0] * (n-t) + [1] * t
        random.shuffle(N)

        K = random.sample(N,k) # committee
        # K = N[0:k] # selecting the first k parties is equivalent

        t_subset_perc = sum(K)/len(K)
        return(t_subset_perc)

    n_sim = 1000 # number of simulations
    n_success = 0 # numbers of times t_subset_perc is greater than 0.5

    for i in range(0,n_sim):
        n_success += (simulate_committee_selection(n,t,k) > 0.5)

    alpha_threshold_estimated = n_success / n_sim

    print("\nn = " + str(n))
    print("t = " + str(t) + " (" + str(math.trunc(t/n*100)) + " %)")
    print("k = " + str(k) + " (" + str(math.trunc(k/n*100)) + " %)")
    print("alpha_threshold = " + str(alpha_threshold))
    print("alpha_threshold_estimated = " + str(alpha_threshold_estimated))

# compute and show results
for n in n_values:
    for t_perc in t_perc_values:
        for k_perc in k_perc_values:
            t = math.ceil(n * t_perc) # number of honest parties
            k = math.ceil(n * k_perc) # size of the committee
            committee_analysis(n,t,k)
