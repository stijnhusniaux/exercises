# Write your code here
def rotate(xs,n):
    for _ in range(n):
        res = xs.pop(0)
        xs.append(res)
