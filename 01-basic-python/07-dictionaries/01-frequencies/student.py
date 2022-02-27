# Write your code here
def frequencies(ns):
    result = {}

    for i in ns:
        if i not in result:
            result[i] = 0
        result[i] += 1
    return result
