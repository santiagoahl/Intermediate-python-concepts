def divisors(num):
    divisors = []
    assert num > 0, 'No negative numbers admited'
    for i in range(1,num):
        if num % i == 0:
            divisors.append(i)
    return divisors
            
    
def main():
    num = str(input('Put a positive integer: ')) #What if the user doesn't put a number?
    assert float(num).is_integer(), 'You have to put a number'
    print(divisors(int(num)))
    
if __name__=='__main__':
    main()