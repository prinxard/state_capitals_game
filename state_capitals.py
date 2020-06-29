
import csv
import random
with open('african_countries.csv', 'r') as csvfile:
    capital_states = csv.reader(csvfile)
    states_and_caps = list(capital_states)
    random.shuffle(states_and_caps)
    score = 0
    for i in range(10):
        if '*' in states_and_caps[i][1]:
            capital = states_and_caps[i][1].split('*')
            capital = [state.lower() for state in capital]
            print(f"What is the capital of {states_and_caps[i][0]}")
            answer = input().lower()
            if answer == states_and_caps[i][1].lower().strip() or answer == capital[0].strip() or answer == capital[1].strip() or answer == capital[2].strip():
              print(f"{answer} is correct")
              score+=1
            elif (answer != states_and_caps[i][1].lower().strip()):
              print(
              f"{answer} is Wrong, the correct answer is { states_and_caps[i][1]}")
            else:
              print(f'Your score is {score}')
        else:
          print(f"What is the capital of {states_and_caps[i][0]}")
          answer = input().lower()
          if answer == states_and_caps[i][1].lower().strip():
              print(f"{answer} is correct")
              score += 1
          elif (answer != states_and_caps[i][1].lower().strip()):
            print(f"{answer} is Wrong, the correct answer is { states_and_caps[i][1]}")
    else:
      print(f'Your score is {score}')
       
          



# import random
# import csv
# with open('african_countries.csv', 'r') as csvfile:
#     capital_states = csv.reader(csvfile)
    # random.shuffle(capital_states)
    # caps_state = list(capital_states)
    # random.shuffle(caps_state)

    # for cap in capital_states:
    #     if '*' in cap[1]:
    #         cap[1] = cap[1].split('*')
    #         cap[1] = [capital.lower().strip() for capital in cap[1]]
    #     else:
    #         cap[1] = cap[1].lower().strip()

    #     print(f'what is the capital of {cap[0]}')
    #     answer = input().lower()
    #     if answer != '' and answer in cap[1]:
    #         print(f'{answer} is correct')
    #     else:
    #         print('wrong')
