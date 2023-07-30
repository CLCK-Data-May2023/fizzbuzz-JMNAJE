
for num in range(1, 101):
                            #In the range, I used 101 instead of 101 because 100 stopped at 99. 
    
    if num % 3 == 0 and num % 5 == 0:
                            #used the "%" instead of the "/", because I did not want a float number    
        print("FizzBuzz")
    
    elif num % 3 == 0:      # "Else if" allows to chain of multiple conditions together, which allows code to be executed when its condition is true
        print("Fizz")
    
    elif num % 5 == 0:
        print("Buzz")
    
    else:
        print(num)   

