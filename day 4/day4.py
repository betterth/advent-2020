#day 4 passport scanning

def main():
    input = handle_input('input.txt')
    passport_lines = []
    passport_list = []
    for line in input:
        if line == '':
            passport_list.append(build_passport(passport_lines))
            passport_lines = []
        else:
            passport_lines.append(line)
        

def build_passport(lines):
    print(" ".join(lines))

def handle_input(file):
    input_list = []
    # Read input
    with open(file, 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list

if __name__ == "__main__":
    main()