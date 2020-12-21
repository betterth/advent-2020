#day 4 passport scanning

def main():
    passport = {"byr":"1980"}
    byr = int(passport.get("byr"))
    if not 2020 >= byr >= 1920:
        print("FALSE")
    else:
        print("TRUE")

if __name__ == "__main__":
    main()