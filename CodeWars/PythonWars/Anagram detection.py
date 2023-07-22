
# Given two strings return True if they are anagrams of each other,
# if they are not return False

def is_anagram(test: str, original: str) -> bool:
    testList = list(test.lower())
    originalList = list(original.lower())

    testList.sort()
    originalList.sort()

    if testList == originalList:
        return True
    else:
        return False
    

print(is_anagram('woot', 'toow'))
