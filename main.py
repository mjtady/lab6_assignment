# This code belongs to Maria Juliana Tady
def encode(user_pass):
    # the encoder stores the encoded password to a new
    # variable, with each digit being shifted up by 3 numbers.
    encoded_list = []
    for i in range(0, len(user_pass)):
        encoded_list.append(str(int(user_pass[i])+3)[-1])
    new_pass = ''.join(encoded_list)
    return new_pass


def main():
    print('Menu')
    print("-" * 8)
    user_input = input("\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
    while True:
        if user_input == "1":
            user_pass = input("Please enter your password to encode: ")
            encode_pass = encode(user_pass)
            print(encode_pass)
            print("Your password has been encoded and stored!")
        elif user_input == "2":
            decode_pass = decode(encode_pass)
            print(f"The encoded password is {encode_pass}, and the original password is {decode_pass}.")
        elif user_input == "3":
            quit()
        else:
            return -1


if __name__ == "__main__":
    main()
