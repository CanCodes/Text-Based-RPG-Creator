class Game:
    def __init__(self, name):
        self.name = name
    
    def cls(self):
        print("\n" * 50)

    def say(self, text) -> None:
        """ Basic print function. """
        self.cls()
        print(text)
        input("\n\n\nPress any key to continue.")
    
    def ask(self, question = str) -> str:
        """ Simple and plain question. Returns string. Accepts string """
        self.cls()
        return input(question)
    
    def ask_choices(self, question = str, choices = list) -> tuple:
        """ Ask questions with choices. Choices list should contain the choices you give to the player. Returns the choice index and text. """
        self.cls()
        choices_string = "\n".join([f"{choices.index(choice)+1}) {choice}" for choice in choices])
        answer = int(input(f'{question}\n\n\n{choices_string}\n')) - 1
        if answer > len(choices):
            self.ask_choices(question, choices)
        else:
            return (answer, choices[answer])
    