def guess_num(range, guesses = 1):
    """Tries to guess a number in a range given as an array by narrowing down the range recursively"""
    candidate = range[0] + (range[1] - range[0]) / 2
    answer = raw_input("Is it " + str(candidate) + "? Answer 'h' for 'higher', 'l' for 'lower', 'r' for 'right': ")
    if answer == "h": guess_num([candidate + 1, range[1]], guesses + 1)
    elif answer == "l": guess_num([range[0], candidate - 1], guesses + 1)
    elif answer == "r": print "HA! And it took me only " + str(guesses) + " guesses!"
    else: guess_num(range, guesses)

num = raw_input("Please enter a whole number between 1 and 100 and I'll try to guess it: ")
guess_num([1, 100])
