#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(raw_input):
    x = raw_input[::-1]
    return x == raw_input


#YOUR CODE GOES HERE

raw_input = input()
print(palindrome(raw_input))