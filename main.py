import random

class User:

#конструктор
    def __init__(self, name, money):
        self.name = name
        self.money = int(money)

#играть в казино
    def play(self, idMachine, money, admin, *superusers):
        superuser = list(*superusers)
        machines[idMachine].number = machines[idMachine].number + money
        superuser[admin].money = superuser[admin].money - money
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)
        print(num1, num2, num3)
        if num1 == num2 == num3:
            superuser[admin].money = superuser[admin].money + money * 3
            machines[idMachine].number = machines[idMachine].number - money
            print('\nПЕРЕМОГА, ваш баланс = ', superuser[admin].money)
            if machines[idMachine].number <= 0 : print('Автомат під ID: ', idMachine, ' більше не працює'); del machines[idMachine]
        elif num1 == num2 or num1 == num3 or num2 == num3:
            superuser[admin].money = superuser[admin].money + money * 2
            machines[idMachine].number = machines[idMachine].number - money
            print('\nПЕРЕМОГА, ваш баланс = ', superuser[admin].money)
            if machines[idMachine].number <= 0 : print('Автомат під ID: ', idMachine, ' більше не працює'); del machines[idMachine]
        else: print('\nПОРАЗКА, ваш баланс = ', superuser[admin].money)
        return superuser

class SuperUser(User):

#зібрати гроші з казино
    def MoneyOfCasino(self, admin, idcasino):
        i = 0
        money = 0
        while i < len(machines):
            if machines[i].admin == admin and machines[i].keycasino == idcasino:
                money = money + machines[i].number
                machines[i].number = 0
            i = i + 1
        superusers[admin].money = superusers[admin].money + money
        print('Гроші з казино під назвою: ', casino[idcasino].name, ' списані\nБаланс SuperUser ', superusers[admin].name, ' - ', superusers[admin].money)

#видалення ігрового автомату
    def DelGameMachine(self, idmachine, idcasino, *SuperMachines):
        SuperMachine = list(*SuperMachines)
        money = machines[idmachine].number // (len(SuperMachine) - 1)
        i = 0
        while i < len(machines):
            if machines[i].keycasino == idcasino:
                machines[i].number = machines[i].number + money
            i = i + 1
        del machines[idmachine]
        print('Машина видалена')



class Casino:

    def __init__(self, name, admin):
        self.name = name
        self.admin = int(admin)


class GameMachine:

    def __init__(self, number, admin, casino):
        self.number = number
        self.admin = int(admin)
        self.keycasino = int(casino)



#створення User
def CreateUser(*users):
    user = list(*users)
    name = input('Введіть Nick нового User: ')
    money = int(input('Введіть початкову суму грошей User: '))
    if money <= 1:
        print('Неправильне введення, спробуйте ще раз'); TerminalForUser(user)
    else:
        user.append(User(name, money)); print('\nНовий User СТВОРЕН') ;TerminalForUser(user)

#печать юзеров
def SealUser(*users):
    user = list(*users)
    a = 0
    while a < len(user):
        print('ID:', a, ' Nick User: ',user[a].name, ' Кількість грошей: ',user[a].money)
        a = a + 1
    TerminalForUser(user)

def CreateSuperUser(*superusers):
    superuser = list(*superusers)
    name = input('Введіть Nick SuperUser: ')
    money = int(input('Введіть початкову суму грошей SuperUser: '))
    if money <= 1:
        print('Неправильне введення, спробуйте ще раз'); TerminalForSuper(superuser)
    else:
        superuser.append(SuperUser(name, money)); print('\nНовий SuperUser СТВОРЕН') ;TerminalForSuper(superuser)

def SealSuperUser(*superusers):
    superuser = list(*superusers)
    a = 0
    while a < len(superuser):
        print('ID: ', a, ' Nick: ',superuser[a].name, ' Кількість грошей: ', superuser[a].money)
        a = a + 1
    TerminalForSuper(superuser)


