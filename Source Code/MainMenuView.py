import pygame
from GameView import Text, Button, RadioGroup, Radio, Checkbox
import PokerGame as poker
import SolitaireGame
import SnapGame
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 155, 0)
blue = (50, 50, 190)
red = (190, 50, 50)
grey = (100, 100, 100)

display_dimensions = (1100, 800)

pygame.init()

game_display = pygame.display.set_mode(display_dimensions)

pygame.display.set_caption('52 Card Game')

clock = pygame.time.Clock()
FPS = 10

def start_menu():
    title = Text(display_dimensions, (0, -100), "52 Card Game", 50, black)

    solitaire_button = Button(display_dimensions, "Play Solitaire", (0, 0), (100, 50), blue, text_color=white, action="solitaire")
    quit_button = Button(display_dimensions, "Play Snap", (200, 0), (100, 50), red, text_color=white, action="snap")
    poker_button = Button(display_dimensions, "Play Poker", (-200, 0), (100, 50), grey, text_color=white, action="poker")
    buttons = [solitaire_button, quit_button, poker_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SolitaireGame.quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:
                    for button in buttons:
                        if button.check_if_clicked(mouse_pos):
                            if button.action == "solitaire":
                                SolitaireGame.SolitaireGameSetup()
                                SnapGame.SnapGame()
                            elif button.action == "poker":
                                poker.PokerGame()
                                pass
                            else:
                                print("Button action: {} does not exist".format(button.action))

        game_display.fill(green)

        title.display(game_display)

        for button in buttons:
            button.display(game_display, pygame.mouse.get_pos())

        pygame.display.update()
        clock.tick(FPS)


start_menu()
