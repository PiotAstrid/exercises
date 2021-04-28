# Write your code here
from collections import OrderedDict

def remove_duplicates(xs):
  # zelf gevonden
  #  return list(OrderedDict.fromkeys(xs))

    found = set()
    result = []

    for x in xs:
        if x not in found:
            result.append(x)
            found.add(x)
    return result


