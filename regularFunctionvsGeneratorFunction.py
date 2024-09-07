def regular_function():
    print('inside regular function')
    return 10
regular_function()  #call the function

def generator_function():
    print('before yield')            #yield makes it a generator
    yield 10
generator_function()
print('change\n print' *2)
def regular_function():
    print('inside regular function')
    return 10
print(regular_function())  #call the function

def generator_function():
    print('before yield')            #yield makes it a generator
    yield 10
print(generator_function())
print(next(generator_function()))