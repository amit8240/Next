import winsound
import tkinter as tk
from PIL import ImageTk, Image
from file1 import GreetingCard
from file2 import BirthdayCard
from gtts import gTTS
from playsound import playsound
import math


def double_letter(my_str):
    return ''.join(map(lambda x: x * 2, my_str))


##################################
def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, range(1, number + 1)))


##################################
def sum_of_digits(number):
    return sum(map(int, str(number)))


##################################
def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))


##################################
def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1))


##################################
def is_funny(string):
    return all(char == 'h' or char == 'a' for char in string)


##################################
def decode(password):
    return ''.join(chr((ord(char) - 97 + 2) % 26 + 97) if char.isalpha() else char for char in password)


##################################
class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        Octopus.count_animals += 1
        self._name = name
        self._age = 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


##################################
class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average_color = (self._red + self._green + self._blue) // 3
        self._red = average_color
        self._green = average_color
        self._blue = average_color

    def print_pixel_info(self):
        color_info = f"Color: ({self._red}, {self._green}, {self._blue})"
        color_info += " " + self.get_nonzero_color_name()
        print(f"X: {self._x}, Y: {self._y}, {color_info}")

    def get_nonzero_color_name(self):
        if self._red > 50 and self._green == 0 and self._blue == 0:
            return "Red"
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            return "Green"
        elif self._red == 0 and self._green == 0 and self._blue > 50:
            return "Blue"
        else:
            return ""


#############################
class BigThing:
    def __init__(self, variable):
        self._variable = variable

    def size(self):
        if isinstance(self._variable, (int, float)):
            return self._variable
        elif isinstance(self._variable, (list, dict, str)):
            return len(self._variable)


#############################
class BigCat(BigThing):
    def __init__(self, variable, weight):
        super().__init__(variable)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"


#############################
def raise_stop_iteration():
    next(iter([]))


#############################
def raise_zero_division_error():
    x = 1 / 0


#############################
def raise_assertion_error():
    assert 2 + 2 == 5


#############################
def raise_import_error():
    #import not_exist
    pass


#############################
def raise_key_error():
    my_dict = {'key': 'value'}
    print(my_dict['non_existing_key'])


#############################
def raise_syntax_error():
    eval("print('Hello, world!')")


#############################
def raise_indentation_error():
    print("Indentation Error")
     # print("Indentation Error")


#############################
def raise_type_error():
    x = "hello" + 1


#############################
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            return f"__CONTENT_START__\n{contents}\n__CONTENT_END__"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"


#############################
class UnderAge(Exception):
    def __init__(self, age):
        super().__init__()
        self._age = age

    def __str__(self):
        return f"Your age is {self._age}. In {18 - self._age} years, you'll be able to reach Ido's birthday!"


#############################
def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


#############################
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_words = (words.get(word, word) for word in sentence.split())
    translated_sentence = ' '.join(translated_words)
    return translated_sentence


#############################
def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#############################
def primes_generator(start):
    while True:
        if is_prime(start):
            yield start
        start += 1


#############################
def first_prime_over(n):
    primes = primes_generator(n + 1)
    return next(primes)


#############################
def parse_ranges(ranges_string):
    ranges = (range(int(start), int(stop) + 1) for start, stop in
              (pair.split('-') for pair in ranges_string.split(',')))
    numbers = (num for range_ in ranges for num in range_)
    return numbers


#############################
def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


#############################
def little_song():
    freqs = {
        "la": 220,
        "si": 247,
        "do": 261,
        "re": 293,
        "mi": 329,
        "fa": 349,
        "sol": 392,
    }

    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    note_list = notes.split('-')
    for note in note_list:
        note_info = note.split(',')
        note_name = note_info[0]
        duration = int(note_info[1])

        frequency = freqs[note_name]
        winsound.Beep(frequency, duration)


#############################
class MusicNotes:
    def __init__(self):
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 34:
            raise StopIteration

        self.index += 1
        self.notes.append(self.notes[self.index] * 2)

        return self.notes[self.index]


#############################
image_label = 0


def show_image():
    image_path = "photo.png"
    image = Image.open(image_path)
    image = image.resize((300, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo


#############################

if __name__ == '__main__':
    # -----------------1-----------------
    # print(double_letter("we are the champions!"))
    # print(four_dividers(9))
    # print(sum_of_digits(104))
    # print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
    # print(is_prime(4))
    # print(is_funny("hahahahahaha"))
    # print(decode("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))

    ###############################
    # -----------------2-----------------

    # animal1 = Octopus("amit")
    # animal2 = Octopus()
    # animal1.birthday()
    # print(animal1.get_name())
    # print(animal2.get_name())
    # animal2.set_name("Oct")
    # print(animal2.get_name())
    # print(Octopus.count_animals)

    # p = Pixel(5, 6, 250, 0, 0)
    # p.print_pixel_info()
    # p.set_grayscale()
    # p.print_pixel_info()

    # my_thing = BigThing("balloon")
    # print(my_thing.size())
    #
    # cutie = BigCat("mitzy", 22)
    # print(cutie.size())

    ###############################
    # -----------------3-----------------

    # raise_stop_iteration()
    # raise_zero_division_error()
    # raise_assertion_error()
    # raise_import_error()
    raise_key_error()
    # raise_syntax_error()
    # raise_indentation_error()
    # raise_stop_iteration()
    # print(read_file("file_does_not_exist.txt"))
    # send_invitation("Alice", 17)
    # send_invitation("Bob", 20)

    ###############################
    # -----------------4-----------------

    # print(translate("el gato esta en la casa"))
    # print(first_prime_over(1000000))
    # print(list(parse_ranges("1-2,4-4,8-10")))
    # print(list(parse_ranges("0-0,4-8,20-21,43-45")))
    # fibo_gen = get_fibo()
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))

    ###############################
    # -----------------5-----------------

    # little_song()
    # numbers = iter(range(1, 101))
    # for i in numbers:
    #     try:
    #         print(i)
    #         next(numbers)
    #         next(numbers)
    #     except StopIteration:
    #         break

    # notes_iter = iter(MusicNotes())
    # for freq in notes_iter:
    #     print(freq)

    ###############################
    # -----------------6-----------------

    # window = tk.Tk()
    # window.title("tk")
    # question_label = tk.Label(window, text="What is your favorite video?")
    # question_label.pack()
    # button = tk.Button(window, text="click to find out!", command=show_image)
    # button.pack()
    # image_label = tk.Label(window)
    # image_label.pack()
    # window.mainloop()

    # card1 = GreetingCard()
    # card2 = BirthdayCard(sender_age=25)
    # card1.greeting_msg()
    # print()
    # card2.greeting_msg()

    sentence = "first time i'm using a package in next.py course"
    tts = gTTS(text=sentence, lang='en')
    tts.save('output.mp3')
    playsound('output.mp3')
