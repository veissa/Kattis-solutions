"""
Jake is learning how to play the card game Dominion. In Dominion, you can buy a variety of treasure, action, and victory point cards – at the end of the game, the player with the most victory points wins!

Each turn, each player draws

cards and can use their action and treasure cards to obtain buying power in order to buy more cards. Since Jake is just starting out, he’s decided to buy only treasure and victory point cards.

There are

kinds of victory cards in Dominion:

    Province (costs 

, worth

victory points)

Duchy (costs
, worth

victory points)

Estate (costs
, worth

    victory point)

And, there are

kinds of treasure cards:

    Gold (costs 

, worth

buying power)

Silver (costs
, worth

buying power)

Copper (costs
, worth

    buying power)

At the start of Jake’s turn, he draws

of these cards. Given the number of Golds, Silvers, and Coppers in Jake’s hand, calculate the best victory card and best treasure card he could buy that turn. Note that Jake can buy only one card.
Input

The input consists of a single test case on a single line, which contains three non-negative integers
, , (

) indicating the number of Golds, Silvers, and Coppers Jake draws in his hand.
Output

Output the best victory card (Province, Duchy, or Estate) and the best treasure card (Gold, Silver, or Copper) Jake can buy this turn, separated with " or ", in this order. If Jake cannot afford any victory cards, output only the best treasure card he can buy.
Sample Explanation

In Sample Input
, Jake has Silver in his hand, which means he has buying power. This would allow him to either buy an Estate or a Copper
"""
def solve():
    g, s, c = map(int, input().split())
    
    # Calculate the total buying power
    buying_power = g * 3 + s * 2 + c
    
    # Determine the best treasure card
    if buying_power >= 6:
        best_treasure = "Gold"
    elif buying_power >= 3:
        best_treasure = "Silver"
    else:
        best_treasure = "Copper"
    
    # Determine the best victory card
    if buying_power >= 8:
        best_victory = "Province"
    elif buying_power >= 5:
        best_victory = "Duchy"
    elif buying_power >= 2:
        best_victory = "Estate"
    else:
        best_victory = None
    
    # Output the result
    if best_victory:
        return f"{best_victory} or {best_treasure}"
    else:
        return best_treasure

# Example usage
print(solve())
