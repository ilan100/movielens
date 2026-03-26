import string
from pathlib import Path

letter_names = {"A": "ay", "B": "bee", "C": "see", "D": "dee", "E": "ee",
                "F": "ef", "G": "gee", "H": "aitch", "I": "eye", "J": "jay",
                "K": "kay", "L": "el", "M": "em", "N": "en", "O": "oh", "P":
                "pee", "Q": "cue", "R": "ar", "S": "ess", "T": "tee", "U": "you",
                "V": "vee", "W": "double-u", "X": "ex", "Y": "why", "Z": "zee"
}

""" EX1: writes letter names from A to Z in separate files """
def write_letters_to_files():
    for letter in string.ascii_uppercase:
        filename = "Letters/" + letter + ".txt" # write all files in a folder named "Letters" (under project)
        with open(filename, "w") as f:
            f.write(letter_names[letter] + "\n")

"""" EX2: read the first 20 lines of a file """
def read_lines_from_file(filename, number_of_lines : int):
    lines = []
    with open(filename, "r") as f:
        for i in range (0, number_of_lines):
            lines.append(f.readline())
    return lines

""" EX3 and EX4 are handled in a separate script (corona.py) """

""" EX5: merge all text files into one """
def merge_text_files(folder_name : str, new_file_name : str):
    folder = Path(folder_name)
    with open(folder_name + "/" + new_file_name, "w") as f_new:
        for file in folder.iterdir():
            if file.is_file():
                with open(file, "r") as f:
                    for line in f:
                        f_new.write(line)


""" Advanced - encoding caesar encryption """
class CaesarFile:
    def __init__(self, filename, shift):
        self.filename = filename
        self.shift = shift

    def __enter__(self):
        # Open the file
        self.f = open(self.filename, "r")
        # Read lines and decode each line
        self.decoded_lines = [
            self.caesar_decode(line.rstrip("\n")) for line in self.f
        ]
        return self.decoded_lines  # return a list of decoded lines

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()  # always close the file

    # Caesar decoding method
    def caesar_decode(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                result += chr((ord(char) - offset - self.shift) % 26 + offset)
            else:
                result += char
        return result


#----------------------------------------------------------------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_letters_to_files()

    lines = read_lines_from_file("A.txt", 20)
    for i in range (0, 20):
        print(lines[i])

    # this one is tested by merging all the letter files to one (under folder "letter")
    merge_text_files("Letters", "Merge.txt")

# Caesar file
    with CaesarFile("caesar.txt", shift=3) as lines:
        for line in lines:
            print(line)
