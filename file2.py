from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch", sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print("Happy birthday!")
        print(f"Age: {self._sender_age}")


# Test the BirthdayCard class
if __name__ == "__main__":
    card = BirthdayCard(sender_age=30)
    card.greeting_msg()
