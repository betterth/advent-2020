#day 2 pt2- password validation again

def main():
    #get iterable of input
    answer = 0
    input = handle_input('input.txt')
    for line in input:
        if is_pass_valid(line) == 1:
            answer += 1
    print("Valid: ",answer)

def handle_input(file):
    input_list = []
    # Read input
    with open(file, 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list

def is_pass_valid(pass_string):
    #pass_string e.g. "4-5 m: mpmmmm"
    position_string = pass_string.split(":")[0].split(" ")[0]
    #Their positions are not zero bound, so reduce by 1
    position_one = int(position_string.split("-")[0])-1
    position_two = int(position_string.split("-")[1])-1
    requirement = pass_string.split(":")[0].split(" ")[1]
    password = pass_string.split(":")[1].lstrip()
    answer = 0
    if password[position_one] == requirement:
        answer += 1
    if password[position_two] == requirement:
        answer += 1
    print(position_string,requirement,position_one,position_two,password,answer)
    return answer
    
if __name__ == "__main__":
    main()