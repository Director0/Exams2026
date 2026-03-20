def primes(n):
    answer = []
    d = 2
    while n > 1 and d ** 2 <= n:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    if n != 1:
        answer.append(n)
    return answer
