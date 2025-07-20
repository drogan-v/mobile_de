from src.euro_rate import EuroRate

def test_euro_rate():
    e = EuroRate()
    res = e.euro_to_ruble()
    assert isinstance(res, float)
