import pytest
from unittest.mock import patch
from unittest.mock import Mock

from praktikum.bun import Bun

class TestBun:
    def test_get_bun_input_black_bun_returns_black_bun_text(self, create_bun):
        assert create_bun.get_name() == 'black bun'

    def test_get_price_returns_type_str(self, create_bun):
        assert create_bun.get_price() == 100