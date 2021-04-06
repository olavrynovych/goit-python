def calculate_fibonacci(number):
    
    if number == 0:
        return 0
    if number in (1, 2):
        return 1
    return calculate_fibonacci(number - 1) + calculate_fibonacci(number - 2)


def main():
    
    n = 0
    n = int(input('Enter number:'))
    result = calculate_fibonacci(n)
    print(f'Fibonacci result is: {result}')

    if __name__ == '__main__':
        main()





##    if number == 1:
##        return 1
##    if number == 0:
##        return 0
##    else:
##         return calculate_fibonacci(number-1) + calculate_fibonacci(number-2)


    
