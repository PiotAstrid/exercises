# Write your code here
def contains_duplicates(xs):
    for k in range(len(xs)):
        for l in range(k + 1, len(xs)):
            if xs[k] == xs[l]: 
                return True
    return False