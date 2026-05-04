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
score = 0
question_list = ["1. What was the name of the chief mountain who was the "
                 "Nameless One's master?\n\nA) Otanewainuku  B) Manunui  "
                 "C) Maui  D) Maungatautari  E) Omanawa ", 
                 "2. What was the name of the beautiful mountain the "
                 "Nameless One was in love with?\n\nA) Waipuna  B) Hinewai  "
                 "C) Karewa  D) Puwhenua  E) Matarangi", 
                 "3. Why was the Nameless One sad?\n\n"
                 "A) The trees on him were dying  B) Otanewainuku was leaving  "
                 "C) Puwhenua did not love him  "
                 "D) The Moa were being hunted to extinction  E) He had no name"
                 , "4. Who helped the nameless mountain?\n\nA) Forest birds  "
                 "B) Otanewainuku and Puwhenua  C) The rivers  "
                 "D) Tane Mahuta and Papatuanuku  E) Patupaiarehe", 
                 "5. How did the Patupaiarehe get the nameless mountain"
                 "to the entrance of Tauranga Moana?\n\nA) Magic  B) Carried "
                 "him  C) Using harakeke ropes  D) Gave him legs  "
                 "E) Dug a path to push him down", "6. What stopped the "
                 "Patupaiarehe when they were dragging the Nameless mountain?\n"
                 "\nA) Fatigue  B) The sun rising  C) Evil spirits "
                 "D) The Nameless One's protests  E) Tane Mahuta", "7. What was"
                 " the name given to the mountain at the end of the story?\n\n"
                 "A) Mauao  B) Maui  C) Te Rapuhia  D) Roderick  E) Maungatapu"
                 , "8. What does 'Mauao' mean?\n\nA) 'Lowly one'  "
                 "B) 'Blessed'  C) 'Caught by the Dawn'  "
                 "D) 'Mountain of Sorrow'  E) 'Slave Mountain'"
                 ]

#Because of the range function and the index of question_list, question 1 
#actually becomes question 0 to the code.
qanda_dict = {0: 'A', 1: 'D', 2: 'C', 3: 'E', 4: 'C', 5: 'B', 6: 'A', 7: 'C'}

#Introducing the program and providing instructions for the user.
print("Welcome to the legend of Mauao quiz!!")
print(f"Answer {NUM_OF_QUES} questions based on the Maori Legend of Mauao.")
print("This quiz is multichoice - Enter 'A', 'B', 'C', 'D', 'E' "
      "based on what answer you think is correct.")
print("Good luck!")
#Asking the user the questions.
for quesnum in range(NUM_OF_QUES):
   print(question_list[quesnum])
   try:
      user_answer = input("Answer: ").upper()
      if user_answer == qanda_dict[quesnum]:
         print("Correct")
         score += POINTS_PER_ANS
      else:
         print(f"Incorrect.   The correct answer was {qanda_dict[quesnum]}")
   except:
      print(f"Invalid input. The answer was {qanda_dict[quesnum]}")