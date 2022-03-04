# Write your code here
def slug(string):
    res = string.split(' ')
    firstname = res[0]
    lastname = res[1:]

    return '-'.join(s.lower() for s in lastname + [firstname])