import random


class QuoteModel:
    def __init__(self):
        self.quotes = ['A man is not complete until he is married. Then he is finished.',
                       'As I said before, I never repeat myself.',
                       'Behind a successful man is an exhausted woman.',
                       'Black holes really suck...',
                       'Facts are stubborn things.']

    def get_random_quote_number(self):
        return random.randint(0, self.quotes.__len__()-1)

    def check_quote_number_valid(self, n):
        valid = False
        try:
            n = int(n)
            if n in range(-1, self.quotes.__len__()):
                valid = True
            else:
                print('The quote number should between 0 and {}'.format(self.quotes.__len__() - 1))
        except ValueError as err:
            print('The quote number should between 0 and {}'.format(self.quotes.__len__() - 1))
        return valid

    def get_quote(self, n):
        valid = self.check_quote_number_valid(n)
        value = 'Not found'
        if valid:
            if n == -1:
                random_num = self.get_random_quote_number()
                value = self.quotes[random_num]
            else:
                value = self.quotes[n]
        return value

    def add_quote(self, quote):
        self.quotes.append(quote)

    def show_all(self):
        return self.quotes

class QuoteTerminalView:
    def __init__(self):
        pass

    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see? ')

    def add_quote(self):
        return raw_input("Enter a new quote:")

    def show_all(self, quotes):
        print("All quotes are listed:")
        for quote in quotes:
            print(quote)



class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        n = self.view.select_quote()
        quote = self.model.get_quote(n)
        self.view.show(quote)

        ret = raw_input("Add a new quote?(Y/N)")
        if ret in ("y", "Y"):
            quote = self.view.add_quote()
            self.model.add_quote(quote)

        quotes = self.model.show_all()
        self.view.show_all(quotes)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()
