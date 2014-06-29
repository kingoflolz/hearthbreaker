from hsgame.constants import CHARACTER_CLASS, CARD_RARITY
from hsgame.game_objects import MinionCard, Minion

__author__ = 'Daniel'


class AlAkirTheWindlord(MinionCard):
    def __init__(self):
        super().__init__("Al'Akir the Windlord", 8, CHARACTER_CLASS.SHAMAN,
                         CARD_RARITY.LEGENDARY)

    def create_minion(self, player):
        minion = Minion(3, 5)
        minion.wind_fury = True
        minion.charge = True
        minion.divine_shield = True
        minion.taunt = True
        return minion


class DustDevil(MinionCard):
    def __init__(self):
        super().__init__("Dust Devil", 1, CHARACTER_CLASS.SHAMAN,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(3, 1)
        minion.wind_fury = True
        player.overload += 2
        return minion
