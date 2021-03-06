# Write your code here
def median(ns):
    xs = sorted(ns)
    ab = len(ns)
    if ab % 2 == 0:
        er = ab // 2 -1
        tw = ab // 2 
        med = (xs[er] + xs[tw]) / 2
        return med
    else:
        return xs[ab // 2 ]
