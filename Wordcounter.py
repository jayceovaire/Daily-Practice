loost = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
         'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'p': 0, 'r': 0,
         's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
         }
woords = {}
liost = []

text = input("Enter your text here: ")
text = text.lower()
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('"', '')
text = text.replace("'", '')
text = text.replace('!', '')
text = text.replace('?', '')
stest = text.split()
wcount = 0
lcount = 0

for w in stest:
    wcount += 1
for c in text:
    if c == " ":
        continue
    elif c == ",":
        continue
    else:
        lcount += 1
for c in text:
    if c in loost:
        loost[c] += 1
for w in stest:
    woords[w] = 0
for w in stest:
    if w in woords:
        woords[w] += 1
print(woords)
print(loost)
print(f"there are {wcount} words and {lcount} letters")
print(text)