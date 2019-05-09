

def ask_for_name():
    name = input("What is your name?")
    return name


def ask_multiple_choice_question(question, numofoptions):
    answer2 = input(question)
    if (not answer2.isnumeric()):
        print("Please enter valid response")
        return ask_multiple_choice_question(question,numofoptions)
    elif int(answer2)>numofoptions:
        print("Please enter response within range")
        return ask_multiple_choice_question(question,numofoptions)
    return int(answer2)

def ask_about_movies():
    response = input("""What is the name of your favourite movie among the following
    Harry Potter, Captain America, DeadPool, American Pie ? (Type the name)
    """)
    if response.lower()=='harry potter' or response.lower()=='captain america':
        return 1
    elif response.lower()=='deadpool' or response.lower()=='american pie':
        return 2
    else:
        print("Incorrect value entered")
        ask_about_movies()
        
def ask_about_angelina():
    response = input("""Do you know Angelina Jolie?
    Y- Yes
    N- No
    """)
    if response.lower()=='y':
        return 1
    elif response.lower()=='n':
        return 2
    else:
        return 3

def ask_about_emma():
    response = input("""Do you know Emma Watson?
    Y- Yes
    N- No
    """)
    if response.lower()=='y':
        return 1
    elif response.lower()=='n':
        return 2
    else:
        return 3

def ask_for_study_hours():
    response = int(input("""How many hours do you study per week? (Enter 1,2 or 3)
    1. 1-3
    2. 4-10
    3. more than 10
    """))
    if int(response)>3:
        print("Enter value within range.")
    elif response==1:
        return 1
    elif response==2:
        return 2
    else:
        return 3

def ask_branching_question():
    initial= ask_multiple_choice_question("""Who is your favourite actor?
    1. Daniel Radcliff
    2. Brad Pitt
    3. Don't watch movies?
    """,3)
    if initial==1:
        follow_up= ask_about_emma()
    elif initial==2:
        follow_up=ask_about_angelina()
    elif initial==3:
        follow_up= ask_for_study_hours()
    """This method returns nerd score of 2 if the person has favourite actors and their favourite movie is deadpool or american pie.
    If person doesn't watch movies and does not know Angelina Jolie or favourite movie is 'Harry Potter' or 'Captain America' it returns score of 5.
    Returns score of 10 if the person studies more than 10 hours. For other cases returns score of 7 """
    if (initial==1 and follow_up ==2) or (initial==1 and follow_up ==3) or (initial==2 and follow_up==1):
        nerd_score_branching = 2
    elif (initial==1 and follow_up ==1) or (initial==2 and follow_up==2):
        nerd_score_branching = 5
    elif (initial==3 and follow_up==3):
        nerd_score_branching = 10
    else:
         nerd_score_branching=7
    return int(nerd_score_branching)

def report_results(question1,question2,question3,question4,name):
    """This method calculates the berd score based on habits and preferences of user.
    If the person prefers coffee and either prefers chess or no sports and has nerd score from branching question of more than 7; then final nerd score is 10.
    If the person prefers Milkshake and enjoys sports like basketball/ tennis and has nerd score from branching question between 5-7; then final nerd score is 7.
    If the person prefers Beer and enjoys more than one sports and has nerd score from branching question less than 5; then final nerd score is 5. """

    if (question1==2 or question1==1) and (question2==3 or question2==4 )  and question3 > 7 and question4==1:
        score = 10
    elif question1==3 and (question2==2 or question2==1 ) and (question3>5 and question3<=7):
        score = 7
    elif question1==4 and question2==5 and question3<=5 and question4== 2:
        score = 5
    else:
        score = 3
    return score

#Execute if run as a script
if __name__ == "__main__":
    #User Name Question
    name = ask_for_name()
    print("*** Welcome "+name+" ! Let's find out what what level of nerd you are ***")
   #Multiple Choice Question
    question1 = ask_multiple_choice_question("""What is your favourite beverage?
        1. Coffee
        2. More Coffee
        3. Milkshake
        4. Beer
        """,4)
    question2 = ask_multiple_choice_question("""What is your favourite sport?
        1. Basketball
        2. Tennis
        3. Chess
        4. None
        5. More than one?
        """,5)
    # Branching question
    question3 = ask_branching_question()
    # Free response question
    question4 = ask_about_movies()
    finalscore = report_results(question1,question2,question3,question4,name)
print("******End of game!!!*******")
print("Hey "+name+ " ! Your nerd score is :"+ str(finalscore))
