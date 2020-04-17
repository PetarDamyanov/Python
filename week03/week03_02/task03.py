import sys


class BowlingGame:
    def __init__(self, lst):
        if len(lst) < 12:
            raise Exeption("Invalid frames number of frames")
        self.lst = lst
        self.score = 0

    def result(self):
        n = len(self.lst) - 1
        if self.lst[n - 2] == 10:
            n = len(self.lst) - 2
        elif (self.lst[n - 1] + self.lst[n - 2]) == 10:
            n = len(self.lst) - 1
        x = 0
        while x < n:
            if self.lst[x] == 10:
                self.score += int(self.lst[x]) + int(self.lst[x + 1]) + int(self.lst[x + 2])
                # x=+1
            elif (self.lst[x] + self.lst[x + 1]) == 10:
                self.score += int(self.lst[x]) + int(self.lst[x + 1]) + int(self.lst[x + 2])
                x += 1
            else:
                self.score += self.lst[x] + self.lst[x + 1]
                x += 1
            x += 1
        return self.score

    def __str__(self):
        return self.score

    def __repr__(self):
        return self.lst


def main():
    arg = sys.argv[1]
    game = BowlingGame(arg)
    print(game.score)


if __name__ == '__main__':
    main()
