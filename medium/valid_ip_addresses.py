def isValidPart(part):
    if not part:
        return False
    part_len = len(part)
    if part_len > 3:
        return False
    if part_len > 1 and part[0] == '0':
        return False
    if int(part) > 255:
        return False
    return True 

def validIPAddresses(string, ip_parts=4):
    strings = []
    if ip_parts == 1:
        if isValidPart(string):
            strings.append(string)
        return strings
    for i in range(3):
        first_part = string[:i+1]
        if isValidPart(first_part):
            for sub_ip in validIPAddresses(string[i+1:], ip_parts=ip_parts - 1):
                strings.append(first_part + '.' + sub_ip)
    return strings
