import random
import os.path
import sqlite3 as sq
import re




def print_man(man, answered_byk):
    print(
        rf"""
      _________________
     |                 |
     |                 |
     {man[6]}     HELP ME     |
    {man[3]}{man[4]}{man[5]}      PLEASE!!! |
     {man[2]}                 |
    {man[0]} {man[1]}               /|
    
"""
    )
    for i in answered_byk:
        print(i, end="")
    print("\n")


def hod_korolevy(
    score, qanswer, question, man, delete_chast, answered_byk, player_name
):
    print_man(man, answered_byk)
    while True:
        if len(answered_byk) == len(qanswer) and (not '_' in answered_byk):
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
            f = open("text.txt", "w")
            f.write(str(score) + "\n")
            f.write(question + "\n")
            for i in man:
                f.write(str(i))
            f.write("\n")
            f.write(str(delete_chast) + "\n")
            for i in answered_byk:
                f.write(str(i))
            f.write("\n")
            f.write(player_name + "\n")
            f.write(qanswer)
            f.close()
            print("Сохранение успешно завершено!")
        else:

            if (
                buk in qanswer or buk in qanswer.upper() or buk in qanswer.lower()
            ) and buk not in answered_byk:
                score += 1
                print(f"Absolutely right! Колво ваших очков теперь: {score}")
                buk = buk.lower()
                qanswer = qanswer.lower()
                l = [i for i in range(len(qanswer)) if qanswer[i] == buk]
                for i in l:
                    answered_byk[i] = buk

            else:
                man[delete_chast] = " "
                delete_chast += 1
            print_man(man, answered_byk)
            if delete_chast == 7:
                print("Sorry, you are loser, game END!!!!!!!!")
                break


while True:
    with sq.connect("Saper.db") as con:
        cur = con.cursor()
        idd = random.randrange(1, 5)
        cur.execute(f"SELECT question FROM questionshmm WHERE id = {idd}")
        result = cur.fetchall()
        result = str(result)
        question = re.sub("[\[\](',)]", "", result)
        cur.execute(f"SELECT tanswer FROM questionshmm WHERE id = {idd}")
        result = cur.fetchall()
        result = str(result)
        qanswer = re.sub("[\[\](',)]", "", result)
    print(
        "Do you want to start the new game? y/n However, if you want to load the last save, enter 'load'"
    )
    answer = input()
    if answer == "y":
        answered_byk = []

        #questions_mas = ["who am i", "who are you"]
        man = ["/", "\\", "|", "\\", "|", "/", "O"]
        print("Hello! This is a Hangman!!! What is your name???")
        player_name = input()
        score = 0
        print("Good, Let's start game!")
        delete_chast = 0
        for i in range(0, len(qanswer)):
            answered_byk.append("_")

        print(f"Question: {question}")

        hod_korolevy(
            score, qanswer, question, man, delete_chast, answered_byk, player_name
        )
    elif answer == "load":
        if os.path.isfile("text.txt"):
            f = open("text.txt", "r")
            text = f.read()
            text = text.split("\n")   #сделать перезапись qanswer
            score = int(text[0])
            question = text[1]
            man = list(text[2])
            delete_chast = int(text[3])
            answered_byk = list(text[4])
            player_name = text[5]
            qanswer = text[6]
            print("Загрузка последнего сохранения успешно завершилась!")
            print(f"Игрок: {player_name}. Количество очков: {score} ")
            print(f"Вопрос: {question}")
            hod_korolevy(
                score, qanswer, question, man, delete_chast, answered_byk, player_name
            )
        else:
            print("Sorry, сохранение куда то подевалось, начните новую игру...")
    elif answer == "n":
        break
    else:
        print("Please, enter the correct answer: YES OR BLYAD NO!")
