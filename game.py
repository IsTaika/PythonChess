import board
import pygame
import os
import time
import interface
import tables
from random import randint

pygame.init()
font = pygame.font.SysFont("Arial", 20)
FONT = pygame.font.Font(None, 32)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


def registration(window):
    run = True
    menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (752, 752))
    window.blit(menu_bg, (0, 0))
    logintext = font.render("Enter name:", 1, (255, 255, 255))
    window.blit(logintext, (50, 50))
    inputlogin = InputBox(50, 100, 50, 30)
    countrytext = font.render("Enter your country: ", 1, (255, 255, 255))
    window.blit(countrytext, (50, 200))
    inputcountry = InputBox(50, 250, 50, 30)
    buttonfin = interface.Button(
        'Register me!',
        (50, 300),
        font=30,
        bg='navy'
    )
    buttonfin.show(window, buttonfin)
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if buttonfin.rect.collidepoint(x, y):
                        if inputlogin != "" and inputcountry != "":
                            tables.registration_table_append(inputlogin.text, inputcountry.text)
                            menu(window)
                        else:
                            warning = font.render("Enter your username and country!", 1, (255, 0, 0))
                            window.blit(warning, (376, 376))

            inputlogin.handle_event(event)
            inputcountry.handle_event(event)
        inputlogin.update()
        inputlogin.draw(window)
        inputcountry.update()
        inputcountry.draw(window)
        pygame.display.update()


def menu(window):
    run = True

    clock = pygame.time.Clock()
    menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (752, 752))
    window.blit(menu_bg, (0, 0))
    inputsecond = InputBox(50, 100, 50, 30)
    secondtext = font.render("Enter your opponent's name:", 1, (255, 255, 255))
    window.blit(secondtext, (50, 50))
    buttonwhite = interface.Button(
        "White",
        (50, 250),
        font=30,
        bg='navy'
    )
    buttonwhite.show(window, buttonwhite)
    buttonblack = interface.Button(
        "Black",
        (150, 250),
        font=30,
        bg='navy'
    )
    buttonblack.show(window, buttonblack)
    turntext = font.render("Select your turn:", 1, (255, 255, 255))
    window.blit(turntext, (50, 200))
    creartor = font.render("by Radmir Khusainov, github rep: https://github.com/IsTaika/PythonChess", 1,
                           (255, 255, 255))
    window.blit(creartor, (10, 700))
    buttonstatic = interface.Button(
        "Statistic",
        (50, 350),
        font=30,
        bg='navy'
    )
    buttonstatic.show(window, buttonstatic)
    pygame.display.update()
    while run:
        fps = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if buttonblack.rect.collidepoint(x, y):
                        if inputsecond.text != "":
                            colortext = font.render("You are black!:", 1, (255, 255, 255))
                            window.blit(colortext, (500, 300))
                            opname = inputsecond.text
                            main(window, 'black', opname)
                        else:
                            warning = font.render("Enter your opponent's name!", 1, (255, 0, 0))
                            window.blit(warning, (30, 400))
                    if buttonwhite.rect.collidepoint(x, y):
                        if inputsecond.text != "":
                            colortext = font.render("You are white!", 1, (255, 255, 255))
                            window.blit(colortext, (500, 300))
                            opname = inputsecond.text
                            main(window, 'white', opname)
                        else:
                            warning = font.render("Enter your opponent's name!", 1, (255, 0, 0))
                            window.blit(warning, (30, 400))
                    if buttonstatic.rect.collidepoint(x, y):
                        if tables.get_games_profile() is not None:
                            statistic_screen(window)
                        else:
                            warning = font.render("You need to play more games!", 1, (255, 0, 0))
                            window.blit(warning, (30, 500))

            inputsecond.handle_event(event)
        inputsecond.update()
        inputsecond.draw(window)
        pygame.display.update()
        pygame.display.flip()


