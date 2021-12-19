class Number:
    def __init__(self):
        '''Gets needed information(number) and sets some default values!'''
        self.input_number = int(input('Enter number : '))
        self.answer = 0
        self.sum = 0


    def sum_digits(self, number):
        '''Gets number and returns sum of its digits!'''
        for char in str(number):
            self.sum += int(char)
        
        self.answer = self.sum
        self.sum = 0

    def calculate(self):
        '''Keeps suming digits of the given number until answer is one digit.\n
        At the end prints the answer.
        '''
        self.sum_digits(number=self.input_number)
        
        while self.answer > 9 :
            self.sum_digits(self.answer)

        print(self.answer)




number = Number()
number.calculate()
