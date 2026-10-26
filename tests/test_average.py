from gradebook import student

def test_average_with_no_scores():
    s = student("Zunair", 101)
    assert s.average() == 0.0

    