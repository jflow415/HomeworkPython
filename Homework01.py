#!/usr/bin/env python3                                                                                        
import pyinputplus as pyip                                                                                    
                                                                                                        
                                                                                                        
correctAnswers= 0                                                                                             
                                                                                                        
def q1():                                                                                                     
    #Question 1                                                                                               
    question1 = input( "1. Who killed Ned Stark?(A. Cersei/B. Joffrey/C. Jamie/D. Ilyn Payne)\n")             
    if question1 == "d" or question1 == "Ilyn Payne":                                                         
        global correctAnswers
        correctAnswers += 1                                                                                   
        print(f"Good job your score is now {correctAnswers}")                                                  
    else:                                                                                                     
        print("Wrong! You are a failure. The answer is Ilyn Payne.")      
def q2():                                     
    #Question 2 
    question1 = input( "1. Who killed Ned Stark?(A. Cersei/B. Joffrey/C. Jamie/D. Ilyn Payne)\n")             
    if question1 == "d" or question1 == "Ilyn Payne":                                                         
        global correctAnswers
        correctAnswers += 1                                                                                   
        print(f"Good job your score is now {correctAnswers}")                                                  
    else:                                                                                                     
        print("Wrong! You are a failure. The answer is Ilyn Payne.")                                                                                              



while True:                                                                                                   
    prompt = "Want to play a Game of Thrones quiz?\n"                                                         
    response = pyip.inputYesNo(prompt)                                                                        
    if response =='yes':                                                                                      
        q1()                                                                                                  
                                                                                   
                                                                                                        
    elif response =='no':                                                                                     
        print('Thank you. Have a nice day.') 
        exit()