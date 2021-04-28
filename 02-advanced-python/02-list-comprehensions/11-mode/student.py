# Write your code here
def freq(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n] = 0
        result[n] += 1
    return result


def mode(ns):
    return max(freq(ns).items(), key=lambda pair: pair[1])[0]