# it generates the value with the help of yield, instead of return

def generator_function(num):
    for x in range(2,num,2):
        yield x
    
even_gen = (generator_function(12))

for i in even_gen:
    print(i)

