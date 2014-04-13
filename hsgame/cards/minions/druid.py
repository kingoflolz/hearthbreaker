import hsgame.targetting
from hsgame.constants import CHARACTER_CLASS, CARD_STATUS, MINION_TYPES
from hsgame.game_objects import MinionCard, Minion, Card

__author__ = 'Daniel'


class KeeperOfTheGrove(MinionCard):
    def __init__(self):
        super().__init__("Keeper of the Grove", 4, CHARACTER_CLASS.DRUID, CARD_STATUS.RARE)

    def create_minion(self, player):

        class Moonfire(Card):
            def __init__(self):
                super().__init__("Moonfire", 0, CHARACTER_CLASS.DRUID, CARD_STATUS.RARE, True, hsgame.targetting.find_minion_spell_target)

            def use(self, player, game):
                target.spell_damage(2, self)

        class Dispel(Card):
            def __init__(self):
                super().__init__("Dispel", 0, CHARACTER_CLASS.DRUID, CARD_STATUS.RARE, True, hsgame.targetting.find_minion_spell_target)

            def use(self, player, game):
                target.silence()

        targets = hsgame.targetting.find_minion_spell_target(player.game)

        if len(targets) > 0:
            target = player.agent.choose_target(targets)
            option = player.agent.choose_option(Moonfire(), Dispel())
            option.use(player, player.game)

        return Minion(2, 4, MINION_TYPES.NONE)
