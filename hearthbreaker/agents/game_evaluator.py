# note all values are experimental

def game_evaluator(player, evaluate_once=False):
    score = 0
    for minion in player.minions:
        minion_score = 0
        minion_score += minion.calculate_attack() * minion.health ** 0.7
        if minion.taunt:
            minion_score += minion.health * 2
        if not minion.can_be_targeted_by_spells:
            minion_score *= 1.5
        score += minion_score
    score += len(player.hand) * 3
    score += player.max_mana * 3
    score += player.hero.health
    if not evaluate_once:
        score -= game_evaluator(player.opponent, True)
    return score
