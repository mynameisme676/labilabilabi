import itertools


def ivan():
    alphabet = "ABCDE"

    c = 0
    for w in itertools.product(alphabet, repeat=5):
        if w[0] != "E" and w[-1] != "A":
            c += 1

    print(c)

def bin_numbers():
    a = bin((4 ** 511) + (2 ** 511) - 511)
    print(a[2:].count('1'))

if __name__ == "__main__":
    ivan()
    bin_numbers()