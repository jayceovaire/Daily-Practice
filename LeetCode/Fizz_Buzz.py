#Fizzbuzz problem
# make a list of 1 to 100 and for every number divisible by 3 print fizz
# every number divisible by 5 print buzz
# every number divisible by 3 and 5 print fizzbuzz
#list every other number


def fizzbuzz():
    fizz_hash = {
        3: 'Fizz',
        5: 'Buzz',
        7: 'Bazz',
    }
    for i in range(1, 101):
        output = ''
        for j in fizz_hash:
            if i % j == 0:
                output += fizz_hash[j]
        if output == '':
            output = i
        print(output)

def fizzbuzz2():
    for i in range(1, 101):
        output = ''
        if i % 3 == 0: output += 'Fizz'
        if i % 5 == 0: output += 'Buzz'
        if i % 7 == 0: output += 'Bazz'
        if output == '': output = i
        print(output)

fizzbuzz2()