def ChangeSuperUser():
    admin = int(input('\nВиберіть SuperUser за допогомогою його id - '))
    return admin

def createCasino(*superusers):
    superuser = list(*superusers)
    admin = ChangeSuperUser()
    name = 'LA'
    CreateCasino(name, admin)
    print('\nСТВОРЕНО КАЗИНО')
    TerminalForSuper(superuser)

def ChangeCasino():
    casino = int(input('\nВиберіть КАЗИНО за допогомогою його id - '))
    return casino


def createMachine(*superusers):
    superuser = list(*superusers)
    admin = ChangeSuperUser()
    casino = ChangeCasino()
    number = int(input('Введіть стартову сумм до автомату: '))
    money = superuser[admin].money
    superuser[admin].money = superuser[admin].money - number
    if superuser[admin].money < 0: print('Недостатньо коштів'); superuser[admin].money = money; TerminalForSuper(superuser)
    else:
        CreateGameMachine(number, admin, casino)
        print('СТВОРЕН АВТОМАТ')
        TerminalForSuper(superuser)



def TerminalForUser(*users):
    user = list(*users)
    a = int(input('\nСтворити нового USER - 1 \nПереглянути усіх Users - 2 \nPLAY - 3\n'))
    if a == 1:
        CreateUser(user)
    elif a == 2:
        SealUser(user)
    elif a == 3:
        PlayMachineUser(user)
    else: print('Неправильне введення, спробуйте ще раз'); TerminalForUser(user)


def ChangeUser():
    admin = int(input('\nВыберіть User за допогомогою його id - '))
    return admin

def PlayMachineUser(*users):
    user = list(*users)
    iduser = ChangeUser()
    print('Доступні автомати для гри:')
    i = 0
    while i < len(machines):
        print('Id: ', i, ' Кількість грошей в автоматі: ', machines[i].number)
        i = i + 1
    idmachine = int(input('Оберіть автомат за допомогою його Id - '))
    money = int(input('Введіть кількість грошей до автомату: '))
    safemoney = user[iduser].money
    user[iduser].money = user[iduser].money - money
    if user[iduser].money < 1: print('\nНедостатньо коштів'); user[iduser].money = safemoney; TerminalForUser(user)
    else:
        machines[idmachine].number = machines[idmachine].number + money
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)
        print(num1, num2, num3)
        if num1 == num2 == num3:
            user[iduser].money = user[iduser].money + money * 3
            machines[idmachine].number = machines[idmachine].number - money
            print('Вы выиграли, ваш баланс = ', user[iduser].money)
            if machines[idmachine].number <= 0 : print('Автомат під ID: ', idmachine, ' більше не працює'); del machines[idmachine]; TerminalForUser(user)
        elif num1 == num2 or num1 == num3 or num2 == num3:
            user[iduser].money = user[iduser].money + money * 2
            machines[idmachine].number = machines[idmachine].number - money
            print('Вы выиграли, ваш баланс = ', user[iduser].money)
            if machines[idmachine].number <= 0 : print('Автомат під ID: ', idmachine, ' більше не працює'); del machines[idmachine]; TerminalForUser(user)
        else:
            print('Вы проиграли, ваш баланс = ', user[iduser].money)
        TerminalForUser(user)


def TerminalForSuper(*superusers):
    superuser = list(*superusers)
    a = int(input('\nСтворити SuperUser - 1 \nПереглянути усіх SuperUser - 2 \nСтворити нове казино - 3 \nСтворити нову машину - 4 \nПереглянути КАЗИНО - 5\nПереглянути машини - 6\nPLAY - 7 \nЗабрати гроші з казино - 8\nВидалити автомат - 9\n\nВведіть цифру потрібної Вам команди -  '))
    if a == 1:
        CreateSuperUser(superuser)
    elif a == 2:
        SealSuperUser(superuser)
    elif a == 3:
        createCasino(superuser)
    elif a == 4:
        createMachine(superuser)
    elif a == 5:
        printCasino(superuser)
    elif a == 6:
        printMachine(superuser)
    elif a == 7:
        PlayMachine(superuser)
    elif a == 8:
        TakeMoney(superuser)
    elif a == 9:
        DelMachine(superuser)
    else: print('Неправильне введення, спробуйте ще раз'); TerminalForSuper(superuser)


