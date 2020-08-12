from typing import Optional
from dataclasses import dataclass

from auctions.domain.value_objects.money import Money


@dataclass(repr=True)
class Bid:
    def __init__(self, id: Optional[int], bidder_id: int, amount: Money):
        assert isinstance(amount, Money)
        self.id = id
        self.bidder_id = bidder_id
        self.amount = amount
