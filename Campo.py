import random


class Campo:
    def __init__(self, n, navi):
        self.navi = navi
        self.matr = []
        for i in range(n):
            self.matr.append([])
            for j in range(n):
                self.matr[i].append('0')

    def popola_rand(self):
        for nave in self.navi:
            allEmpty = False
            x = 0
            y = 0
            z = ''
            while not allEmpty:
                allEmpty = True
                x = random.randint(0, 9)
                y = random.randint(0, 9)
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

    def popola_rand_down(self):
        for nave in self.navi:
            allEmpty = False
            x = 0
            y = 0
            while not allEmpty:
                allEmpty = True
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if y < len(self.matr) - nave:
                    for i in range(nave):
                        if self.matr[y + i][x] == 'X':
                            allEmpty = False
                else:
                    allEmpty = False
            for i in range(nave):
                self.matr[y + i][x] = 'X'

    def printcampo(self):
        for i in range(len(self.matr)):
            s = ''
            for j in range(len(self.matr)):
                s += ' ' + str(self.matr[i][j]) + ' '
            print(s)

    def can_go_down(self, x, y, nave):


    def can_go_right(self, x, y, nave):


    def place(self, x, y, z, nave):

