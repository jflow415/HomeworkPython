#!/usr/bin/env python3                                                                                        
import pyinputplus as pyip                                                                                    
                                                                                                        
                                                                                                        
correctAnswers= 0                                                                                             

questionsDict={
    "Question1": (
        "1. Who killed Ned Stark?(A. Cersei/B. Joffrey/C. Jamie/D. Ilyn Payne",
        ("d","ilyn payne"),
        ("cersei should have never been born", "cersei should've never been born")
        ),
    "Question2": (
        "2.	Which character appeared in the most episodes?(A. Arya Stark/B. Jon Snow/C. Tyrion Lannister/D. Cersei Lannister",
        ("c","tyrion lannister")
        ),
    "Question3": (
        "3.	Which of these characters does the show never actually show physically sitting on the Iron Throne?(A.Robert Baratheon/B. Cersei Lannister/C. Ned Stark/D.Tywin Lannister",
        ("a","robert baratheon")
        ),
    "Question4": (
        "4. Before Game of Thrones, this actor/actress never acted before.(A. Peter Vaughan/B. Emilia Clarke/C. Kit Harington/D. Maisie Williams",
        ("d","maisie williams")
        ),
    "Question5": (
        "5.	A sword from lord of the Rings can be seen on the Iron Throne?(T. True/ F. False",
        ("t","true")
        ),
    "Question6": (
        "6.	What are the words of House Bolton?(A. Our Blades are Sharp/B. Unflinching/C. Death Before Disgrace/D. Cut Deepest",
        ("a","our blades are sharp")
        ),
    "Question7": (
        "7.	What is Hodor’s Real name?(A. Wyllem/B. Eddard/C. Wylis/D. Mycahal",
        ("c","wylis")
        ),
    "Question8": (
        "8.How many Great Masters does Dany crucify to retaliate for the slave children killed?(A. 211/B. 163/C. 150/D. 101",
        ("b","163")
        ),
    "Question9": (
        "9.	What is the tallest structure in the world of Game of Thrones?(A. Oldtown’s High Tower/B. The Great Pyramid of Meereen/C. The wall/D. Red Keep",
        ("a","oldtown's high tower")
        ),
    "Question10": (
        "10. How many times has Beric Dondarrion died?(A. 6/B. 4/C. 8/D. 7",
        ("d","7")
        )
        
}

def handlequestion(question):                                                                                                     
    #Handles the question                                                                                                
    answer = input(f"{question[0]}\n")
    answer = answer.strip().lower()             
    if answer in question[1]:                                                         
        global correctAnswers
        correctAnswers += 1                                                                                   
        print(f"Good job your score is now {correctAnswers}")
    #secret answer check
    elif len(question) == 3:
        if answer in question[2]:
            correctAnswers += 100
            print(f"You have answered the secret question. Your score is now {correctAnswers}")
        else:
            print(f"Wrong! You are a failure. The answer is {question[1]}.")  

    else:                                                                                                     
        print(f"Wrong! You are a failure. The answer is {question[1]}.")  

                                                                                             
while True:                                                                                                   
    prompt = "Want to play a Game of Thrones quiz?\n"                                                         
    response = pyip.inputYesNo(prompt)                                                                        
    if response =='yes': 
        #for each key in the dict                                                                                     
        for question in questionsDict:
            handlequestion(questionsDict[question])
        
        print(f"Your score is {correctAnswers}. Thanks for playing")
        break

                                                                                   
                                                                                                        
    elif response =='no':                                                                                     
        print('Thank you. Have a nice day.') 
        exit()