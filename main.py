#Morse-Code-Converter(String to Morse-Code)
import os

# -------------------- LOGO -------------------- #

print('''
88                                88
88                                88
88,dPPYba,  ,adPPYYba,  ,adPPYba, 88   ,d8  ,adPPYba, 8b,dPPYba,
88P'    "8a ""     `Y8 a8"     "" 88 ,a8"  a8P_____88 88P'   "Y8
88       88 ,adPPPPP88 8b         8888[    8PP""""""" 88
88       88 88,    ,88 "8a,   ,aa 88`"Yba, "8b,   ,aa 88
88       88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a `"Ybbd8"' 88
''')

# -------------------- MORSE CODE -------------------- #

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..','0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

print("\n Welcome to the 'Morse-Code-Converter!'")

resetting = input("\n To erase text type 'reset' otherwise type 'no': ")

encrypted_code = []

is_on = True # Run the while loop again

while is_on:
    text = input("\nType your 'SECRET' message here: ").upper() # Make all letters upper case

    for i in text:
        x = morse_code[i]
        encrypted_code.append(x) # Append code in list

    sorting = " ".join(encrypted_code) # This will remove the spacing between final encrypted code

    print(f"\nHere is your Encrypted Code: {sorting}") # This will print the final encrypted code

    is_go_again = input("\nType 'Yes' If you want to RUN the converter again otherwise Type 'No' ").title() # Make first letter capital

    def writingfile(): # Make new file and append it side by side
        with open("data_1.txt",mode="a") as data:
            data.write(f"{text.title()} :-  {sorting}\n")

    writingfile() # Calling function

    if resetting == "reset": # Erase previous entries
        os.remove("data_1.txt")
        writingfile()
    elif resetting == "no":
        pass

    if is_go_again == "Yes": # Run the converter again
        encrypted_code.clear()
        is_on
    elif is_go_again == "No":
        is_on = False
    else:
        print("\n plese type a valid option")
        is_on = False