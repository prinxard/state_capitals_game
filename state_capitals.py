
import csv
import random
with open('african_countries.csv', 'r') as csvfile:
    capital_states = csv.reader(csvfile)
    states_and_caps = list(capital_states)
    random.shuffle(states_and_caps)
    score = 0
    for i in range(10):
        print(f"What is the capital of {states_and_caps[i][0]}")
        answer = input().lower()
        if answer == states_and_caps[i][1].lower().strip():
            print("correct")
            score+=1
        elif (answer != states_and_caps[i][1][:].lower().strip()):
          print('Wrong')
    else:
      print(f'Your score is {score}')

