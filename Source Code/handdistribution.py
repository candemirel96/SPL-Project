
import pickle
import os
from collections import namedtuple


class HandDistribute:
    def __init__(self, cards, x, y, card_size, pile_type="tableau"):
        self.Order = namedtuple('Order', ['foundation', 'rank', 'color_suit'])
        self.card_width, self.card_height = card_size

        self.pile_type = pile_type
        if self.pile_type == 'tableau':
            self.fanned = True
            self.order = self.Order(foundation='king', rank=-1, color_suit='alt-color')
            self.face_up = 'top'
            self.height = 500
    def pile_bottom(self):
        return self.cards[-1].position[1] + self.card_height

    def update_faces(self):
        if len(self.cards) != 0:
            for index, card in enumerate(self.cards):
                if self.face_up == 'none':
                    card.face_up = False
                elif self.face_up == 'top':
                    if index == len(self.cards) - 1:
                        card.face_up = True
                elif self.face_up == 'all':
                    card.face_up = True

    def update_positions(self):
        if len(self.cards) != 0:
            for index, card in enumerate(self.cards):
                if self.fanned == True:
                    card.position = (self.x, self.y + (index * self.card_spacing))
                else:
                    card.position = (self.x, self.y)

    def updateHand(self):
        self.set_hand()
        self.set_handCardPositions()
def save_settings(settings):
    data = settings

    file_path = os.path.join("game_data", "settings.data")
    file = open(file_path, "wb")

    pickle.dump(data, file)
    file.close()

def load_settings():
    try:
        file_path = os.path.join("game_data", "settings.data")
        file = open(file_path, "rb")
    except FileNotFoundError:
        save_settings(default_settings)
        return default_settings
    else:
        settings = pickle.load(file)
        file.close()
        return settings
