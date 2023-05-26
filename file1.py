class GreetingCard:
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"Dear {self._recipient},")
        print(f"From: {self._sender}")


# Test the GreetingCard class
if __name__ == "__main__":
    card = GreetingCard()
    card.greeting_msg()
