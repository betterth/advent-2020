#day 4 passport scanning

def main():
    valid_passports = 0
    total = 0
    passport_lines = []
    passport_list = []
    #collect multi-line input into passport groups
    input = handle_input('day 4/input.txt')
    #issue: doesn't process last element because last line isn't blank
    for line in input:
        if not line == '':
            passport_lines.append(line)
        else:
            passport_list.append(" ".join(passport_lines).split(" "))
            passport_lines = []
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
    if not is_int(byr): return False
    if not 2002 >= int(byr) >= 1920: return False
    #iyr
    iyr = passport.get("iyr")
    if not iyr: return False
    if not is_int(iyr): return False
    if not 2020 >= int(iyr) >= 2010: return False
    #
    eyr = passport.get("eyr")
    if not eyr: return False
    if not is_int(eyr): return False
    if not 2030 >= int(eyr) >= 2020: return False
    #   
    hgt = passport.get("hgt")
    if not hgt: return False
    if hgt.find("cm") != -1:
        if not 193 >= int(hgt.replace("cm","")) >= 150: return False
    elif hgt.find("in") != -1:
        if not 76 >= int(hgt.replace("in","")) >= 59: return False
    else: return False
    #
    hcl = passport.get("hcl")
    if not hcl: return False
    if not hcl[0] == "#": return False
    if not len(hcl[1:]) == 6: return False
    if not is_int(hcl[1:],16): return False
    #
    ecl = passport.get("ecl")
    if not ecl in ("amb","blu","brn","gry","grn","hzl","oth"): return False
    #
    pid = passport.get("pid")
    if not pid: return False
    if not pid.isnumeric(): return False
    if not len(pid) == 9: return False
    # 
    else:
        return True     

def is_int(num,base=10):
    try:
        int(num,base)
        return True
    except ValueError:
        return False

def handle_input(file):
    input_list = []
    with open(file, 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(line.rstrip())
    return input_list

if __name__ == "__main__":
    main()