import re

pattern = re.compile(r"(\w{3}):(\S+)")

# rules
byr = re.compile(r"(\d{4})$")  # 1920, 2002
iyr = re.compile(r"(\d{4})$")  # 2010, 2020
eyr = re.compile(r"(\d{4})$")  # 2020, 2030
hgt = re.compile(r"(\d+)(in|cm)$")  # cm: 150, 193. in: 59, 76
hcl = re.compile(r"#([0-9a-f]{6})$")
ecl = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)$")
pid = re.compile(r"(\d{9})$")

required_keys = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
rules_dict = {
    "byr": byr,
    "iyr": iyr,
    "eyr": eyr,
    "hgt": hgt,
    "hcl": hcl,
    "ecl": ecl,
    "pid": pid,
}
ranges_dict = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "hgt": ((150, 193), (59, 76)),
}

with open("input/in4.txt") as f:
    num_valid = 0
    num_found_keys = 0
    invalid = False

    for line in f:
        if line == "\n":
            if invalid is False and num_found_keys == len(required_keys):
                num_valid += 1
            num_found_keys = 0
            invalid = False

        elif invalid is True:
            continue

        else:
            for key, value in pattern.findall(line):
                if key in required_keys:
                    rule = rules_dict.get(key)
                    if rule.match(value):
                        if ranges_dict.get(key) is not None:
                            low, high = ranges_dict[key]
                            if not isinstance(low, int):
                                unit = value[-2:]
                                if unit == "cm":
                                    low, high = low
                                else:
                                    low, high = high
                                value = value[:-2]

                            if low <= int(value) <= high:
                                num_found_keys += 1
                            else:
                                invalid = True
                                break
                        else:
                            num_found_keys += 1
                    else:
                        invalid = True
                        break

    if num_found_keys == len(required_keys):
        num_valid += 1


print(num_valid)
