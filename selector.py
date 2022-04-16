from steps import Steps
from welcomeandcheck import WelcomeAndCheck
from documentsmanager import Documents

documents = Documents()
welcomeandcheck = WelcomeAndCheck()
step = Steps()


class Selector:


    def __init__(self):
        with open(file="count.txt", mode="r") as file:
            content = file.read()
        self.step_number = content

    def step_selector(self):
        user_choice = input("Type 'proceed' to move to the next step, Type 'restart' to  navigate back to the beginning,\n"
                                "Type the step number (1 or 2 or .... 6)to move to a specific step,\n"
                                "Type 'done' to end the program: ").lower()


        if user_choice == 'proceed':
            with open(file="count.txt", mode="r") as file:
                content = file.read()
     
                with open(file="userinput.txt", mode='r') as file1:
                    year = int(file1.readlines()[0])
                self.step_number = int(content)
                if self.step_number > 6:
                    print("There are only 6 steps- You are at step 6-can not 'proceed', Please enter a valid input\n")
                    if self.step_selector() is False:
                        print("The program can't be terminated at this step, please terminate at the next step")

                else:
                    next_step = self.step_number
                    # print(next_step)
                    step.step(next_step)
                    with open(file="count.txt", mode="w") as file2:
                        content = file2.write(f"{int(content) + 1}")


        elif user_choice == "restart":
            with open(file="userinput.txt", mode="r") as file:
                year = int(file.readlines()[0])
            step.start_declaration(year)
        elif user_choice == "1":
            step.step(1)
            with open(file="count.txt", mode="w") as file:
                content = file.write("1")
                self.step_number = content
        elif user_choice == "2":
            step.step(2)
            with open(file="count.txt", mode="w") as file:
                content = file.write("2")
                self.step_number = content
        elif user_choice == "3":
            step.step(3)
            with open(file="count.txt", mode="w") as file:
                content = file.write("3")
                self.step_number = content
        elif user_choice == "4":
             step.step(4)
             with open(file="count.txt", mode="w") as file:
                content = file.write("4")
                self.step_number = content
        elif user_choice == "5":
            step.step(5)
            with open(file="count.txt", mode="w") as file:
                content = file.write("5")
                self.step_number = content
        elif user_choice == "6":
            step.step(6)
            with open(file="count.txt", mode="w") as file:
                content = file.write("6")
                self.step_number = content

        elif user_choice == 'done':
            with open(file='count.txt', mode="w") as file:
                reset = file.write("1")
            with open(file='userinput.txt', mode="w") as file:
                reset = file.write("")
            print("The data you have entered have been deleted, Bye!")
            return False
        elif user_choice not in ("proceed", "done","restart","1","2","3","4","5","6"):
            print("Please enter a valid input")
            self.step_selector()

        elif int(user_choice) > 6:
            print('There are only 6 steps. Please enter a valid input\n')
            self.step_selector()




