def generator_function():
    print('before yield')          #yield make it a generator
    yield 10
    print('before second yield')
    yield 20

gen = generator_function() #save generator object in variable

print(next(gen))
print(next(gen))

for value in generator_function():  #use for loop
    print(value)