# Write your code here
def is_increasing(ns):
    for i in  range (0,len(ns)):
        x = ns[i]
        y = ns[i + 1]

        if ( x > y ):
            return False
        else:
            return True