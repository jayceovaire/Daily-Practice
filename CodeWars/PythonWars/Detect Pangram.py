def is_pangram(s: str) -> bool:
    chars = set()
    for char in s:
        if char.isalpha():
            chars.add(char.lower())

    return len(chars) == 26


def is_pangram(s: str) -> bool:
    chars = {}
    for char in s:
        if char.isalpha():
            if char not in chars:
                chars[char] = 1

    return len(chars) == 26


