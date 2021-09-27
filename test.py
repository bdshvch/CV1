from toimport import FirstStep
from toimport import SecondStep
from toimport import ThirdStep

def testFirstStep():
    assert FirstStep([0, 0], [1, 1]) == [0.0, 1.0]
    assert FirstStep([0.5, 0.5], [0.5, 0.5]) == [0.5, 0.5]

def testSecondStep():
    assert SecondStep([0.6, 0.4], [0.4, 0.6], [[[1, 0], [0, 1]], [[1, 1], [0, 0]]], 2, [[0, 0], [0, 0]], [[0, 0], [0, 0]], 2) == ([[1.0, 0.4], [0.0, 0.6]], [[1.0, 0.6], [0.0, 0.4]])

def testThirdStep():
    assert ThirdStep([[0.5, 0.5], [0.5, 0.5]], [[0.5, 0.5], [0.5, 0.5]], 1, [0.6, 0.4], [[[1, 0], [0, 0]]], 2) == ([0.6], [0.4])
