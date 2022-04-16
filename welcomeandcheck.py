class WelcomeAndCheck:

    def __init__(self):
       self.check_answer = ""

    def welcome(self):
        print('Welcome to your Tax Buddy!')
        print('\n')
        print('Please note that this program was created to give you instruction  on how to fill your tax\n'
              ' declaration.\n It will walk you hand by hand to prepare the required documents and fill the\n'
              ' declaration.\n However, please note that It was created for specific situation, new features\n'
              'will be added to serve wider audience.')

    def check(self):
        print('\n')
        self.check_answer = input('Check if the current version of Tax Buddy is for you.\n\n'
                      'Are you a salaried employee?\n'
                      'Have you made investments in the stock market?\n'
                      'You are not a: prestador de serviços have, or sócio de empresa, or aposentado.\n'
                      'You do not have a car or house in your name?\n'
                      'If your answer is YES to the previous questions\n'
                      'Then type(yes) or else type (no): ').lower()
        if self.check_answer == 'no':
            return False
        elif self.check_answer == 'yes':
            return True
        else:
            return 'invalid input'
