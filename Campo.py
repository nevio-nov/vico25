import random
import time

class Campo:
    def __init__(self, n, navi):
        self.navi = navi
        self.matr = []
        self.ematr = []
        self.cnavi = []
        for i in range(n):
            self.matr.append([])
            self.ematr.append([])
            for j in range(n):
                self.matr[i].append('0')
                self.ematr[i].append('0')

    def popola_rand(self):
        for nave in self.navi:
            allEmpty = False
            x = 0
            y = 0
            z = ''
            while not allEmpty:
                allEmpty = True
                x = random.randint(0, len(self.matr) - 1)
                y = random.randint(0, len(self.matr) - 1)
                z = random.choice(["down", "right"])
                if z == "down":
                    if self.can_go_down(x, y, nave):
                        break
                    elif self.can_go_right(x, y, nave):
                        z = "right"
                        break
                    else:
                        allEmpty = False
                else:
                    if self.can_go_right(x, y, nave):
                        break
                    elif self.can_go_down(x, y, nave):
                        z = "down"
                        break
                    else:
                        allEmpty = False
            self.place(x, y, z, nave)

    def printcampo(self):
        for i in range(len(self.matr)):
            s = ''
            for j in range(len(self.matr)):
                s += ' ' + str(self.matr[i][j]) + ' '
            print(s)

    def can_go_down(self, x, y, nave):
        if y + nave <= len(self.matr):
            for i in range(nave):
                if self.matr[y + i][x] == 'X':
                    return False
        else:
            return False
        return True

    def can_go_right(self, x, y, nave):
        if x + nave <= len(self.matr):
            for i in range(nave):
                if self.matr[y][x + i] == 'X':
                    return False
        else:
            return False
        return True

    def place(self, x, y, z, nave):
        coordinate = []
        if z == "down":
            for i in range(nave):
                self.matr[y + i][x] = 'X'
                coordinate.append((y + i, x))
        else:
            for i in range(nave):
                self.matr[y][x + i] = 'X'
                coordinate.append((y, x + i))
        self.cnavi.append(coordinate)


    def printecampo(self):
        s = '   '
        for i in range(len(self.ematr)):
            s += ' ' + str(i) + ' '
        print(s)
        print('  ' + '-'*(len(s)-3))
        for i in range(len(self.ematr)):
            s = str(i) + ' |'
            for j in range(len(self.ematr)):
                s += ' ' + str(self.ematr[i][j]) + ' '
            print(s)

    def check_win(self):
        s = 0
        for raw in self.ematr:
            for elem in raw:
                if elem == 'X':
                    s += 1
        sn = 0
        for elem in self.navi:
            sn += elem
        if s >= sn:
            return True
        return False

def playerturn(campi):
    campi[0].printecampo()
    sparoyx = input("sparo alle coordinate: ")
    y = int(sparoyx[0])
    x = int(sparoyx[1])
    while campi[0].ematr[y][x] != '0':
        sparoyx = input("sparo alle coordinate: ")
        y = int(sparoyx[0])
        x = int(sparoyx[1])
    if campi[1].matr[y][x] == 'X':
        distrutta = False
        for nave in campi[1].cnavi:
            if (y, x) in nave:
                nave.remove((y, x))
                if len(nave) == 0:
                    distrutta = True
                break
        if distrutta:
            print("SHIP DOWN!")
        else:
            print("HIT!")
        campi[0].ematr[y][x] = 'X'
    else:
        print("water...")
        campi[0].ematr[y][x] = '-'
    time.sleep(1)


def botturn(campi):
    campi[1].printecampo()
    y = random.randint(0, len(campi[1].matr) - 1)
    x = random.randint(0, len(campi[1].matr) - 1)
    while campi[1].ematr[y][x] != '0':
        y = random.randint(0, len(campi[1].matr) - 1)
        x = random.randint(0, len(campi[1].matr) - 1)
    print("sparo alle coordinate:", y, x)
    time.sleep(1)
    if campi[0].matr[y][x] == 'X':
        distrutta = False
        for nave in campi[0].cnavi:
            if (y, x) in nave:
                nave.remove((y, x))
                if len(nave) == 0:
                    distrutta = True
                break
        if distrutta:
            print("SHIP DOWN!")
        else:
            print("HIT!")
        campi[1].ematr[y][x] = 'X'
    else:
        print("water...")
        campi[1].ematr[y][x] = '-'
    time.sleep(1)


def vs_bot(n, navi):
    player = random.randint(0, 1) #0 player, 1 bot
    campi = [Campo(n, navi), Campo(n, navi)]
    campi[0].popola_rand()
    campi[1].popola_rand()


    while True:
        print('turn of player', player)
        if player == 0:
            playerturn(campi)
        else:
            botturn(campi)
        if campi[player].check_win():
            print('player', player, 'won!')
            break
        player = (player + 1) % 2
