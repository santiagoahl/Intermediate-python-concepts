def divisors(num):
    #divisors = [i for i in range(1, num + 1) if num % i == 1]
    try:
        if type(num) == int and num <0:
            raise ValueError('No negative numbers admited')
        divisors = []
        for i in range(1,num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False
            
    
def main():
    try:
        num = int(input('Put a positive integer: ')) #What if the user doesn't put a number?
        print(divisors(num))
    except ValueError:
        print('You must put only int numbers')
    print('Programm ended')
if __name__=='__main__':
    main()