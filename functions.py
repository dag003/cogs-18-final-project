"""A collection of function for doing my project."""
import time
import random
from IPython.display import Image
from my_module.classes import Question
from my_module.classes import Question_2

questions_blue  = [
     "1. Would you aviod someone who is being casted out? \n a. No,I would'nt I dont mind being thier friend \
      \n b. yes, I have been told they cause trouble \n c. No. I understand how they might be feeling \
      \n d. I woul'nt  care \n ",
    
     "2. Would you ever run away from your best friend? \n a. No, I would try to help them \
      \n b. I have my own curese to run away from.\n c. No one would care if I Do \
      \n d. I'm a runner im a trackstar 🏃‍♂️ \n",
   
     "3. Your bestie asks if you want to go sky watching wyd? \n a. I'm going to take a nap under a tree\
     \n b.no \n c. Maybe next time \n d. Ignore them \n",
    
     "4. What is your form of confrontation? \n a. Ask directly \n b. I am not going to press the issue \
     \n c.Confrontation who? Dont know them \n d. Run Away part 2\n ",
    
     "5. You have the night offf, what will you choose to do? \n a. SLEEP OMG lots of sleep \
     \n b.Try to find my desting once and for all. \n c. Train and get stronger \
     \n d. Watch the stars \n ",
    
     "6. What do you prefer in a friend? \n a. Has the greatest Neflix recommendations \
     \n b. For someone to always be there \n c. Someone who is loud \n d. A kind person\n ",
    
     "7. What do you consider to be a weekness? \n a. Laziness \
     \n b. Animals \n c. Spending too much time on your phone \n d. Being shy \n ",
     
     "8. What do you consider a strength? \n a. Being strong \n b. Dealing with people \
     \n c. Paying attention to details \n d. I am great \n ",
    
     "9. What is your favorite color? \n a. Red \n b. Green \n c. Blue \n d. black \n"
    
]

question_purple = [ 
    "1. You are stuck in the middle of a forest...quick do you \n a. Take a nap b. look for a way out \
    \n c. throw a party \n d. enjoy your stay \n",
    "2. They call you weak what do you say? \n a. Fight them \n b. Ignore them \
    \n  c. Wait for karma to do it's thing \n d. Not pay attention to them \n", 
    "3. On a Sunday Morning do you.. \n a. spend time with your parents \n b. do everything to aviod them \
    \n c. spend time with friends \n d. read a book \n", 
    "4. What is your favorite food?\n a. orange \n b. apples \n c. cherry \n d. mango \n"
    
]



response = [
     Question(questions_blue[0], "a" ),
     Question(questions_blue[1], "b" ),
     Question(questions_blue[2], "a" ),
     Question(questions_blue[3], "b" ),
     Question(questions_blue[4], "c" ),
     Question(questions_blue[5], "b" ),
     Question(questions_blue[6], "d" ),
     Question(questions_blue[7], "d" ),
     Question(questions_blue[8], "a" ) 
              
]

response_purple = [
     Question_2(question_purple[0], "c" ),
     Question_2(question_purple[1], "b" ),
     Question_2(question_purple[2], "a" ),
     Question_2(question_purple[3], "d" )
    
]

def examing_results(score):
    
    """"
    
    Parameters
    ----------
    score : int 
        Takes in number of questions answered correctly. 
        
    Returns
    -------
    none : 
        It gives the used a commonent about their score and opens and image so they 
        can see their best friend. 
    
    """
    
    if score == 9 : 
        print("you seem like you would be shikumara's bestfriend")
        display(Image(filename='./project_pics/naruto_shikumar.png'))
        
    elif score == 7 or score == 8:
        print("you seem like you would be neji's bestfriend")
        display(Image(filename='./project_pics/neji_naruto.jpeg'))
            
    elif score == 4 or score == 5 or score == 6: 
        print("maybe gaara is your bestie")
        display(Image(filename='./project_pics/gaara_naruto.jpg'))
        
    elif score == 0 or score == 1 or score == 2 or score == 3: 
        print("Well... please play again? ")
        display(Image(filename='./project_pics/confusion.jpg'))
        
