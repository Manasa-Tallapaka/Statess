
import pytest
from States.states import states


def test_States_info():
    states = states("Generic states", "location")
    assert states.get_info() == "Generic states states covers location."




