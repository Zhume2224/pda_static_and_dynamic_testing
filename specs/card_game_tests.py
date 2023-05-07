import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

  def setUp(self):
    self.card1=Card('clubs',1)
    self.card2=Card('diamond',3)
    self.cards=[self.card1,self.card2]

    self.cardgame=CardGame()
    


  def test_card_has_ace(self):
     result=self.cardgame.check_for_ace(self.card1)
     self.assertEqual(True,result)



  def test_there_is_the_highest_card(self):
     result=self.cardgame.highest_card(self.card1,self.card2)
     self.assertEqual(self.card2,result)

  def test_cards_have_total_value(self):
     result=self.cardgame.cards_total(self.cards)
     self.assertEqual("You have a total of 4",result)



