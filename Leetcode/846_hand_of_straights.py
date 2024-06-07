from collections import Counter
from typing import List


"""
Complexity
    Time complexity: O(nlogn)
    Space complexity: O(n)
"""
def isNStraightHand(hand: List[int], groupSize: int) -> bool:
        hand_size = len(hand)
        if hand_size % groupSize != 0:
            # Cant divide into group size group
            return False

        # Create map from cards
        card_counter = Counter(hand)

        # sort to get the cards in order
        hand.sort()

        for card in hand:
            # card is already used up skip it
            if card not in card_counter or card_counter.get(card) == 0:
                continue
            
            # Check if a new group can be created starting from this card
            for num in range(card, card + groupSize):
                if num not in card_counter or card_counter.get(num) <= 0:
                    return False
                card_counter[num] -= 1
                if card_counter.get(num) <= 0:
                    del card_counter[num]

        if len(card_counter) == 0:
            return True

print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(isNStraightHand([1,2,3,4,5], 4))