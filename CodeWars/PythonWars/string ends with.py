# Write a function that takes in 2 strings and returns a True
# if string 1 ends with string 2.


def solution(text: str, ending: str) -> bool:
    endlength = len(ending)
    if text[-endlength::] == ending:
        return True
    else:
        return False
