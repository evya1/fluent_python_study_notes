"""Chapter 1 - The Python Data Model"""
from collections import namedtuple
from random import choice

prompt = ">>> "  # Constant representing the prompt style for printing examples or demonstrations
Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        Returns the number of cards in the deck.

        This method enables the use of the len() function on a FrenchDeck instance.
        If this method is not defined, attempting to use len() on a FrenchDeck instance
        will raise a TypeError.

        Returns:
            int: The number of cards in the deck.
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        Returns the card at the specified position in the deck.

        This method enables the subscript notation ([]) to access individual cards
        in the deck.
        If this method is not defined, attempting to use subscript
        notation on a FrenchDeck instance will raise a 'TypeError'.

        'subscriptable' is the ability of an object to be accessed using square brackets ([]).
        In Python, objects that support the __getitem__ method are said to be subscriptable
        because they can be accessed using this notation.
        Lists, tuples, dictionaries, and certain custom classes are examples of subscriptable objects

        Args:
            position (int): The index of the card to retrieve.

        Returns:
            Card: The card at the specified position in the deck.
        """
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)  # for sorting purposes


def spades_high(input_card: Card) -> int:
    rank_value = FrenchDeck.ranks.index(input_card.rank)
    return rank_value * len(suit_values) + suit_values[input_card.suit]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    second_beer_card = Card('A', 'diamonds')
    print(f"{prompt}{beer_card = }")
    print(f"{prompt}{beer_card.rank = }")
    print(f"{prompt}{second_beer_card.rank = }")
    print()
    deck = FrenchDeck()
    deck[-1]
    print(f"{prompt}{len(deck) = }")
    print(f"{prompt}{deck[0] = }\n"
          f"{prompt}{deck[-1] = }")

    print()
    print("thanks to the implementation of '__getitem__'\n"
          "we don't need to implement a specific method to get a random item from a sequence:")
    print(f"{prompt}{choice(deck) = }")
    print(f"{prompt}{choice(deck) = }")

    print("\nSo far we have just seen 2 advantages of using special methods "
          "to leverage the Python Data Model")
    print("\n1:\tUsers of our class don't need to memorize arbitrary method names or standard operations."
          "\n\tlike, for example: How to get the number of items? by using '.size()' or '.length()' or what?!")
    print("\n2:\tIt's easier to benefit from the rich Python standard library and avoid reinventing the wheel,"
          "\n\tlike the 'random.choice' function")
    print()
    print("By defining the `__getitem__` method in our class,\n"
          "any instance of our custom class enables us to use square brackets (`[]`) for\n"
          "-1: accessing individual cards\n"
          "-2: enables slicing operations.\n"
          "-3: making deck iterable\n"
          "Examples:")
    print("\n-2- Slicing:")
    print(f"{prompt}{deck[:3] = }")
    print(f'{prompt}{deck[12::13] = }')
    print("\n-3a- deck as iterable:")
    for card in deck[:5]:
        print(card)
    print()
    print("-3b- iterate in reverse order:")
    for card in reversed(deck):
        print(card)
        break
    print()
    print(f"Card('Q', 'spades') in deck? {Card('Q', 'spades') in deck}")
    print(f"Card('Q', 'beasts') in deck? {Card('Q', 'beasts') in deck}")
    print()
    print(f"{suit_values = }\n")
    print()
    print("sorted order:")
    for card in sorted(deck, key=spades_high)[:5]:
        print(card)

