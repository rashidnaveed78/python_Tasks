def fizz_buzz(n):

    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("Fizzbuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("buzz")
    else:
        print(i)

number=int(input("Enter your number: "))
fizz_buzz (number)

    