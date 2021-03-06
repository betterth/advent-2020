#day 3 both parts 
# calculating slope / tree hits

def main():
    input = handle_input('input.txt')
    slope_list = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    answer = 1
    for slope in slope_list:
        x = slope[0]
        y = slope[1]
        iteration_result = check_problem(input,x,y)
        print(slope,iteration_result)
        answer *= iteration_result
    print(answer)

def check_problem(map,slope_x,slope_y):
    hits = 0
    x_pos = 0
    x_max = len(map[0])
    for index, line in enumerate(map):
        #move y position more maybe
        if index % slope_y != 0:
            continue
        #check for hits
        if line[x_pos] == "#":
            hits += 1
        #move x position
        x_pos = x_pos + slope_x % x_max
    return hits

def handle_input(file):
    input_list = []
    # Read input
    with open(file, 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list
    
if __name__ == "__main__":
    main()