from welcomeandcheck import WelcomeAndCheck
from documentsmanager import Documents
from steps import Steps
from selector import Selector

selector = Selector()
COUNTER = 1
welcome_and_check = WelcomeAndCheck()
documents = Documents()
step = Steps()
JUST_ONCE = 0


# Welcome Message, Checks and set up the main loop
welcome_and_check.welcome()
running = True

while running:
    x = welcome_and_check.check()
    if not x:
        print('The Current version does not support your current tax situation, please wait for future updates'
              'which will incorporate more cases.\nMeanwhile do pay an accountant to do what we will be doing for free in a bit 😂')
        running = False
    elif x == 'invalid input':
        print('\n')
        print("Please print 'yes' or 'no' answer")
    elif x is True:
        documents.get_user_input()
        documents.prepare_documents()
        keep_on = True
        while keep_on:
            all_ready = input('Do You have all the required documents? yes or no: ').lower()
            with open(file="count.txt", mode="r") as file:
                check_step = int(file.read())
            if check_step > 6:
                print("You are at step no. 6 , there are only 6 steps in the program, 'proceed' is not a valid entry at this point")
                selector.step_selector()

            elif all_ready == 'no':
                print('Do not leave it to the last minute, go fitch the docs and come back when ready.')
                keep_on = False
                running = False
            elif all_ready == "yes":
                JUST_ONCE += 1
                if check_step == 1 and JUST_ONCE == 1:
                    step.start_declaration(documents.current_year)
                if selector.step_selector() is False:
                    keep_on = False
                    running = False

                else:
                    continue

            elif all_ready != 'no' or all_ready != 'yes':
                print('Please enter a valid input. For example: yes or no')