def square_root(k):
    epsilon = 0.01
    guess = k/2
    while abs(guess*guess - k) >= epsilon:
        guess = guess - (guess*guess - k)/(2*guess)
    return guess

def factorial(number):
    if number == 0: 
        return 1
    return number*factorial(number-1)

def calc(calculate_method_func, number):
    return calculate_method_func(number)

def sum(condi,array):
    sum = 0
    step = 0
    for num in array:
        if condi(num):
            sum += num
            step += 1
    return sum,step

print(sum(lambda x: x,[1,2,3,4,5] ))
