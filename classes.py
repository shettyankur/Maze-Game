import pygame
import constants
from pygame import *
from constants import *

pygame.init()


class Game:
    def __init__(self, window):
        self.lines = []
        self.window = window
        self.selectpos = 0

    def home(self):
        # Displays the background of the menu

        self.window.blit(home, (0, 0))
        pygame.display.flip()

    def select(self, level, move=False):
        # Move the arrows according to the key pressed (Up / Down)

        if self.selectpos == 0:
            if move == True:
                self.selectpos = 1
            if level == 1:
                self.home()
                self.window.blit(select1, (0, 0))
            if level == 2:
                self.home()
                self.window.blit(select2, (0, 0))
        else:
            if move == True:
                self.selectpos = 0
            if level == 1:
                self.home()
                self.window.blit(select1b, (0, 0))
            if level == 2:
                self.home()
                self.window.blit(select2b, (0, 0))
        pygame.display.flip()

    def initlevel(self, level):
        # We recover the lines of the level to reuse them

        name = "levels/lev" + str(level)
        with open(name, "r") as file:
            self.lines = file.readlines()
        file.close()
        self.castart = True
        return self.lines

    def level(self, ending=False):
        # The level is generated from the characters in the level file

        self.window.blit(background, (0, 0))
        y = 0
        for line in self.lines:
            x = 0
            for chara in line:
                if chara == "d":
                    self.window.blit(start, (x, y))
                if chara == "w":
                    self.window.blit(brick, (x, y))
                if chara == "a":
                    self.window.blit(end, (x, y))
                x += 30
            y += 30
        if self.castart == True:
            self.window.blit(cadown, (0, 0))
        self.castart = False
        if ending == False:
            pygame.display.flip()


class Donkey:
    def __init__(self, window, level):
        self.window = window
        Gameinst = Game(window)
        self.lines = Game.initlevel(Gameinst, level)
        self.win = 1

    def move(self, direction, pos_donkey):
        if direction == "up":
            if self.lines[(pos_donkey[1] - 30) // 30][pos_donkey[0] // 30] != "w" and (pos_donkey[1] - 30) >= 0:
                pos_donkey[1] -= 30
            self.window.blit(caup, pos_donkey)
        if direction == "down":
            try:
                if self.lines[(pos_donkey[1] + 30) // 30][pos_donkey[0] // 30] != "w" and pos_donkey[1] + 30 <= 420:
                    pos_donkey[1] += 30
            except:
                pass
            self.window.blit(cadown, pos_donkey)
        if direction == "left":
            if self.lines[pos_donkey[1] // 30][(pos_donkey[0] - 30) // 30] != "w" and (pos_donkey[0] - 30) >= 0:
                pos_donkey[0] -= 30
            self.window.blit(caleft, pos_donkey)
        if direction == "right":
            try:
                if self.lines[pos_donkey[1] // 30][(pos_donkey[0] + 30) // 30] != "w" and pos_donkey[0] + 30 <= 420:
                    pos_donkey[0] += 30
            except:
                pass
            self.window.blit(caright, pos_donkey)
        pygame.display.flip()

    def success(self, pos_donkey):
        if self.lines[pos_donkey[1] // 30][pos_donkey[0] // 30] == "a":
            return True

    def winmove(self, pos_donkey):
        if self.win == 1:
            self.window.blit(cawin1, (pos_donkey[0] - 4, pos_donkey[1] - 5))
        if self.win == 2:
            self.window.blit(cawin2, (pos_donkey[0] - 7, pos_donkey[1] - 5))
        if self.win == 3:
            self.window.blit(cawin3, (pos_donkey[0] - 4, pos_donkey[1] - 5))
        if self.win == 4:
            self.window.blit(cawin4, (pos_donkey[0] + 1, pos_donkey[1] - 5))
        self.win += 1
        if self.win == 5:
            self.win = 1
        self.window.blit(success, (0, 0))
        pygame.display.flip()
