# The parameter weekday is
# True if it is a weekday, and the parameter vacation is True if we are on Vacation
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in
# sleep_in(False, False) -> True
# sleep_in(True, False) -> False
# sleep_in(False, True) -> True

def sleep_in(weekday, vacation): # use colon instead of curly braces
    if not weekday or vacation:
        print("We are sleeping in")
        return True

    else:
        print("We are sleeping in")
        return False # indentation to close
