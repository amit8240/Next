from functools import reduce
import string
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


# ex 1
def longest_name(names):
    print(max(names))


def sum_names_len(names):
    print(reduce(lambda x, y: x + len(y), names, 0))


def print_shortest_names(names):
    print('\n'.join(filter(lambda name: len(name) == min(map(len, names)), names)))


def open_new_file(names):
    open("C:\\Users\\AMIT\\name_length.txt", "w").writelines([str(len(name)) + '\n' for name in names])


def name_by_length(names, length):
    print('\n'.join(filter(lambda name: len(name) == length, names)))


# ex 2
class Animal:
    """
    A class used to represent an animal
    """
    ZOO_NAME = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hanger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hanger > 0

    def feed(self):
        self._hanger -= 1

    def talk(self):
        print("cant talk")


class Dog(Animal):

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, name, hunger=0, stick_count=6):
        super().__init__(name, hunger)
        self._stick_count = stick_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):

    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


# ex 3

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character, position):
        super().__init__(f"Error: Username contains illegal character '{illegal_character}' at position {position}.")


class UsernameTooShort(Exception):
    def __init__(self):
        super().__init__("Error: Username is too short.")


class UsernameTooLong(Exception):
    def __init__(self):
        super().__init__("Error: Username is too long.")


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Error: Password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __init__(self):
        super().__init__("Error: Password is too short.")


class PasswordTooLong(Exception):
    def __init__(self):
        super().__init__("Error: Password is too long.")


def check_input(username, password):
    # Check username
    for position, character in enumerate(username):
        if not character.isalnum() and character != '_':
            raise UsernameContainsIllegalCharacter(character, position + 1)
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    # Check password
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True
        elif character in string.punctuation:
            has_special = True
    if not has_uppercase:
        raise PasswordMissingUppercase()
    if not has_lowercase:
        raise PasswordMissingLowercase()
    if not has_digit:
        raise PasswordMissingDigit()
    if not has_special:
        raise PasswordMissingSpecial()
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    print("OK")


# ex 4

def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{sec:02d}"


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    if month == 2:
        if leap_year:
            yield 29
        else:
            yield 28
    elif month in [4, 6, 9, 11]:
        yield 30
    else:
        yield 31


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for days in gen_days(month, (year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                for day in range(1, days + 1):
                    for time in gen_time():
                        yield f"{day:02d}/{month:02d}/{year:02d} {time}"


# ex 5

def check_id_valid(id_number):
    id_list = list((int(num) % 10 + int(num) // 10) for num in list(int(num) *
                                                                    [1, 2][i % 2] for i, num in
                                                                    enumerate(str(id_number))))
    return sum(id_list) % 10 == 0


class IDIterator:
    def __init__(self, _id):
        self._id = _id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id > 999999999:
            raise StopIteration

        while True:
            self._id += 1
            if check_id_valid(self._id):
                return self._id


def id_generator(id_number):
    while id_number <= 999999999:
        id_str = str(id_number).zfill(9)
        if check_id_valid(id_str):
            yield id_str
        id_number += 1
    raise StopIteration


# list of dots, in the following format: [x, y, x, y, x, y,...]
first = (
    146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
    355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
    178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
    307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
    199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
    389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
    216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
    365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
    215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
    290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
    279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
    291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
    306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
    393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
    336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
    259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
    349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
    234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
    339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
    122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
    214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
    134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
    171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
    115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
    89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108,
    132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149,
    77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111,
    156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259,
    136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153,
    366, 149, 379, 147, 394, 146, 399
)
second = (
    156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186,
    150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175,
    159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146,
    218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172,
    114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81,
    162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126,
    113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157,
    128, 156, 134, 157, 136, 156, 136
)


def main1():
    input_file = open(r'C:\\Users\\AMIT\\names.txt', "r")
    names = input_file.read().split('\n')
    print(names)
    longest_name(names)
    sum_names_len(names)
    print_shortest_names(names)
    open_new_file(names)
    file_path = open(r"C:\\Users\\AMIT\\name_length.txt", "r")
    print('\n'.join(file_path.read().split('\n')))
    length = int(input("Enter name length: "))
    name_by_length(names, length)


def main2():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky")
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    zoo_lst = [dog, cat, skunk, unicorn, dragon]
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)
    zoo_lst.extend([dog2, cat2, skunk2, unicorn2, dragon2])
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__, animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        else:
            animal.breath_fire()
    print(skunk.ZOO_NAME)


def main3():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except Exception as e:
            print(e)
            continue


def main4():
    # for gt in gen_time():
    #     print(gt)
    date_gen = gen_date()
    count = 1
    for date in date_gen:
        if count % 1000000 == 0:
            print(date)
        count += 1


def main5():
    id_number = int(input("Enter ID: "))
    gen_or_it = input("Generator or Iterator? (gen/it)? ")
    if gen_or_it == "gen":
        id_gen = id_generator(id_number)
        for i in range(10):
            print(next(id_gen))
    else:
        id_it = IDIterator(id_number)
        for i in range(10):
            print(next(id_it))


def main6():
    image = Image.open("ex6p4.jpg")
    draw = ImageDraw.Draw(image)
    draw.line(first, fill="red")
    draw.line(second, fill="red")
    plt.imshow(image)
    plt.show()


if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    main6()
