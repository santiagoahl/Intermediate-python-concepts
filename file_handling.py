def read():
    read_numbers = []
    path = './my_files/numbers.txt'
    with open(path,'r', encoding = 'utf-8') as f:       #r means read, encoding is a top argument
        for line in f:
            read_numbers.append(int(line))
    print(read_numbers)


def write():
    names = ['Tony', 'Chris', 'Banners', 'Scarlett', 'Rocío']
    path = './my_files/names.txt'
    with open(path, 'w', encoding = 'utf-8') as f:
        for name in names:
            f.write(name)         #f means the link between python an our file
            f.write('\n')

def main():
    write()

if __name__ == '__main__':
    main()