import math
from fractions import Fraction


def prime_factors(n):
    primfac = set()
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.add(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.add(n)
    return primfac


def phi(n: int):
    result = Fraction(n, 1)
    factors = prime_factors(n)

    for i in factors:
        result *= (1 - Fraction(1, i))

    return result


if __name__ == "__main__":
    print("Prove Euler's Totient Theorem\n")

    print("When 'a' is relatively prime to 'm'")
    m = int(input("Please enter 'm':"))
    a = int(input("Please enter 'a':"))

    max_a = int(phi(m))
    print("\nphi(m) =", max_a)

    set_a = set()
    for num in range(1, max_a + 1):
        if math.gcd(num, m) == 1:
            set_a.add(num)

    print("\nRelative prime set in the range {1, 2, 3, ... m}:", set_a)

    set_b = set()
    for i in set_a:
        set_b.add(a * i)

    print("Set {an1, an2, an3, ... a(n(phi(m)))}:", set_b)

    print("\nResult:\n")

    count = 0
    for b in set_b:
        for a in set_a:
            if b % m == a % m:
                print(f"{a} ≡ {b} (mod {m})")
                count += 1
                break

    print(f"\nTotal {count} pairs found.")
    print("Length of {1, 2, 3, ... m}: ", len(set_a))
    print("Length of {an1, an2, an3, ... a(n(phi(m)))}: ", len(set_b))

    if count == len(set_a) == len(set_b):
        print(f"{count} = {len(set_a)} = {len(set_b)}, prove ends.")
