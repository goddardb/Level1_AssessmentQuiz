'''This is my sumbission for NCEA Level 1 Assessment 92004.
   It is a quiz based on the Maori korero of the legend of Mauao,
   and users will have to answer eight multiple choice questions, 
   recieving a score at the end. 
   Created by Ben Goddard 24/04/2026 till //2026.'''

# This initialises constants, states the questions and answers,
# and imports modules for later in the code.
import time
import os
NUM_OF_QUES = 8
POINTS_PER_ANS = 1
MIN_DISP_CURR_SCOR = 0
FIRST_SCOR_SPLIT = 80
SEC_SCOR_SPLIT = 60
THIRD_SCOR_SPLIT = 35
score = 0
corrects = 0
question_list = ["1. What was the name of the chief mountain who was the "
                 "Nameless One's master?\n\nA) Otanewainuku\nB) Manunui\n"
                 "C) Maui\nD) Maungatautari\nE) Omanawa", 
                 "2. What was the name of the beautiful mountain the "
                 "Nameless One was in love with?\n\nA) Waipuna\nB) Hinewai\n"
                 "C) Karewa\nD) Puwhenua\nE) Matarangi", 
                 "3. Why was the Nameless One sad?\n\n"
                 "A) The trees on him were dying\nB) Otanewainuku was leaving\n"
                 "C) Puwhenua did not love him\n"
                 "D) The Moa were being hunted to extinction\nE) He had no name"
                 , "4. Who helped the nameless mountain?\n\nA) Forest birds\n"
                 "B) Otanewainuku and Puwhenua\nC) The rivers\n"
                 "D) Tane Mahuta and Papatuanuku\nE) Patupaiarehe", 
                 "5. How did the Patupaiarehe get the nameless mountain"
                 "to the entrance of Tauranga Moana?\n\nA) Magic\nB) Carried "
                 "him\nC) Using harakeke ropes\nD) Gave him legs\n"
                 "E) Dug a path to push him down", "6. What stopped the "
                 "Patupaiarehe when they were dragging the Nameless mountain?\n"
                 "\nA) Fatigue\nB) The sun rising\nC) Evil spirits\n"
                 "D) The Nameless One's protests\nE) Tane Mahuta", "7. What was"
                 " the name given to the mountain at the end of the story?\n\n"
                 "A) Mauao\nB) Maui\nC) Te Rapuhia\nD) Roderick\nE) Maungatapu"
                 , "8. What does 'Mauao' mean?\n\nA) 'Lowly one'\n"
                 "B) 'Blessed'\nC) 'Caught by the Dawn'\n"
                 "D) 'Mountain of Sorrow'\nE) 'Slave Mountain'"
                 ]
#Because of the range function and the index of question_list, question 1 
#actually becomes question 0 to the code.
q_and_a_dict = {0: 'A', 1: 'D', 2: 'C', 3: 'E', 4: 'C', 5: 'B', 6: 'A', 7: 'C'}
#Listing valid answers for invalid input detection
valid_ans = ['A', 'B', 'C', 'D', 'E']

#Introducing the program and providing instructions for the user.
print("Welcome to the legend of Mauao quiz!!")
print(f"Answer {NUM_OF_QUES} questions based on the Maori Legend of Mauao.")
print("This quiz is multichoice - Enter 'A', 'B', 'C', 'D', 'E' "
      "based on what answer you think is correct.")
print("Good luck!")
#Purposeless input statement allows the users to read the instructions
#and remove it when they are done
cont = input("Press 'Enter' to continue")
os.system('cls')

#Asking the user the questions.
#Accessing the question and answer text
for quesnum in range(NUM_OF_QUES):
   print(question_list[quesnum])
   #This code loops until the user enters a valid answer.
   while True:
      user_answer = input("Answer: ").upper()
      #This code checks if the input is valid.
      if user_answer in valid_ans:
         #Comparing input with the correct answer
         if user_answer == q_and_a_dict[quesnum]:
            print("Correct")
            #Tracks amount of correct answers
            score += POINTS_PER_ANS
            corrects += 1
         else:
            #Supplies feedback
            print(f"Incorrect.   The correct answer "
                  f"was {q_and_a_dict[quesnum]}")
         break
      #For invalid input
      else:
         print(f"Invalid input. Please enter either 'A', 'B', 'C', 'D', or 'E'")
         time.sleep(1.5)
         os.system('cls')
         print(question_list[quesnum])

   #Printing current score except for on the last question or if score is 0
   #(or whatever MIN_DISP_CURR_SCOR is set to.)
   if quesnum + 1 != NUM_OF_QUES and score > MIN_DISP_CURR_SCOR:
      print(f"Your current score is {score}")
   cont = input("Press 'Enter' to continue")
   time.sleep(0.5)
   os.system('cls')

#Printing socre and a message based on percentage.
percentage = corrects / NUM_OF_QUES * 100
if percentage == 100:
   print("Amazing! You got them all correct!")
elif percentage >= FIRST_SCOR_SPLIT:
   print("Nice Work, You answered most of the questions right.")
elif percentage >= SEC_SCOR_SPLIT:
   print("Pretty Good, You answered a lot right.")
elif percentage >= THIRD_SCOR_SPLIT:
   print("OK, you got some right.")
else:
   print("Better luck next time.")
print(f"Congratulations on completing the quiz!\nYou got a score of {score}.")