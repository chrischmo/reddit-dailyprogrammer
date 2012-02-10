def guess_num(range, counter = 1):
    """Tries to guess a number in a range given as an array by narrowing down the range recursively"""
    candidate = (range[0] + range[1]) / 2   #gets median of current range
    print range
    answer = raw_input("Is it {0}? Answer 'h' for 'higher', 'l' for 'lower', 'r' for 'right': ".format(candidate))
    if answer == "h": guess_num([candidate + 1, range[1]], counter + 1)   #restricts range to higher numbers
    elif answer == "l": guess_num([range[0], candidate - 1], counter + 1)   #restricts range to lower numbers
    elif answer == "r": print "HAH! And it took me only {0} guesses!".format(counter)
    else: guess_num(range, counter)   #catches invalid input

num = raw_input("Please enter a whole number between 1 and 100 and I'll try to guess it: ")
guess_num([1, 100])
