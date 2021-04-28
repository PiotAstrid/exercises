# Write your code here
def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        return all(n / x != round(n / x) for x in range (2, n -1))