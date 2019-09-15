# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling
# We are in trouble if they are both smiling or it neither of them is smiling
# Return True if we are in trouble
# monkey_trouble(True, True) -> True
# monkey_trouble(False, False) -> True
# monkey_trouble(True, False) -> False

def monkey_trouble(a_smile, b_smile):
        if a_smile and b_smile:
            return True
            print("We are in trouble")
        if not a_smile and not b_smile:
            return True
            print("We are in trouble")
        return False
        print("We are not in trouble")
