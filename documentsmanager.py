B3Investidor = {1: 'posicao', 2: 'negociacao'}

class Documents:

    def __init__(self):
        self.current_year = 0
        self.company_name = ""
        self.banks_list = []
        self.banks_dict = {}
        self.brokers_list = []
        self.brokers_dict = {}
        self.b3investidor = B3Investidor


    def get_user_input(self):
        """Gets user input and assigned it to the corresponding class attribute"""
        try:
            self.current_year = int(input('Please enter the CURRENT year (2021,2022,...): '))
        except ValueError:
            print("Please enter a valid year: YYYY")
            self.get_user_input()
        else:
            with open(file="userinput.txt", mode="w") as file:
                content = file.write(f"{self.current_year}\n")
            self.company_name = input('Which company do you work for? ').lower()
            # write the company name to the userinput.txt file
            with open(file="userinput.txt", mode="a") as file:
                content = file.write(f"{self.company_name}\n")
             # Get Banks' Dictionary
            banks = input(
                f'Please list the banks where you have or had an account during {self.current_year - 1}? separated by comma\n'
                f'like so: bank1, bank2, bank3, .....: ').lower()
            self.banks_list = banks.split(',')
            for bank in self.banks_list:
                self.banks_dict[f'{bank}'] = {'1': 'Comprovante para declaracao de rendimentos ativos e escriturais',
                                           '2': 'informe de rendimentos financeiros'
                                           }
            # write the list to the userinput.txt file
            with open(file="userinput.txt", mode="a") as file:
                content = file.write(f"{self.banks_dict}\n")

            # Get Brokers' Dictionary
            brokers = input('Please enter the name of your Brokers seperated by a comma like so: broker1, broker2,\n'
                                ' broker3, .....: ').lower()

            self.brokers_list = brokers.split(',')

            for broker in self.brokers_list:
                self.brokers_dict[f'{broker}'] = {'1': 'Annual', '2': 'Custodia', '3': 'Day Trade', '4': 'extrato', '5': 'Operacoes',
                                       '6': 'Preventos'}
            with open(file="userinput.txt", mode="a") as file:
                content = file.write(f"{self.brokers_dict}\n")

    def prepare_documents(self):
        print('Please prepare the following documents before moving to the next step.\n')
        print(self.company_name + ': Informe de Rendimento De Empresa.')
        print('Source: will be provided by the Employer.\n')
        print(self.banks_dict)
        print("Can be downloaded from the banks' app or websites.\n")
        print(self.brokers_dict)
        print("Source: It will be available in your brokerage account.\n")
        print(f"B3 Investidor (CEI): {self.b3investidor}")
        print("Source: It can be found and downloaded from your account with B3 Investidor.\n")
