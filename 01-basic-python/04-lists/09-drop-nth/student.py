# Write your code here
def drop_nth(xs, n):
    ab = xs[:n]
    xz = xs[n+1:]
    return ab + xz