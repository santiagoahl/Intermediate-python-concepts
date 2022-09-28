def main():
    my_dict = {}
    for n in range(1,101):
        if n%3 != 0:
            my_dict[n]=n**3
    #print(my_dict)  
    #DICT COMPREHENSION
    comp_dict = {n:n^2 for n in range(1,101) if n % 3 != 0} 
    print(comp_dict)


if __name__ == '__main__':
    main()