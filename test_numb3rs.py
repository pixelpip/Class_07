from numb3rs import validate

def test_valid():
    assert validate("192.168.0.1") == True

def test_invalid_octet():
    assert validate("192.168.0.300") == False

def test_invalid_ip_address():
    assert validate("192.168.0") == False




def main():
    test_valid()
    test_invalid_octet()
    test_invalid_ip_address()


if __name__ == "__main__":
    main()




 

