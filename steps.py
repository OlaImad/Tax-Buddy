from documentsmanager import Documents
import ast
documents = Documents()
B3Investidor = {1: 'posicao', 2: 'negociacao'}

class Steps:

    def __init__(self):
        self.company_name = ""
        self.current_year = 0
        self.banks_list = []
        self.banks_dict = {}
        self.brokers_list = []
        self.brokers_dict = {}
        self.b3investidor = B3Investidor

    def start_declaration(self, year):
        print('\n')
        print("On the main page of the Receita Federal Program")
        print(f"Click on 'NOVA' then there are two cases: \n"
              f"1. If it is your first time then choose: Iniciar Declaração em Branco\n"
              f"2. If you have declared in the previous year choose: Iniciar Importando a "
              f"Declaracao de {year -1}"
              " Then set the -> Tipo : Declaração de Ajuste Anual.\n")

    def step(self, number):
        if number == 1:
            self.step_1()
        elif number == 2:
            self.step_2()
        elif number == 3:
            self.step_3()
        elif number == 4:
            self.step_4()
        elif number == 5:
            self.step_5()
        elif number == 6:
            self.step_6()


    def step_1(self):
        """It will guide the user through the first step, it also calls the step1 validation function"""
        print("\n")
        print("The First Step: IDENTIFICAÇÃO DO CONTRIBUINTE.\n")
        print("Fill your personal information including (Título Eleitoral)")
        print("If you have changed your addressed during the year, make sure to change the address")
        print("Highlights: Please update your personal information with any changes.")
        with open(file="info.txt", mode="r", encoding="utf8") as file:
            content = file.read()
            print(content)
            self.step1_validation()
        print("In case you have chosen to import that last year's Declaration, Please check that the N do Recibo is filled.")

    def step1_validation(self):
        """It will be called by step 1 to check if there is a change to occupation info in order to update the
        info.txt """
        validate = True
        while validate:
            info_change = input("\nIs there a change in occupation info? yes or no: ").lower()
            if info_change == 'no':
                print('proceed with the same codes above')
                validate = False


            elif info_change == 'yes':
                new_code = input("Please copy and past the new codes to be saved for next year's declaration:\n")
                with open(file="info.txt", mode="w", encoding="utf8") as file:
                    content = file.write(new_code)
                    print("file updated successfully!")
                    validate = False
                    # call step 2
            elif info_change != 'yes' or info_change != 'no':
                    print('please type a valid response')



    def step_2(self):
        with open(file="userinput.txt", mode="r") as file:
            company_name = file.readlines()[1]
        print("\nRENDIMENTOS TRIBUTÁVEIS RECEBIDOS DE PESSOA JURÍDICA PELO TITULAR.\n")
        print(f"Source: Informe de Rendimento De {company_name}\n")
        print("please fill the fields that are in the company's form in the appropriate place in the tax form.")

    def step_3(self):
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[2]
            banks_dict = ast.literal_eval(content)
        new_dict1 = {key: value['2'] for (key, value) in banks_dict.items()}
        # ---------------------------------------------------------------------
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[2]
            banks_dict = ast.literal_eval(content)
        new_dict2 = {key: value['1'] for (key, value) in banks_dict.items()}
        # ---------------------------------------------------------------------
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[3]
            banks_dict = ast.literal_eval(content)
        new_dict3 = {key: value['6'] for (key, value) in banks_dict.items()}
        print('\nRENDIMENTOS ISENTOS E NÃO TRIBUTÁVEIS.\n')
        print("1- Here you will have to fill the: Interest on bank accounts (Poupanca - Juros na Conta) CODIGO: 12.\n"
              f"Source: {new_dict1}\n")
        print("2- You will also need to fill The Dividends (VALOR LIQUIDO) - CODIGO: 9")
        print("Do not forget to fill any DIVIDENDS IN TRANSIT in a separate entry")
        print(f"Source: {new_dict2} AND {new_dict3}\n")
        print("3- Need to fill the profitable SWING TRADES which has a sales value less than 20K per month - CODIGO: 20")
        print(f"Go through sales in the: {documents.b3investidor[2]} and check the sales QUANTITY and sales VALUE for each sale,\n"
              f"then compare it to the corresponding share in excel sheet and nota de corretagem at the time of purchase and sale\n"
              f"Calculate the profit minus the taxes and commissions. We only need to fill a single entry which is the sum of all\n"
              f"sales during the year excluding taxes and commissions.")





    def step_4(self):
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[2]
            banks_dict = ast.literal_eval(content)
        new_dict = {key: value['1'] for (key, value) in banks_dict.items()}
        # -------------------------------------------------------------------
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[3]
            banks_dict = ast.literal_eval(content)
        new_dict2 = {key: value['6'] for (key, value) in banks_dict.items()}
        print("RENDIMENTOS SUJEITOS À TRIBUTAÇÃO EXCLUSIVA / DEFINITIVA\n")
        print("Here you will have to insert the JCP (Juros Sobre Capital) - CODIGO: 10")
        print(f"Source: {new_dict} AND {new_dict2}")
        print("Start with the Preventos and check each Source of JCP against it is record in the banks' statment.\n"
              "against the banks' statements, be carefull to cheeck for credit em transito ")
        print("NOTE: In case there is a JCP ( JCP CREDITO EM TRANSITO) for the same stock then make a separate entry for it\n"
              "Else, If there is only the ( JCP CREDITO EM TRANSITO) you will have to make an entry for it")



    def step_5(self):
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[2]
            banks_dict = ast.literal_eval(content)
        new_dict1 = {key: value['2'] for (key, value) in banks_dict.items()}
        # ------------------------------------------------------------------------
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[3]
            banks_dict = ast.literal_eval(content)
        new_dict2 = {key: value['1'] for (key, value) in banks_dict.items()}
        # -----------------------------------------------------------------------
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[3]
            banks_dict = ast.literal_eval(content)
        new_dict3 = {key: value['2'] for (key, value) in banks_dict.items()}
        # -----------------------------------------------------------------------
        with open(file="userinput.txt", mode="r") as file:
            content = file.readlines()[2]
            banks_dict = ast.literal_eval(content)
        new_dict4 = {key: value['1'] for (key, value) in banks_dict.items()}
        # -------------------------------------------------------------------------
        print("\nDECLARAÇÃO DE BENS E DIREITOS\n")
        print("1- SALDO NA CONTA : The bank account balance on 31/12 - (Groupo = 6, Codigo = 1)")
        print(f"Source: {new_dict1}\n")
        print("2- SALDO NA CONTA DE CORRETORA: The balance in the broker's account on 31/12 - (Groupo = 6, Codigo = 99)")
        print(f"Source: {new_dict2}\n")
        print("3- Declarar acoes holding em 31/12 - (Groupo = 3, Codigo = 1). The format to declare:\n"
              "EMPRESA: BANCO BRADESCO S.A. //CÓDIGO DE NEGOCIAÇÃO: BBDC3//CNPJ: 60746948000112//NUMÉRO DE AÇÕES: 10"
              "// ADQUIRIDAS AO PREÇO MÉDIO: R$ 16,50//VALOR TOTAL : R$ 165,00//CUSTODIA NA CORRETORA: XP INVESTIMENTOS"
              " CCTVM S/A (CORRETORA CLEAR)//CNPJ: 02.332.886/0001-04")
        print(f"Source: {new_dict3} AND {new_dict4}\n")
        print("4- CREDITO EM TRANSITO: (Groupo = 99, Codigo = 7) Here we have to declare the JCP em transito (the first \n"
              "step is to declare it in step 4,which if you did skipped please go back and fill it, and also the dividends\n"
              "in transit,first step to declare it in step 3, if skiiped please go back and fill it.\n"
              "make sure to check the (credito em transito) section and the situation on (31/12) of the previous year\n"
              "and on 31/12 the current year as it will be formatted as you should mention it in the declaration\n"
              "Check against last year's declaration")
        print("Remember! to zero any value from last year as it was credit to the account during the current year.")
        print(f"Source: {new_dict4}")
        print("Format:\n"
              "CRÉDITO EM TRÂNSITO, JUROS SOBRE CAPITAL (JCP) EMPRESA BANCO BRADESCO S.A. CNPJ: 60.746.948/0001-12 \n"
              "VALOR TOTAL: R$ 3,36 NA CORRETORA XP INVESTIMENTOS CCTVM S/A CNPJ: 02.332.886/0001-04 SERÁ LÍQUIDO \n"
              "EM ANO(S) SEGUINTE(S)\n")
        print("SWING TRADE: If there is a loss in swing trade for a share that we owned at or before the end of last year\n"
              "we have to declare it here with the sales value and will have to zero out the end of year balace for that share\n"
              "or deduct the number of shares we have sold from total owned, then fill in the loss amount in next step\n")



    def step_6(self):
        print("\nRENDA VARIÁVEL - OPERAÇÕES COMUNS/DAYTRADE - TITULAR")
        print("Here we will have to fill month by month the\n"
              "1- Day Trade operations\n"
              "Source: From Excel sheet and DARF\n"
              "Note: Remember to carry the loss from year to year and declarar IR na fonte that was paid in DARF\n"
              "Record the loss of the previous year from (last year's declaration and fill it in Jan of the current year."
              "2- Any Swing Trade operations with a sales value over 20K per month. It will be taxed at 15% rate.\n"
              "It needs to be filled excluding taxes and commissions and record the IR paid"
              "3- Any loss in Swing Trade Operations, only fill the amount of loss after recording the SALE in Bens e Direitos\n")
        print("Note: Calculate gains minus costs and losses plus custos\n")










