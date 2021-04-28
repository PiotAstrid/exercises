# Write your code here
def contains_duplicates(xs):
    # return xs == [xs.add(x) for x in xs]
       
    return len(set(xs)) != len(xs)