from gradebook import student

def test_average_with_no_scores():
    s = student("Zunair", 101)
    assert s.average() == 0.0

def test_average_with_scores():
    s = student("Ali", 102)
    s.score = [70, 80, 90]
    assert s.average() == 80.0