def click(position):
    print(position)
    rez = [94, 94, 752, 752]
    x = position[0]
    y = position[1]
    i, j = 0, 0
    if rez[0] < x < rez[0] + rez[2]:
        i = int(x // (rez[2] / 8))
    if rez[0] < y < rez[0] + rez[3]:
        j = int(y // (rez[3] / 8))
    print(j, ' ', i)
    if -1 < i < 8:
        if -1 < j < 9:
            return j, i


def window_update(window, bo):
    boardimg = pygame.transform.scale(pygame.image.load(os.path.join("img", "board.png")), (752, 752))
    window.blit(boardimg, (0, 0))
    bo.icon(window)
    pygame.display.update()


def main(window, color2, opname):
    run = True
    bo = board.Board(8, 8)
    bo.update_moves()
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        window_update(window, bo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                color = bo.turn
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                print("TEST", i, " ", j, " ", color)
                bo.select(i, j, color)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if bo.turn == 'white':
                        bo.winner = 'black'
                    else:
                        bo.winner = 'white'
        if bo.winner == color2:
            print("Winner = ", bo.winner, ' color = ', color2)
            tables.games_table_append(opname, 'win', bo.amount, bo.text)
            end_screen(window, bo.winner)
        if bo.winner != color2 and bo.winner is not None:
            print("Winner = ", bo.winner, ' color = ', color2)
            tables.games_table_append(opname, 'lose', bo.amount, bo.text)
            end_screen(window, bo.winner)


def end_screen(window, winner):
    run = True
    menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (752, 752))
    window.blit(menu_bg, (0, 0))
    tables.profile_table_change()
    endtext = font.render(winner + " win!",1 , (255, 255, 255))
    window.blit(endtext, (100, 100))
    buttonmenu = interface.Button(
        ("Menu"),
        (100, 200),
        font=30,
        bg='navy'
    )
    buttonmenu.show(window, buttonmenu)
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if buttonmenu.rect.collidepoint(x, y):
                        menu(window)


def statistic_screen(window):
    run = True
    menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (752, 752))
    window.blit(menu_bg, (0, 0))
    name = "Name: " + str(tables.get_name())
    games = "Games: " + str(tables.get_games_profile())
    country = "Country: " + str(tables.get_country_profile())
    wins = "Wins: " + str(tables.get_wins_profile())
    loses = "Loses: " + str(tables.get_loses_profile())
    percent = ""
    if tables.get_precent_profile():
        percent = "Win % :" + str(tables.get_precent_profile())
    txtzagolovok = font.render("Your statistic: ", 1, (255, 255, 255))
    window.blit(txtzagolovok, (50, 50))
    txtname = font.render(name, 1, (255, 255, 255))
    window.blit(txtname, (50, 100))
    txtcountry = font.render(country, 1, (255, 255, 255))
    window.blit(txtcountry, (50, 150))
    txtgames = font.render(games, 1, (255, 255, 255))
    window.blit(txtgames, (50, 200))
    txtwins = font.render(wins, 1, (255, 255, 255))
    window.blit(txtwins, (50, 250))
    txtloses = font.render(loses, 1, (255, 255, 255))
    window.blit(txtloses, (50, 300))
    if percent != "":
        txtpercent = font.render(percent, 1, (255, 255, 255))
        window.blit(txtpercent, (50, 350))
    buttonmenu = interface.Button(
        "Menu",
        (50, 550),
        font=30,
        bg='navy'
    )
    buttonmenu.show(window, buttonmenu)
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if buttonmenu.rect.collidepoint(x, y):
                        menu(window)

def games_show(window, id):
    txt1 = font.render(" ", 1, (255, 255, 255))
    window.blit(txt1, (50, 300))
    txt2 = font.render(" ", 1, (255, 255, 255))
    window.blit(txt2, (50, 400))
    txt3 = font.render(" ", 1, (255, 255, 255))
    window.blit(txt3, (50, 500))
    txt4 = font.render(" ", 1, (255, 255, 255))
    window.blit(txt4, (50, 600))
    txt5 = font.render(" ", 1, (255, 255, 255))
    window.blit(txt5, (50, 700))


def games_screen(window):
    run = True
    menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (752, 752))
    window.blit(menu_bg, (0, 0))
    txt = font.render("Select game: ", 1, (255, 255, 255))
    window.blit(txt, (50, 200))
    inputgame = InputBox(50, 100, 50, 30)
    buttonmenu = interface.Button(
        "Menu",
        (50, 100),
        font=30,
        bg='navy'
    )
    buttonreplay = interface.Button(
        "Watch replay",
        (300, 100),
        font=30,
        bg='navy'
    )
    buttonnext = interface.Button(
        "Show next games",
        (450, 700),
        font=30,
        bg='navy'
    )
    id = tables.get_last_id()
    id1 = 1
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if buttonmenu.rect.collidepoint(x, y):
                        menu(window)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if buttonnext.rect.collidepoint(x, y):
                        games_screen(window)
                        id1
            inputgame.handle_event(event)
    inputgame.update()
    inputgame.draw(window)
    pygame.display.update()
    pygame.display.flip()

rez = [94, 94, 752, 752]
width = 752
height = 752
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python chess")
if tables.table_test():
    menu(window)
    print("MAIN")
else:
    print("ELSE")
    registration(window)
