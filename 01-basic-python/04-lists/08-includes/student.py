# Write your code here
def includes(xs, ys):
    for  y in  ys :
        #// Look for a way to check for list membership in Python
        if y not in xs:
            return False

    return True
