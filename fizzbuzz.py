def getFizzBuzz(multiples, *args):
    for i in range(*args):
        output = ""
        for multiple in multiples:
            if i % multiple==0:
                output+=multiples[multiple]
        if output =="":
            output = i
        print(output)            

multiples = {3:'Fizz', 5:'Buzz'}
getFizzBuzz(multiples,101)

multiples = [5,6,10,15,20,26,32,40,46,52,57,60,66,75,84,90]   
for multiple in multiples:
    print(multiple)

