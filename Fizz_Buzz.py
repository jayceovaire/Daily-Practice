#Fizzbuzz problem
# make a list of 1 to 100 and for every number divisible by 3 print fizz
# every number divisible by 5 print buzz
# every number divisible by 3 and 5 print fizzbuzz
#list every other number

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + ' fizzbuzz')
    elif i% 3 == 0:
        print(str(i) + ' fizz')
    elif i% 5 == 0:
        print(str(i) + ' buzz')
    else:
        print(str(i))

#Shorter list comprehension version

for i in range(1,101):
    fizz = 'Fizz' if i % 3 == 0 else ''
    buzz = 'Buzz' if i % 5 == 0 else ''
    print(f"{fizz}{buzz}" or i)


# Separated lists / longer "code-y" version
number =[]
fizz = []
buzz = []
fizzbuzz = []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz.append(i)

    if i % 3 == 0:
        fizz.append(i)

    if i % 5 == 0:
        buzz.append(i)
    if i % 3 !=0 and i % 5 !=0:
        number.append(i)

for i in fizz:
    if i % 5 == 0:
        fizz.remove(i)


for i in buzz:
    if i % 3 == 0:
        buzz.remove(i)


print(f"Fizz: \n {fizz}")
print(f"Buzz: \n {buzz}")
print(f"FizzBuzz: \n {fizzbuzz}")
print(f"Other Numbers: \n {number}")
