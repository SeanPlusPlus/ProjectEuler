from figurate import Figurate

def main():
    f = Figurate()
    threshold = 6
    print [f.triangle(n) for n in range(1,threshold)]
    print [f.square(n) for n in range(1,threshold)]
    print [f.pentagonal(n) for n in range(1,threshold)]
    print [f.hexagonal(n) for n in range(1,threshold)]
    print [f.heptagonal(n) for n in range(1,threshold)]
    print [f.octoganol(n) for n in range(1,threshold)]


if __name__ == '__main__':
    main()
    
