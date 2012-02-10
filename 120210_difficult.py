def guess_num(range, guesses):
    candidate = range[0] + (range[1] - range[0]) / 2
    answer = raw_input("Is it " + str(candidate) + "? - 'h' for higher 'l', for lower, 'r' for right: ")
    if answer == "h": guess_num([candidate + 1, range[1]], guesses + 1)
    elif answer == "l": guess_num([range[0], candidate - 1], guesses + 1)
    elif answer == "r": print "YEAH! Needed " + str(guesses) + " guesses."
    else: print "Invalid answer, let's try again: \n" + guess_num(range, guesses)

num = raw_input("Please enter a whole number between 1 and 100: ")
guess_num([1, 100], 1)
