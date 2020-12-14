#day 2 pt2- password validation again

#slope = right3 down1
def main():
    #get iterable of input
    answer = 0
    x_max = 30 #0bound
    #discard first line, set x position to 3 (0 bound)
    x_pos = 3
    input = handle_input('input.txt')[1:] #list slicing to remove the first entry
    #print(len(input[0]))
    hits = 0
    #
    for index, line in enumerate(input):
        if line[x_pos] == "#":
            hits += 1
            print("Hit at ",x_pos,",",index+2," ",hits)
        x_pos += 3    
        if x_pos >= x_max:
            x_pos -= x_max
    print(hits)

def handle_input(file):
    input_list = []
    # Read input
    with open(file, 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list
    
if __name__ == "__main__":
    main()