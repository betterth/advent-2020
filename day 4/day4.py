#day 4 passport scanning

def main():
    valid_passports = 0
    total = 0
    passport_lines = []
    passport_list = []
    #collect multi-line input into passport groups
    input = handle_input('input.txt')
    for line in input:
        if line == '':
            passport_list.append(" ".join(passport_lines).split(" "))
            passport_lines = []
        else:
            passport_lines.append(line)
    #process passport list
    for passport in passport_list:
        total += 1
        passport_dict = {}
        #build and test a dictionary of each passport
        for value in passport:
            value = value.split(":")
            passport_dict[value[0]] = value[1]
        if passport_is_valid(passport_dict) == True:
            valid_passports += 1
            print("valid:",len(passport_dict),passport_dict)
        else:  
            print("INVALID:",len(passport_dict),passport_dict)
    print(valid_passports,total)

def passport_is_valid(passport):
    if "byr" not in passport:
        return False    
    elif "iyr" not in passport:
        return False    
    elif "eyr" not in passport:
        return False        
    elif "hgt" not in passport:
        return False    
    elif "hcl" not in passport:
        return False    
    elif "ecl" not in passport:
        return False    
    elif "pid" not in passport:
        return False   
    else:
        return True     

def handle_input(file):
    input_list = []
    with open(file, 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list

if __name__ == "__main__":
    main()