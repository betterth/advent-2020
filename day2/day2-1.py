#day 2 pt1- password validation

def main():
    #get iterable of input
    answer = 0
    input = handle_input()
    for line in input:
        if is_pass_valid(line):
            answer += 1
    print("Valid: ",answer)

def handle_input():
    input_list = []
    # Read input
    with open('input.txt', 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list

def is_pass_valid(pass_string):
    splitstring = pass_string.split(":")
    range = splitstring[0].split(" ")[0]
    range_low = int(range.split("-")[0])
    range_high = int(range.split("-")[1])
    requirement = splitstring[0].split(" ")[1]
    password = splitstring[1].lstrip()
    occurence = password.count(requirement)
    if range_low <= occurence <= range_high:
        return True

if __name__ == "__main__":
    main()