import random
import math

n = 1000 # number of parties
t_perc = 0.55 # percentage of honest parties

t = math.ceil(n * t_perc) # honest parties
N = [0] * (n-t) + [1] * t
random.shuffle(N)

k_perc = 0.6 # percentage representing the committee
K = random.sample(N,math.ceil(n * k_perc)) # committee
# K = N[0:k] # selecting the first k parties is equivalent

t_subset_perc = sum(K)/len(K)
print(t_subset_perc)
