import functools

numbers = [1,2,3,4]

result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)

print('/'*100)

def accum(counter,item):
    print('counter: ', counter)
    print('item: ', item)
    return counter + item 

solution= functools.reduce(accum, numbers)
print(solution)