# Write your code here
def nth_longest_string(n, strings):
    sortedstrings = sorted(strings, key=lambda p: len(p))
    
    return sortedstrings[-n]
