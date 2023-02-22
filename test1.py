input_str = input("Enter the message: ")
shift_val = int(input("Enter the shift number (1-25, inclusive): "))

def input_str_check(input_strr):
    for char in input_strr:
        if char.isalnum() == False:
            if char == " ":
                continue
            else:
                print("Please restrict your message to characters, numbers, and spaces.")
                break
    else:
        return True

def shift_val_check(shift_vall):
    if shift_vall not in range(0,26):
        print("Please enter a number that is between 1 and 25, inclusive.")
        return False
    else:
        return True

def convert():
    converted_list = []
    for char in input_str:
        current_ord = ord(char)
        if current_ord == 32:
            converted_list.append(" ")
        else:
            if current_ord in range(97,123):
                if 122 - current_ord < shift_val:
                    converted_list.append(chr(shift_val - ((122 - current_ord)) + 96))
                else:
                    converted_list.append(chr(shift_val + current_ord))
            elif current_ord in range(65,90):
                if 90 - current_ord < shift_val:
                    converted_list.append(chr(shift_val - ((90 - current_ord)) + 64))
                else:
                    converted_list.append(chr(shift_val + current_ord))
            elif current_ord in range(48,58):
                converted_list.append(char)
            else:
                break
    return converted_list

def combine():
    final = "".join(convert())
    return final

if input_str_check(input_str) and shift_val_check(shift_val) == True:
    convert()
    print(combine())
else:
    None

