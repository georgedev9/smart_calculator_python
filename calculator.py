import re

class Calculator:

    def __init__(self):
        self.variable_dict = {}
        self.variable_name = None
        self.variable_value = None
        self.user_input = None

    def verify_variable_exp(self, operation):
        return re.fullmatch(r"\s*[a-zA-Z]+\s*=\s*[0-9]+\s*", operation)

    def verify_wrong_exp(self):
        name = re.search(r"[0-9]+", self.variable_name)
        if name:
            return 'Invalid identifier'
        return 'Invalid assignment'

    def is_variable(self, operation):
        return re.fullmatch(r"[a-zA-Z]+", operation)

    def add_variable(self):
        self.variable_dict[self.variable_name] = int(self.variable_value)

    def variable_to_variable(self, operation):
        return re.fullmatch(r"\s*[a-zA-Z]+\s*=\s*[a-zA-Z]+\s*", operation)

    def format_variable(self, variable):
        key, value = variable.split("=", maxsplit=1)
        self.variable_name = key
        self.variable_value = value
        
    def assign_variable(self):
        self.format_variable(self.user_input)
        if self.verify_variable_exp(self.user_input):
            self.add_variable()
        elif self.variable_to_variable(self.user_input):
            variable = self.variable_dict.get(self.variable_value, False)
            if not variable:
                print('Invalid assignment')
            else:
                self.variable_dict[self.variable_name] = self.variable_dict.get(self.variable_value)
        else:
            print(self.verify_wrong_exp())

    def evaluate_expression(self):
        try:
            if self.is_variable(self.user_input):
                print(self.variable_dict.get(self.user_input, "Unknown variable"))
            else:
                expression = self.user_input
                for variable in self.user_input:
                    if variable.isalpha() and variable in self.variable_dict:
                        expression = expression.replace(variable, str(self.variable_dict.get(variable)))
                # checks and replace normal division and exponentiation
                if '/' in expression:
                    expression = expression.replace("/", "//")
                if '^' in expression:
                    expression = expression.replace("^", "**")
                print(eval(expression))
        except NameError:
            print("Invalid identifier")
        except SyntaxError:
            print("Invalid expression")

    def start_calc(self):
        while True:
            self.user_input = input().replace(" ", "")

            if self.user_input == '/exit':
                print("Bye!")
                break
            elif self.user_input == '/help':
                print("The program calculates math expressions like: '4 + 6 - 8' and shows the result")
            elif self.user_input == '':
                pass
            elif self.user_input.startswith('/'):
                print('Unknown command')
            elif '=' in self.user_input:
                self.assign_variable()
            else:
                self.evaluate_expression()

def main():
    Calculator().start_calc()


if __name__ == "__main__":
    main()