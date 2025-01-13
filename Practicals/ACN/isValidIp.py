def isValidIp(ip):
    temp = ip
    try:
        if hasValidSeparator(ip):
            ip = ip.split(".")
        
            if isValidLen(ip):
                for cell in ip:
                    if hasOnlyInteger(cell):
                        if hasLeadingZeroes(cell):
                            if isValidRange(cell):
                                continue
                        else:
                            return False
        return True
    except Exception as e:
        print(e)
        return False

def isValidLen(ip):
    if len(ip) == 4:
        return True
    raise Exception("IPv4 should have 4 cells.")

def isValidRange(cell):
    if 0 <= int(cell) <= 255:
        return True
    raise Exception("Each cell should have values between 0 and 255.")

def hasLeadingZeroes(cell):
    if len(cell) > 1 and cell[0] == '0':
        raise Exception("Cells should not have any leading zeroes.")
    return True

def hasOnlyInteger(cell):
    if not cell.isdigit():
        raise Exception('The IP address should only contain integers.')
    return True

def hasValidSeparator(ip):
    allowed = set("0123456789.")
    if not all(char in allowed for char in ip):
        raise Exception("IP address contains invalid separators.")
    return True


IP = input("Enter the IP to check  :  ")
print(isValidIp(IP))
