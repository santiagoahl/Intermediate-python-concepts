from math import sqrt

def main():
    square_root_dict = {k:sqrt(k) for k in range(100)}
    print(square_root_dict)
    
if __name__ == '__main__':
    main()