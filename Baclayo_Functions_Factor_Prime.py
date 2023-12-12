print('Smallest Factor of n and Prime Numbers of Range Using Functions')
print('Myka Angelie Baclayo\n')

def smallestfact():
    while True:
        num_int = int(input('Enter a number greater or equal to 2: '))
        if num_int < 2:
             print('Invalid number. Please enter a number greater or equal to 2')
             continue

        smallest = None
        for i in range(2, int(num_int**0.5) + 1):
             if num_int % i == 0:
                 smallest = i
                 break
        if smallest:
            print(f'The smallest factor of {num_int} is {smallest}')
        else:
             print(f'{num_int} is a prime number. Its smallest factor is itself.')
        break


def praym(num):
    if num == 2:
        return True
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    choice = int(input('\n[1] Smallest Factor [2] Prime Numbers: '))
    if choice == 1:
        smallestfact()
    elif choice == 2:
        start = int(input('Enter a number [start]: '))
        if start == 0:
            print('Program Terminated.')
            break
        if start < 0:
            print('Enter a non-negative number.')
            continue

        end = int(input('Enter a number [end]: '))
        if end <= start:
            print(f'Enter a number greater than {start}.')
            continue

        print(f'Prime numbers between {start} and {end} are: ')
        for number in range(start, end + 1):
            if praym(number):
                print(number, end=", ")
                
    else:
        print('Invalid choice.')
