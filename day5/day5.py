#day 4 passport scanning

def main():
    input = handle_input('day5/small.txt')
    for line in input:
        # row 0 - 127 //
        for x in range(0,6):
            row_upper = 127
            row_lower = 0
            factor = 64
            if line[x] == "F":
                if factor > 1:
                    row_upper -= factor
                else:
                    print("row:",row_upper)
            if line[x] == "B":
                if factor > 1:
                    row_lower += factor
                else:
                    print("row:",row_lower)
            factor /= 2
        print(' ')

def handle_input(file):
    input_list = []
    with open(file, 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list

if __name__ == "__main__":
    main()