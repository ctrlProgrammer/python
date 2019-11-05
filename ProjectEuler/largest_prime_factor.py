#
# https://projecteuler.net/problem=3
#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
#
#
#
# cual es el numero primo mas cercano a 600851475143

import os.path as path


class Prime():
    def __init__(self, primes_txt):
        self.primes_txt = primes_txt
        self.get_primes_txt()

    def is_prime(self, num):

        divisors = []

        for i in range(1, num + 1):
            div = num / i

            if(isinstance(div, float)):
                if div.is_integer():
                    div = int(div)

            if isinstance(div, int):
                divisors.append(i)

        if(len(divisors) == 2):
            return True
        else:
            return False

    def create_primes_array(self, max_prime):
        primes = []
        for i in range(1, max_prime):
            if self.is_prime(i):
                primes.append(i)
        return primes

    # Write txt with primes

    def write_primes_txt(self, max_prime):
        f = open(self.primes_txt, 'w')
        primes_array = self.create_primes_array(max_prime)
        primes_array = ",".join(str(int_) for int_ in primes_array)
        if f.write(primes_array):
            return True

    def get_primes_txt(self):
        # Read txt
        if(path.exists(self.primes_txt)):
            f = open(self.primes_txt)
            primes_array = f.read()

            # Seaparate all element with ,
            primes_array = primes_array.split(',')

            # Convert all elements to integer
            for i in range(0, len(primes_array)):
                primes_array[i] = int(primes_array[i])

            return primes_array
        else:
            self.write_primes_txt(10000)


def get_first_factor(num, primes):
    get = True
    counter = 0
    while get:
        counter += 1
        if(num % primes[counter] == 0):
            get = False

    return primes[counter]


primes = Prime('utils/primes_array.txt')
primes_array = primes.get_primes_txt()

bucle = True
num = 600851475143
factors = []

while bucle:
    factor = get_first_factor(num, primes_array)
    factors.append(factor)
    num = num / factor
    if(num == 1):
        bucle = False

print(factors)