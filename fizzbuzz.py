def fizzbuzz(num):
    if(num % 3 == 0 and num % 5):
       print("Fizzbuzz")
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print(num)        





nums = [5,6,10,15,20,26,32,40,46,52,57,60,66,75,84,90]   
for num in nums:
    fizzbuzz(num)

