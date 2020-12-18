#day 4 passport scanning

def main():
    valid_passports = 0
    total = 0
    passport_lines = []
    passport_list = []
    #collect multi-line input into passport groups
    input = handle_input('input.txt')
    #issue: doesn't process last element because last line isn't blank
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
    #byr
    byr = passport.get("byr")
    if not byr: return False
    if not 2002 >= int(byr) >= 1920: return False
    #iyr
    iyr = passport.get("iyr")
    if not iyr: return False
    if not 2020 >= int(iyr) >= 2010: return False
    #
    eyr = passport.get("eyr")
    if not eyr: return False
    if not 2030 >= int(eyr) >= 2020: return False
    #   
    hgt = passport.get("hgt")
    if not hgt: return False
    if hgt.find("cm"):
        if not 193 >= int(hgt.replace("cm","")) >= 150: return False
    elif hgt.find("in"):
        if not 76 >= int(hgt.replace("in","")) >= 59: return False
    #
    if "hcl" not in passport:
        return False    
    if "ecl" not in passport:
        return False    
    if "pid" not in passport:
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