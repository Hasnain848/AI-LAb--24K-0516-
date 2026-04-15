import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]
red_cards = [card for card in deck if card[1] in ['Hearts', 'Diamonds']]
print(f"P(Red Card): {len(red_cards)/len(deck)}")

hearts_in_red = [card for card in red_cards if card[1] == 'Hearts']
print(f"P(Heart | Red): {len(hearts_in_red)/len(red_cards)}")

face_cards = [card for card in deck if card[0] in ['Jack', 'Queen', 'King']]
diamonds_in_face = [card for card in face_cards if card[1] == 'Diamonds']
print(f"P(Diamond | Face): {len(diamonds_in_face)/len(face_cards)}")
spade_or_queen_in_face = [card for card in face_cards if card[1] == 'Spades' or card[0] == 'Queen']
print(f"P(Spade or Queen | Face): {len(spade_or_queen_in_face)/len(face_cards)}")
