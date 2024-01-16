number = int(input("Enter a number: "))
def prime_num(number):

    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number") 
    else:
        print("It is not a prime number")       

    # if number % number == 0 and number % 1 == 0:
    #     print("It is a prime number")
    # else:
    #     print("It is not a prime number")    

prime_num()        