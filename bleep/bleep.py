import sys

# Ensure proper usage
if len(sys.argv) != 2:
    sys.exit("Usage: python bleep.py WORDS")

# Prompt user for message
message = input("What message would you like to censor?\n")

# Censor message
print(message)
