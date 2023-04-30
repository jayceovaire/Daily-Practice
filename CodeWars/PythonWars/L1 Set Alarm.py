# Write a function that returns True if you need to set an alarm clock. You need to set an alarm
# if you are employed and not on vacation.

def set_alarm(employed, vacation):
    if employed and not vacation:
        return True
    else:
        return False
