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
                 "Nameless One’s master?\nA) Otanewainuku  B) Manunui  "
                 "C) Maui  D) Maungatautari  E) Omanawa ", 
                 "2. What was the name of the beautiful mountain the "
                 "Nameless One was in love with?\nA) Waipuna  B) Hinewai  "
                 "C) Karewa  D) Puwhenua  E) Matarangi", 
                 "3. Why was the Nameless One sad?\n"
                 "A) The trees on him were dying  B) Otanewainuku was leaving  "
                 "C) Puwhenua did not love him  "
                 "D) The Moa were being hunted to extinction  E) He had no name"
                 , "4. Who helped the nameless mountain?\nA) Forest birds  "
                 "B) Otanewainuku and Puwhenua  C) The rivers  "
                 "D) Tane Mahuta and Papatuanuku  E) Patupaiarehe", 
                 "5. How did the Patupaiarehe get the nameless mountain"
                 "to the entrance of Tauranga Moana?\nA) Magic  B) Carried him "
                 " C) Using harakeke ropes  D) Gave him legs  "
                 "E) Dug a path to push him down "
                 ]
qanda_dict = {'1': 'A'}