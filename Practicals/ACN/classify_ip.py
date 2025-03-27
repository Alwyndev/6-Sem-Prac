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
    for i in ip.split("."):
        if not i.isdigit():
            raise Exception("IP Adress should contain only digits(0-9) and '.'!")
    if not all(char in allowed for char in ip):
        raise Exception("IP address contains invalid separators.")
    return True


def validateIpBlock(ip):
    try:
        temp = ip.split("/")
        temp_ip = ip[0]
        if len(temp) != 2:
            raise ValueError("Invalid input format. Expected format: IP/PrefixLength")
        
        temp_ip, n = temp[0], int(temp[1])
        temp_ip_bin = ""

        if isValidIp(temp_ip) and 0 <= n <= 32:
            print(f"Network ID (Bits): {n}")
            print(f"Host ID (Bits): {32 - n}")

            # Convert IP to binary
            temp_ip = temp_ip.split(".")
            for i in temp_ip:
                temp_ip_bin += format(int(i), '08b')
            
            subnet = temp_ip_bin
            print(subnet)


            # Calculate the first and last address
            network_bin = temp_ip_bin[:n] + ('0' * (32 - n))  # Network address
            broadcast_bin = temp_ip_bin[:n] + ('1' * (32 - n))  # Broadcast address

            print(f"Network Address (Binary): {network_bin}")
            print(f"Broadcast Address (Binary): {broadcast_bin}")

            # Convert binary to dotted-decimal format
            first_address = ".".join(str(int(network_bin[i:i+8], 2)) for i in range(0, 32, 8))
            last_address = ".".join(str(int(broadcast_bin[i:i+8], 2)) for i in range(0, 32, 8))

            print(f"First Address (Network Address): {first_address}")
            print(f"Last Address (Broadcast Address): {last_address}")

            subnet = subnet[:n] + ('0' * (32 - n))
            subnet = subnet[n:] + ('1' * (n))
            subnet = subnet[::-1]
            print(f"Subnet Mask: {int(subnet[:8],2)}.{int(subnet[8:16],2)}.{int(subnet[16:24],2)}.{int(subnet[24:],2)}")

            # Number of usable hosts
            usable_hosts = (2 ** (32 - n)) - 1 if n < 32 else 0
            print(f"Usable Hosts: {usable_hosts}")
        else:
            print("Invalid IP address or prefix length.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")


def classify(ip):
    # subnet_mask = ''
    temp = ip.split(".")
    try:
        if isValidIp(ip):

            if temp[0] <= "127":
                print("class A")
                print(f"Network ID: {temp[0]}")
                print(f"Host ID: {temp[1]}.{temp[2]}.{temp[3]}")
                print(f"Network Address: {temp[0]}.0.0.0")
                print(f"Host Address: 0.{temp[1]}.{temp[2]}.{temp[3]}")
                print(f"Default Subnet Mask: 255.0.0.0")
                
            elif temp[0] <= "191":
                print("class B")
                print(f"Network ID: {temp[0]}.{temp[1]}.0.0")
                print(f"Host ID: {temp[2]}.{temp[3]}")
                print(f"Network Address: {temp[0]}.{temp[1]}.0.0")
                print(f"Host Address: " + "0.0." + temp[2] + "." + temp[3])
                print(f"Default Subnet Mask: 255.255.0.0")
            elif temp[0] <= "223":
                print("class C")
                print(f"Network ID: {temp[0]}.{temp[1]}.{temp[2]}")
                print(f"Host ID: {temp[3]}")
                print(f"Network Address: {temp[0]}.{temp[1]}.{temp[2]}.0")
                print(f"Host Address: 0.0.0.{temp[3]}")
                print(f"Default Subnet Mask: 255.255.255.0")

            elif temp[0] <= "239":
                print("class D")
                print(f"Network ID: {temp[0]}.{temp[1]}.{temp[2]}")
                print(f"Host ID: {temp[3]}")
            else:
                print("class E")
                print(f"Network ID: N/A")
                print(f"Host ID: N/A")
    except Exception as e:
        print("Invalid IP Address",e)
        
# Classificatin on Binary

def classify_ip_bin(ip):
    try:
        ip = ip.split(".")
        octect = []

        for i in ip:
            cell = format(int(i),'08b')
            octect.append(cell)
        
        ip_bin = ".".join(octect)
        print(f"IP address in Binary Notation  : {ip_bin}")
        if octect[0].startswith('0'):
            print("Class A")
            print(f"Network ID: {octect[0]}")
            print(f"Host ID: {octect[1]}.{octect[2]}.{octect[3]}")
            print(f"Network Address: {octect[0]}.0.0.0")
            print(f"Host Address: 0.{octect[1]}.{octect[2]}.{octect[3]}")
            
        elif octect[0].startswith('10'):
            print("Class B")
            print(f"Network ID: {octect[0]}.{octect[1]}")
            print(f"Host ID: {octect[2]}.{octect[3]}")
            print(f"Network Address: {octect[0]}.{octect[1]}.0.0")
            print(f"Host Address: 0.0.{octect[2]}.{octect[3]}")
        elif octect[0].startswith('110'):
            print("Class C")
            print(f"Network ID: {octect[0]}.{octect[1]}.{octect[2]}")
            print(f"Host ID: {octect[3]}")
            print(f"Network Address: {octect[0]}.{octect[1]}.{octect[2]}.0")
            print(f"Host Address: 0.0.0.{octect[3]}")
        elif octect[0].startswith('1110'):
            print("Class D")
        elif octect[0].startswith('1111'):
            print("Class E")
        else:
            print("Invalid IP Address")
    except Exception as e:
        print("Invalid IP Address:", e)



if __name__ == "__main__":
    
    while (True):
        ch1 = int(input("""\n\nPress\tFor
  1  \t Classful
  2  \t Classless
  3  \t Exit
Your choice  :  """))
        if ch1 == 1:
            IP = input("Enter the IP adddress  :  ")
            if isValidIp(IP):
                classify(IP)
                classify_ip_bin(IP)
        
        elif ch1 == 2:
            ip_block = input("Enter the IP block (xxx.xxx.xxx.xxx/n) :  ")
            validateIpBlock(ip_block)
        else:
            break

