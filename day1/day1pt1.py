# day 1 part 1

def main():
    input_list = []
    # Read input
    with open('input1.txt', 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(int(line.rstrip()))
    # Process data list and determine match, assuming only 1 or first match
    for first_value in input_list:
        inner_list = input_list
        inner_list.remove(first_value)
        for second_value in inner_list:
            if first_value+second_value == 2020:
                break
        if first_value+second_value == 2020:
            break
    # Print answer
    if first_value&second_value:
        print("Found: ",first_value," and ",second_value)
        answer = first_value * second_value
        print("Answer: ",answer)
    else:
        print("No values found")

if __name__ == "__main__":
    main()