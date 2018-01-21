def print_funny():
    print("Something funny")
    print("Something even funnier")
    print("The funniest thing")

print_funny()

def advanced_printing_basics(time, text):
    for volume in range(0, time):
        print(str(text))

advanced_printing_basics(5, "It's alive!")


def print_multiple_funny(time):
    for volume in range(0, time):
        print_funny()

print_multiple_funny(7)

#that is all