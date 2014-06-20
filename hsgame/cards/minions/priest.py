import hsgame.targeting
from hsgame.constants import CHARACTER_CLASS, CARD_RARITY
from hsgame.game_objects import MinionCard, Minion
from hsgame.cards.battlecries import take_control_of_minion

__author__ = 'Daniel'


class AuchenaiSoulpriest(MinionCard):
    def __init__(self):
        super().__init__("Auchenai Soulpriest", 4, CHARACTER_CLASS.PRIEST, CARD_RARITY.RARE)

    def create_minion(self, player):
        def remove_heal_does_damage():
            player.heal_does_damage = False

            # If another Auchenai Soulpriest is alive and not silenced, keep heal_does_damage as True
            for m in player.minions:
                if m.card.name == "Auchenai Soulpriest" and m.silence == False and m is not minion:
                    player.heal_does_damage = True
        
        def silence():
            remove_heal_does_damage()
            
        def die(by):
            remove_heal_does_damage()
        
        minion = Minion(3, 5)
        minion.bind("died", die)
        minion.bind_once("silenced", silence)
        player.heal_does_damage = True
        return minion


class CabalShadowPriest(MinionCard):
    def __init__(self):
        super().__init__("Cabal Shadow Priest", 6, CHARACTER_CLASS.PRIEST, CARD_RARITY.EPIC, hsgame.targeting.find_enemy_minion_battlecry_target, lambda target: target.attack_power <= 2 and target.spell_targetable())

    def create_minion(self, player):
        return Minion(4, 5, battlecry=take_control_of_minion)


class Lightspawn(MinionCard):
    def __init__(self):
        super().__init__("Lightspawn", 4, CHARACTER_CLASS.PRIEST, CARD_RARITY.COMMON)

    def create_minion(self, player):
        def attack_equal_to_health():
            minion.increase_attack(minion.health - minion.attack_power)
                
        minion = Minion(0, 5)
        minion.increase_attack(minion.health - minion.attack_power)
        minion.bind("health_impact", attack_equal_to_health)
        minion.bind_once("silenced", lambda: minion.unbind("health_impact", attack_equal_to_health))
        return minion


class Lightwell(MinionCard):
    def __init__(self):
        super().__init__("Lightwell", 2, CHARACTER_CLASS.PRIEST, CARD_RARITY.RARE)

    def create_minion(self, player):
        def heal_damaged_friendly_character():
            targets = hsgame.targeting.find_friendly_spell_target(player.game, lambda character: character.health != character.max_health)
            if len(targets) != 0:
                targets[player.game.random(0, len(targets) - 1)].heal(player.effective_heal_power(3), minion)
        
        minion = Minion(0, 5)
        player.bind("turn_started", heal_damaged_friendly_character)
        minion.bind_once("silenced", lambda: player.unbind("turn_started", heal_damaged_friendly_character))
        return minion
    
    
class NorthshireCleric(MinionCard):
    def __init__(self):
        super().__init__("Northshire Cleric", 1, CHARACTER_CLASS.PRIEST, CARD_RARITY.FREE)

    def create_minion(self, player):
        def draw_card():
            player.draw()
        
        minion = Minion(1, 3)
        player.game.bind("minion_healed", draw_card)
        minion.bind_once("silenced", lambda: player.game.unbind("minion_healed", draw_card))
        return minion