import re
import sys

def validate(ip):
    matches = re.search(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip)

    if matches:
        for group in matches.groups():
            octet = int(group)
            print (f"octet =  {octet}")
            if octet < 0 or octet > 255:
                print(f"Not a valid IP address: {ip}")
                return False

        print(f"Valid IP address: {ip}")
        return True

    else:
        print(f"Not a valid IP address: {ip}")
        return False

def main():
    ip = input("IPv4 Address: ")
    validate(ip)

if __name__ == "__main__":
    main()
