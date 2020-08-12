import logging

from auctions.domain.entities.auction import Auction
from auctions.domain.value_objects.money import Money
from auctions.domain.value_objects.currency import USD


logger = logging.getLogger()

def test_auction_class():
    money = Money(USD, '100.00')
    auction = Auction(1, '도자기', money, [])
    logger.info(F"{auction}")