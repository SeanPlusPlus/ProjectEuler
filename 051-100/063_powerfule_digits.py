# The 5-digit number, 16807=7^5, is also a fifth power. Similarly,
# the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?


def main():
    power = 5
    p = 7 ** power
    print p, len(str(p)) == power

if __name__ == '__main__':
    main()
    
