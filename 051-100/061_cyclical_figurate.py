from figurate import Figurate

def main():
    f = Figurate()
    threshold = 6
    shapes = [
        'triangle',
        'square',
        'pentagonal',
        'hexagonal',
        'heptagonal',
        'octoganol'
    ]
    for shape in shapes:
        for n in range(1, threshold):
            print shape, getattr(f, shape)(n)




if __name__ == '__main__':
    main()
    
