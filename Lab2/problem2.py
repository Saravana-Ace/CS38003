def main():
    key_value, encrypted_value = encrypt(12345, "zuri")

    print("This is key_value: ", key_value, "This is encrypted_value: ", encrypted_value)

def encrypt(n, txt):
    digits_str = str(n)
    digit_ascii_sum = 0
    digit_sum = 0
    remainder = 0
    ascii_val = 0

    for i in range(len(digits_str)):
        digit_ascii_sum += ord(digits_str[i])
        digit_sum += int(digits_str[i])

    remainder = digit_ascii_sum % digit_sum

    key = 50 + remainder

    encrypted = ""
    for i in range(len(txt)):
        ascii_val = ord(txt[i])
        encrypted += chr((ascii_val + key) % 128)

    return key, encrypted

if __name__ == '__main__':
    main()
