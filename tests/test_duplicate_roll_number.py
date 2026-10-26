from gradebook import student, GradeBook


def test_duplicate_roll_number_is_rejected():
    book = GradeBook()

    first_student = student("Ali", 101)
    second_student = student("Ahmed", 101)

    assert book.add_student(first_student) is True
    assert book.add_student(second_student) is False

    assert len(book.students) == 1
