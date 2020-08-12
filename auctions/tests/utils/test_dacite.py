import logging

from dataclasses import dataclass
from dacite import from_dict


logger = logging.getLogger()

def test_from_dict():
    @dataclass
    class InputDto():
        name: str
        age: int

    input_dto= from_dict(InputDto, {
        'name': 'Jay Kim',
        'age': 100,
        'job': 'Engineer'
    })

    logger.info(input_dto)
