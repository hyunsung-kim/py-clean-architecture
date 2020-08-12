import json
from typing import List
from dataclasses import dataclass

from auctions.domain.entities.bid import Bid
from auctions.domain.value_objects.money import Money


class Auction:
    def __init__(self, id: int, title: str, initial_price: Money, bids: List[Bid]):
        assert isinstance(initial_price, Money)
        self.id = id
        self.title = title
        self.initial_price = initial_price
        self.bids = sorted(bids, key=lambda bid: bid.amount)
        self.withdrawn_bids_ids = []

    def make_a_bid(self, bid: Bid):
        if bid.amout > self.current_price:
            self.bids.append(bid)

    @property
    def current_price(self) -> Money:
        if not self.bids:
            return self.initial_price
        else:
            return self._highest_bid.amout

    @property
    def winners(self):
        if not self.bids:
            return []
        return [ self._highest_bid.bidder_id]

    @property
    def _highest_bid(self) -> Bid:
        return self.bids[-1]

    def withdraw_bid(self, bids_ids: List[int]):
        self.bids = [bid for bid in self.bids if bid.id not in bids_ids]
        self.withdrawn_bids_ids.extend(bids_ids)

    def __repr__(self):
        return json.dumps({
            'id': self.id,
            'title': self.title
        })

