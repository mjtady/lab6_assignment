# This code belongs to Maria Juliana Tady
def encode(user_pass):
    encoded_list = []
    for i in range(0, len(user_pass)):
        encoded_list.append(str(int(user_pass[i] + 3)[-1]))
    return encoded_list


def main():
    print('Menu')
    print("-" * 8)
    user_input = input("\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option")
    while user_input != "3":
        global encode_pass
        if user_input == "1":
            user_pass = input("Please enter your password to encode: ")
            encode_pass = encode(user_pass)
            print("Your password has been encoded and stored!")
        elif user_input == "2":
            pass
        elif user_input == "3":
            continue
        else:
            return -1


if __name__ == "__main__":
    main()
