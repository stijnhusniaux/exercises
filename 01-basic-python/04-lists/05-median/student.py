# Write your code here
def median(ns):
    '''
    // In JavaScript, xs.sort() changes xs, i.e., the sorting occurs "in place"
    // However, it isn't friendly to modify the parameter's value, so we take a copy
    // In Python, there is a separate sorting function that does not sort in place
    // but instead returns a new sorted list
    // Look for this function
    '''
    sortedNs = sorted(ns)

    i = len(sortedNs)//2

    if (len(sortedNs) % 2 == 0 ):
        return (sortedNs[i - 1] + sortedNs[i]) / 2
    else:
        return sortedNs[i]