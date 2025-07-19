from cmu01 import calculate_exp

def test_calculate_exp():
    assert calculate_exp(20,1) == 1000
    assert calculate_exp(20,11) == 2000
    assert calculate_exp(1,12) == 1000
    assert calculate_exp(11,12) == 1000
    assert calculate_exp(24,0) == 2000
    assert calculate_exp(13,0) == 1000
    assert calculate_exp(2,12) == 1000
    assert calculate_exp(2,22) == 2000
    assert calculate_exp(120,0) == 10000
    assert calculate_exp(6,62) == 6000
    assert calculate_exp(6,61) == 5000
    assert calculate_exp(1200,0) == 108000
    assert calculate_exp(0, 1) == 0
    assert calculate_exp(0, 12) == 0
    assert calculate_exp(1, 5) == 0
    assert calculate_exp(1, 12) == 1000
    assert calculate_exp(2, 12) == 1000
    assert calculate_exp(1, 120) == 1000
    assert calculate_exp(2, 22) == 2000
    assert calculate_exp(57, 0) == 5000
    assert calculate_exp(120, 0) == 10000
    assert calculate_exp(2, 24) == 2000
    assert calculate_exp(2, 22) == 2000
    assert calculate_exp(1, 11) == 0
    assert calculate_exp(1, 0) == 0
    assert calculate_exp(5,55) == 5000
    assert calculate_exp(0,32) == 0
    assert calculate_exp(55,5) == 5000
    assert calculate_exp(1200,0) == 108000
    assert calculate_exp(11,12) == 1000
    assert calculate_exp(2,12) == 1000
    assert calculate_exp(1,12) == 1000
    assert calculate_exp(2,22) == 2000
    assert calculate_exp(2,100) == 2000
    assert calculate_exp(5,51) == 4000

test_calculate_exp()