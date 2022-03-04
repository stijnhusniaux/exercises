# Write your code here
def is_prime(ns):
    return ns > 1 and all( [ ns % k != 0 for k in range(2, ns) ] )