def examing_results_purple(number):
    
    """"
    
    Parameters
    ----------
    score : int 
        Takes in number of questions answered correctly. 
        
    Returns
    -------
    none : 
        It gives the used a commonent about their score and opens and image so they 
        can see their best friend. 
    
    """
    
    if number == 4 : 
        print("you seem like you would be Hinata's bestfriend")
        display(Image(filename='./project_pics/4ever_goals.jpeg'))
        
    elif number == 3:
        print("you seem like you would be bestfriends with these too... I'm kind jealous")
        display(Image(filename='./project_pics/tear_naturo.jpeg'))
            
    elif number == 2: 
        print("maybe ino is your bestie")
        display(Image(filename='./project_pics/ino_naruto.jpeg'))
        
    elif number == 0 or number == 1 : 
        print("Sorry just SORRY! :( ")
        display(Image(filename='./project_pics/sakura_naruto.jpg'))
        
def beginning(): 
    """"
    Introduction to Quiz.  
    
    Parameters
    ----------
        None
        
    Returns
    -------
    quiz_options(): Funtion 
        At the end of the print statement it will prompt the quiz options
    
    """
    # Welcomes the user and asks for users name.
    
    print ("Welcome to my anime quiz.")
    time.sleep(1)
    print ("I hope you have fun!.")
    time.sleep(1)
    name = input("What is your name \n")
    print("Hello", name, "you have quite a jouney ahead of you")
    time.sleep(1)
    print ("Let's start!!!!")
    
    quiz_options()
    
    
def quiz_options():
    
    """"
    It is the menu for the quiz. Where the user is presented with two different options. 
    At the end of the print statement it will prompt the quiz options. 
            
    Parameters
    ----------
        None
        
    Returns
    -------
        None    
    """
    # They are able to type which option they want and can be taked to that quiz respectively.
    # If user types in anything else it will end the game. 

    response = input("Take a chance, pick between blue or purple\n")
    
    if response == "blue".lower():
        print("I can see that you have very good judgement")
        ask_question(questions_blue, attempts =3) 
        
    if response == "purple".lower():
        print("YOU ARE SUPIRIOR IDC WHAT ANYONE SAYS!")
        ask_question_purple(question_purple, attempts =3)   
    
def ask_question(question, attempts =3):
    
    """"
    Ask_question asks the user the question in order and if correct adds a point to score other wise
    tells you how many attempts you have left. 
    At the end of the loop it will take the score and determine your result.
    
    Parameters
    ----------
    question: str
        Questions for the option blue 
    attempts : int 
        Has a set value of 3 
        
    Returns
    -------
    None : 
    """
    
    score = 0 
    
    # 
    for question in response: 
        
        while attempts > 0: 
            answer = input(question.questions_blue).lower()
            if answer == question.answer:
                score += 1
                break
            else: 
                print("You have", (attempts - 1) , "left")
                attempts -=1
                continue 
                
    examing_results(score)
    
def ask_question_purple(question_purple, attempts =3):
    
    """"
    Ask_question asks the user the question in order and if correct adds a point to score other wise
    tells you how many attempts you have left. 
    At the end of the loop it will take the score and determine your result.
    
    Parameters
    ----------
    question: str
        Questions for the option blue 
    attempts : int 
        Has a set value of 3 
        
    Returns
    -------
    None :

    """
    
    number = 0 
    
    # 
    for question in response_purple: 
        
        while attempts > 0: 
            answer = input(question.question_purple).lower()
            if answer == question.answer:
                number += 1
                break
            else: 
                print("You have", (attempts - 1) , "left")
                attempts -=1
                continue 
                
    examing_results_purple(number)