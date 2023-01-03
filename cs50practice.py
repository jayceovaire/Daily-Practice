from string import Template
s = Template("$greeting, $user!")

print(s.substitute(greeting="Hi", user="Josh"))

greeting = "Hello"
name = "Josh"
message = "".join((greeting, ", ", name, "!"))
print(message)
print(f"{greeting + ', ' + name + '!'}")

class Special:
    TODAY = 'lasagna'

lunch_order = input("what do you want for lunch?")

match lunch_order:
    case 'salad' | 'soup':
        print('eating healthy, good for you!')
    case ice_cream if 'ice cream' in ice_cream:
        flavor = ice_cream.replace('ice cream', '').strip()
        print(f"Here's your very grown up {flavor}...lunch")
    case order:
        print(f"Enjoy your {order}")
print(lunch_order)