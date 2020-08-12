import json

import dacite
import inject


class PlacingBidPresenter(placing_bid.PlacingBidOutputBoundary):
    def present(self, output_dto: placing_bid.PlacingBidOutputDto) -> None:
        # in a textbook example of the Clean Architecture this method would cause HttpResponse to be sent to a client.
        # However, we are in Django.
        self._data = {
            'is_winner': output_dto.is_winner,
            'current_price': str(output_dto.current_price)
        }

    def get_http_response_msg(self):
        if self._data['is_winner']:
            return f'Congratulations! You are a winner! :) Current price is {self._data["current_price"]}'
        else:
            return f'Unfortunately, you are not winning. :( Current price is {self._data["current_price"]}'


def make_a_bid(request, auction_id: int):
    data = json.loads(request.body)
    input_dto = dacite.from_dict(placing_bid.PlacingBidInputDto, {
        'bidder_id': request.user.id,
        'auction_id': auction_id,
        'amount': get_dollars(data['amount'])
    })
    presenter = PlacingBidPresenter()
    uc = placing_bid.PlacingBidUseCase(presenter)
    uc.execute(input_dto)

    return presenter.get_http_response_msg()