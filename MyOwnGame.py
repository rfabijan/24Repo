'''
This is a class for card initializaiton

card deck = card.txt
'''
import random


class Card:

    # rank and type of card, eg: 4h - four heart
    def __init__(self, rank: str, type: str):
        self.rank = rank
        self.type = type

    # print a specific card
    def drawCard(self):
        rank = self.rank.replace("\n", '')
        type = self.type.replace("\n", '')
        return (rank,type)

    def printCard(self):
        print(self.drawCard()[0] + self.drawCard()[1])



'''
Show what is on the table

the tables
'''
class CardTable:
    deck = []
    table = []

    def __init__(self, player):
        self.player = player

    def printTable(self):
        print("Player Name: {}".format(self.player))

    def shuffleList(self):
        random.shuffle(self.deck)

    def printMenu(self):
        print("_"*10, "WELCOME {}".format(self.player), "_"*10)
        print("[1]- Print the pack out")
        print("[2]- Shuffle")
        print("[3]- Deal a card")
        print("[4]- Make a move, last pile onto previous one")
        print("[5]- Make a move, last pile over 2 piles")
        print("[6]- EXIT")

    def printDeck(self):
        for i in self.deck:
            i.printCard()

    def putCard(self):
        self.table.append(self.deck.pop(-1))
        for i in self.table:
            i.printCard()




    def makeSingleMove(self):
        if self.table[-1].rank == self.table[-2].rank or self.table[-1].type == self.table[-2].type:
            self.table[-2] = self.table[-1]
            self.table.pop(-1)

        for i in self.table:
            i.printCard()





# file =open('cards.txt','r')
table1 = CardTable('Robert')

count = 0
r = ""
t = ""
with open('cards2.txt') as f:
    lines = f.readlines()

for i in lines:
    if count == 0:
        r = i
        count += 1
    elif count == 1:
        t = i
        count = 0
        card = Card(r,t)
        table1.deck.append(card)



while True:
    table1.printMenu()
    inp = int(input("Please select an option: "))
    if inp == 1:
        table1.printDeck()
    elif inp == 2:
        table1.shuffleList()
    elif inp == 3:
        table1.putCard()
        # table1.printCardsOnTable()
    elif inp == 4:
        table1.makeSingleMove()
    elif inp == 6:
        print("Thank you so much!")
        break







# print(table1.deck)
# for i in table1.deck:
#     i.printCard()


