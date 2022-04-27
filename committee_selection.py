import random
import math
import scipy.special as s

n_values = [500,1000] # numbers of parties
t_perc_values = [0.51,0.55,0.6] # percentages of honest parties
k_perc_values = [0.01,0.05,0.1,0.2,0.3] # percentages of size of the committee
alpha_threshold = 0.95

simulate = False

def committee_analysis(n,k,t):

    ### alpha computation
    def hypergeomtric_term(i):
        term = s.binom(t,k/2+i)*s.binom(n-t,k-(k/2+i))/s.binom(n,k)
        return(term)

    alpha = 0

    for i in range(1,int(k/2)+1):
        alpha += hypergeomtric_term(i)

    ### alpha_estimated computation
    if simulate:
        def simulate_committee_selection(n,k,t):
            N = [0] * (n-t) + [1] * t
            random.shuffle(N)

            K = random.sample(N,k) # committee
            # K = N[0:k] # selecting the first k parties is equivalent

            t_subset_perc = sum(K)/len(K)
            return(t_subset_perc)

        n_sim = 100000 # number of simulations
        n_success = 0 # numbers of times t_subset_perc is greater than 0.5

        for i in range(0,n_sim):
            n_success += (simulate_committee_selection(n,k,t) > 0.5)

        alpha_estimated = n_success / n_sim

    return(alpha)

print("| n | k | t | alpha > alpha_threshold = " + str(alpha_threshold) + " |\n|-|-|-|-|")

# compute and show results
for n in n_values:
    for k_perc in k_perc_values:
        for t_perc in t_perc_values:
            k = math.ceil(n * k_perc) # size of the committee
            t = math.ceil(n * t_perc) # number of honest parties

            alpha = committee_analysis(n,k,t)

            if alpha > alpha_threshold:
                print("|" + str(n) + " | " + str(k) + " (" + str(math.trunc(k/n*100)) + " %)" + " | "+ str(t) + " (" + str(math.trunc(t/n*100)) + " %)" + " | " + str(math.trunc(alpha*1000)/1000) + "|")
