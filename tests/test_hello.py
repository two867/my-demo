from src.hello import add
import pytest


cases = [
    (1, 2, 3),
    ('y', 'y', 'yy')
]
@pytest.mark.parametrize('a,b,c', cases)
def test_add(a, b, c):
    assert add(a, b) == c