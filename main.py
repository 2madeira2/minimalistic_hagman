def print_man(man, answered_byk):
    print(rf"""
      _________________
     |                 |
     |                 |
     {man[6]}     HELP ME     |
    {man[3]}{man[4]}{man[5]}      PLEASE!!! |
     {man[2]}                 |
    {man[0]} {man[1]}               /|
    
""")
    for i in answered_byk:
        print(i,end="")
    print("\n")



import random



while True:
    print("Do you want to start the new game? y/n")
    answer = input()
    if answer == "y":
        answered_byk = []
        questions = {"who am i": "dima", "who are you": "pidor"}
        questions_mas = ["who am i", "who are you"]
        man = ["/", "\\", "|", "\\", "|", "/", "O"]
        print("Hello! This is a Hangman!!! What is your name???")
        player_name = input()
        score = 0
        print("Good, Let's start game!")
        delete_chast = 0
        question = questions_mas[random.randrange(0, len(questions_mas))]
        for i in range(0, len(questions[question])):
            answered_byk.append("_")
        print_man(man, answered_byk)
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
            if (buk in questions[question] or buk in questions[question].upper()) and buk not in answered_byk:
                score += 1
                print(f"Absolutely right! Колво ваших очков теперь: {score}")
                buk = buk.lower()
                answered_byk[questions[question].index(buk)] = buk
            else:
                man[delete_chast] = " "
                delete_chast += 1
            print_man(man, answered_byk)
            if delete_chast == 7:
                print("Sorry, you are loser, game END!!!!!!!!")
                break

    elif answer == "n":
        break
    else:
        print("Please, enter the correct answer: YES OR BLYAD NO!")
