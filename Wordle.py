from random import randint

import colorama
from colorama import init
from time import sleep

init(autoreset=True)
from colorama import Fore, Back, Style


def dis(a: list = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]):
    for i in range(25):
        print(a[randint(0, 5)] + '[' + slovar_RU[randint(0, 32)] + ']', end=' ')
    print()


cveta = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
with open('Slova_dlya_Wordle.txt', encoding='utf-8') as s:
    slova = []
    for i in s.read().split():
        if i not in slova:
            slova.append(i)
    sec = 1
    slovar_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    dis(cveta)
    print()
    print(Fore.YELLOW + '                                     СЫГРАЕМ В СЛОВА ?')
    print()
    print(Fore.RED + '                                       нажмите ENTER')
    print()
    dis()
    input()
    dis(cveta)
    print()
    print(Fore.CYAN + 'Правила:')
    sleep(sec)
    print()
    print(Fore.LIGHTCYAN_EX + '''Ваша задача за 6 попыток отгадать слово из пяти букв
(В игре присутствуют только существительные ). Для этого  вам
необходимо ввести существительное , игра подскажет вам и  под
светит вам :''')
    print()
    sleep(sec)
    print(
        Back.BLUE + Fore.BLACK + '1)СИНИМ цветом ,буквы , которые есть в загаданном слове , но они стоят на другом месте')
    sleep(sec)
    print(Back.YELLOW + Fore.BLACK + '2)ЖЁЛТЫМ, буквы которые есть в слове и вы угадали на каком месте они стоят')
    sleep(sec)
    print(Back.LIGHTBLACK_EX + Fore.BLACK + '3)СЕРЫМ цветом , если этой буквы нет в загаданном слове')
    sleep(sec)
    print()
    dis(cveta)
    print()
    print(Fore.CYAN + '                                    Желаю вам удачи!')
    print()
    dis(cveta)
    sleep(2)
    print()
    print(Fore.CYAN + '                                        Начнем ?')
    print(Fore.RED + '                                     Нажмите ENTER')
    print()
    dis(cveta)
    input()
    zagadanoe = slova[randint(0,len(slova))]
    bukvi_zagad = {}

    vivod_zagad = [[], [], [], [], []]
    popitki = 6
    vvedenie_slova = []
    set_bukv = []

    while popitki != 0:
        for i in bukvi_zagad.keys():
            bukvi_zagad[i] = 0
        for i in zagadanoe:
            if i not in bukvi_zagad.keys():
                bukvi_zagad[i] = 1
            else:
                bukvi_zagad[i] += 1
        if popitki == 1:
            dis(cveta)
            print()
            print(Back.RED + Fore.BLACK + f' У вас осталась {popitki} попытка')
            print()
            dis(cveta)
        if popitki in [2, 3, 4]:
            dis(cveta)
            print()
            print(Back.LIGHTRED_EX + Fore.BLACK + f'У вас осталось {popitki} попытки')
            print()
            dis(cveta)
        if popitki in [5, 6]:
            dis(cveta)
            print()
            print(Back.GREEN + Fore.BLACK + f' У вас осталось {popitki} попыток ')
            print()
            dis(cveta)
        print(Fore.BLUE + 'Введите слово :')
        vvedenoe_slovo = list(input().lower())
        if len(''.join(vvedenoe_slovo)) < 5:
            print(Fore.RED + '         Слишком короткое слово , ты что забыл что длина должна быть 5 букв ???????')
            print()
            sleep(sec)
            continue
        for j in range(len(vvedenoe_slovo)):
            if vvedenoe_slovo[j] in bukvi_zagad.keys() and vvedenoe_slovo[j] == zagadanoe[j]:
                bukvi_zagad[vvedenoe_slovo[j]] -= 1

        if len(''.join(vvedenoe_slovo)) > 5:
            print(Fore.RED + '         Слишком длинное слово , ты что забыл что длина максимум 5 букв ???????')
            print()
            sleep(sec)
            continue

        if ''.join(vvedenoe_slovo) not in slova:
            print()
            print(Fore.RED+ 'Такого слова нет в моем словаре ! Если хочешь добавить введи "да"')
            dobavlenie_slova_v_slovar = input()
            if dobavlenie_slova_v_slovar == 'да':
                    with open('Slova_dlya_Wordle.txt' , 'a' , encoding='utf-8') as new_slova:
                        new_slova.write(vvedenoe_slovo+'\n')
                    dis()
                    continue
            else:
                dis()
                print(Fore.RED + '                             ТАКОГО СЛОВА НЕТ В МОЕЙ БАЗЕ СЛОВ')
                print(Fore.RED + '                                    ВВЕДИ ДРУГОЕ СЛОВО')
                sleep(sec)
                continue
        print()
        dis(cveta)
        print()
        if ''.join(vvedenoe_slovo) == zagadanoe:
            dis(cveta)
            print()
            print(
                Fore.RED + '===================================================================================================')
            for i in '    УРАААААА ВЫ ПОБЕДИЛИ !!!! ПОЗДРАВЛЯЕМ !!!!':
                print(cveta[randint(0, 5)] + i, end=' ')
            print()
            print(cveta[randint(0, 5)] + '                                      ЭТО БЫЛО СЛОВО :')
            print(
                '                                         ' + Back.LIGHTYELLOW_EX + Fore.BLACK + '  ' + zagadanoe.upper() + '  ')
            print(
                Fore.RED + '===================================================================================================')
            print()
            dis()
            popitki = -1
            break
        if vvedenoe_slovo in vvedenie_slova:
            dis()
            print()
            print(Fore.RED + 'Вы уже вводили такое слово , придется повторить ввод :)')
            print()
            sleep(sec)
            continue

        if vvedenoe_slovo not in vvedenie_slova:
            for i in range(5):
                if vvedenoe_slovo[i] not in set_bukv:
                    set_bukv.append(vvedenoe_slovo[i])
                if zagadanoe.count(vvedenoe_slovo[i]) > 0:
                    if vvedenoe_slovo[i] == zagadanoe[i]:
                        print(Fore.BLACK + Back.YELLOW + '[' + vvedenoe_slovo[i].upper() + ']', end=' ')
                        sleep(1)
                    else:
                        if vvedenoe_slovo[i] in bukvi_zagad.keys():
                            if bukvi_zagad[vvedenoe_slovo[i]] > 0:
                                print(Fore.BLACK + Back.BLUE + '[' + vvedenoe_slovo[i].upper() + ']', end=' ')
                                sleep(1)
                            else:
                                print(Fore.WHITE + Back.LIGHTBLACK_EX + '[' + vvedenoe_slovo[i].upper() + ']', end=' ')
                                sleep(1)

                        else:
                            print(Fore.WHITE + Back.LIGHTBLACK_EX + '[' + vvedenoe_slovo[i].upper() + ']', end=' ')
                            sleep(1)
                else:
                    print(Fore.WHITE + Back.LIGHTBLACK_EX + '[' + vvedenoe_slovo[i].upper() + ']', end=' ')
                    sleep(1)
            set_bukv.sort()
            print()
            print()
            print(Fore.YELLOW + '                         Как думаешь что это за слово ?')
            print(Fore.YELLOW + '         Буквы которые вы уже вводили , подсвечиваются синим цветом:')
            print(
                Fore.LIGHTMAGENTA_EX + '====================================================================================================')
            for i in range(len(slovar_RU)):
                if slovar_RU[i].lower() in set_bukv:
                    print(Back.BLUE+Fore.BLACK+'[' + (slovar_RU[i]) + ']', end=' ')
                else:
                    print(cveta[randint(1, 5)] +'[' +slovar_RU[i] + ']' , end= ' ')
            print()
            print()
            print(
                Fore.LIGHTMAGENTA_EX + '====================================================================================================')
            print()
            vvedenie_slova.append(vvedenoe_slovo)
            popitki -= 1
    if popitki == 0:
        dis()
        print()
        print(Fore.RED + '                             К СОЖАЛЕНИЮ ПОПЫТКИ ЗАКОНЧИЛИСЬ')
        print()
        dis()
        print()
        for i in zagadanoe:
            print(cveta[randint(1, 5)] + '[' + i.upper() + ']', end=' ')
            print()
        print()
        dis()
        print(Fore.YELLOW + '                                    ПОПРОБУЙ ЕЩЕ РАЗ')
        print()
        dis()
