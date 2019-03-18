STARTING_NUMBER_ERROR = "Please enter a 0 or 1!"


def fibonacci(starting_number, sequence_length=10):
    if starting_number == 0:
        a, b = 0, 1
    elif starting_number == 1:
        a, b = 1, 1
    else:
        print(STARTING_NUMBER_ERROR)
        return

    sequence = str(starting_number)
    for i in range(sequence_length - 1):
        sequence = sequence + " {}".format(b)
        a, b = b, a + b
    print(sequence)


#### DO NOT ADJUST THE TEST PARAMETERS BELOW
#### THE CONSOLE OUTPUT SHOULD MATCH THIS:
#     Please enter a 0 or 1!
#     0 1 1 2 3
#     1 1 2 3 5
#     1 1 2 3 5 8 13 21 34 55
fibonacci(2, 5)
fibonacci(0, 5)
fibonacci(1, 5)
fibonacci(1)
