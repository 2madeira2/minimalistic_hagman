import random


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



def hod_korolevy(score,questions,question, man, delete_chast, answered_byk):
    while True:
        if score == len(questions[question]):
            print("Вы выиграли!")
            break
        print("Угадаете букву? Или хотите сохраниться? Тогда введите 'save'")
        while True:
            buk = input()
            if buk == "save":
                break
            else:
                if len(buk) > 1:
                    print("Please enter only 1 bukva!")
                else:
                    break
        if buk == "save":
            f = open('text.txt', 'w')
            f.write(str(score)+'\n')
            f.write(question + '\n')
            f.write(str(man) + '\n')
            f.write(str(delete_chast) + '\n')
            f.write(str(answered_byk) + '\n')
            f.close()
        else:
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







while True:
    print("Do you want to start the new game? y/n However, if you want to load the last save, enter 's'")
    answer = input()
    if answer == "y":
        answered_byk = []
        questions = {"who am i": "dima", "who are you": "pidor"} #сделать общим для всех
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

        hod_korolevy(score, questions, question, man, delete_chast, answered_byk)
    elif answer == "s":
        #f = open("text.txt","r")
        #text = f.read()
        #распарсить сплитом и занести данные
        pass
    elif answer == "n":
        break
    else:
        print("Please, enter the correct answer: YES OR BLYAD NO!")







