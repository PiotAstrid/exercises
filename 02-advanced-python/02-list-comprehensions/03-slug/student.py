# Write your code here
def slug(name):
    lower = name.lower()
    apart = lower.split(" ")
    voorn = apart[0]
    achtern = apart[1:]


    return '-'.join(s for s in achtern + [voorn])