def DelMachine(*superusers):
    superuser = list(*superusers)
    admin = ChangeSuperUser()
    idcasino = ChangeCasino()
    i = 0
    SuperMachines = []
    print('Всі ваші автомати:')
    while i < len(machines):
        if machines[i].keycasino == idcasino:
            print('ID: ', i, ' Кількість грошей: ', machines[i].number)
            SuperMachines.append(machines[i])
            i = i + 1
        else: i = i + 1
    idmachine = int(input('Оберіть id автомату, який хочете видалити - '))
    superuser[admin].DelGameMachine(idmachine, idcasino, SuperMachines)
    TerminalForSuper(superuser)


def TakeMoney(*superusers):
    superuser =  list(*superusers)
    admin = ChangeSuperUser()
    idcasino = ChangeCasino()
    superuser[admin].MoneyOfCasino(admin, idcasino)
    TerminalForSuper(superuser)

#створення нового казино
def CreateCasino(name, admin):
    casino.append(Casino(name, admin))

#створення нової GameMachine
def CreateGameMachine(number, admin, casino):
    machines.append(GameMachine(number, admin, casino))

def printCasino(*superusers):
    superuser = list(*superusers)
    admin = ChangeSuperUser()
    i = 0
    while i < len(casino):
        if casino[i].admin == admin:
            print('ID: ', i, ' Назва казино: ',casino[i].name, ' ID Власника ' ,casino[i].admin)
            i = i + 1
        else: i = i + 1
    TerminalForSuper(superuser)


def printMachine(*superusers):
    superuser = list(*superusers)
    admin = ChangeSuperUser()
    casino = ChangeCasino()
    i = 0
    while i < len(machines):
        if machines[i].admin == admin and machines[i].keycasino == casino:
            print('ID: ', i, ' ID Власника казино: ',machines[i].admin, ' Номер казино: ',machines[i].keycasino, ' Кількіть грошей в автоматі: ', machines[i].number)
            i = i + 1
        else: i = i + 1
    TerminalForSuper(superuser)

def PlayMachine(*superusers):
    superuser = list(*superusers)
    admin = ChangeSuperUser()
    i = 0
    print('\nДоступні автомати(оберіть один з них за допомогою id):')
    while i < len(machines):
        print('ID: ',i, 'ID Власника казино: ' ,machines[i].admin, ' Номер казино: ',machines[i].keycasino, ' Кількість грошей в автоматі:  ' ,machines[i].number)
        i = i + 1
    idMachine = int(input('id обраного автомату: '))
    money = int(input('Введіть кількість грошей до автомату: '))
    safemoney = superuser[admin].money
    superuser[admin].money = superuser[admin].money - money
    if superuser[admin].money < 1: print('\nНедостатньо коштів'); superuser[admin].money = safemoney; TerminalForSuper(superuser)
    else:
        superuser[admin].money = safemoney
        superuser = list(superuser[admin].play(idMachine, money, admin, superuser))
        TerminalForSuper(superuser)


users = []
users.append(User('Maxim', '100'))

superusers = []
superusers.append(SuperUser('King', '30000'))

casino = []
casino.append(Casino('LA', '0'))
machines = []
machines.append(GameMachine(1000, 0, 0))

a = int(input('Ви User чи SuperUser?\nUser - 1\nSuperUser - 2\n\nВідповідь: '))
if a == 1:
    TerminalForUser(users)
    #break
if a == 2:
    TerminalForSuper(superusers)
    #break
else: print('Неправильне введення, до побачення')