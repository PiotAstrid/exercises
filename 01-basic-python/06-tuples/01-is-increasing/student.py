# Write your code here
def is_increasing(ns):
    if len(ns) == 0:
        return True
    boo = True
    for n in range(len(ns) -1):
        if ns[n] > ns[n + 1]:
            boo = False
        
    return boo
    
