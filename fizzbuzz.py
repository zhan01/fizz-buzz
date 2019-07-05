print("FizzBuzz in range of 10:\n")
n = 10

def fizzbuzz(n):
    for i in range(n):
        
        if i % 3 == 0 and i % 2 == 0:
            print('FizzBuzz')
        elif i % 2 == 0:
            print('Fizz')
        elif i % 3 == 0:
            print('Buzz')
        else:
            print(i)

print(fizzbuzz(n))