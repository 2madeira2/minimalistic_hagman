def print_man(man):
    print(rf"""
      _________________
     |                 |
     |                 |
     {man[6]}     HELP ME     |
    {man[3]}{man[4]}{man[5]}      PLEASE!!! |
     {man[2]}                 |
    {man[0]} {man[1]}               /|
    
""")



import random
answered_byk =""
questions = {"who am i": "dima", "who are you": "pidor"}
questions_mas = ["who am i", "who are you"]
man = ["/", "\\", "|", "\\", "|", "/", "O"]
print("Hello! This is a Hangman!!! What is your name???")
player_name = input()
score = 0
print("Good, Let's start game!")
print_man(man)
delete_chast = 0
question = questions_mas[random.randrange(0,len(questions_mas))]
print(f"Question: {question}")
while True:
    if score == len(questions[question]):
        print("Вы выиграли!")
        break
    print("Угадаете букву?")
    while True:
        buk = input()
        if len(buk) > 1:
            print("Please enter only 1 bukva!")
        else:
            break
    if buk in questions[question] and buk not in answered_byk:
        score += 1
        print(f"Absolutely right! Колво ваших очков теперь: {score}")
        answered_byk += buk
    else:
        man[delete_chast] = " "
        delete_chast += 1
    print_man(man)

        #буквы угаданные отмечать