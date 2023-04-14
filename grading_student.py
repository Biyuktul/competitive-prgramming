#!/usr/bin/python3

def gradingStudents(grades):
    """
    Round the grades of the students according to the following rules:
    - If the difference between the grade and the next multiple of 5 is less than 3,
        round up to the next multiple of 5.
    - If the grade is less than 38, no rounding occurs.

    :param grades: a list of integers representing the grades of the students
    :return: a list of integers representing the rounded grades of the students

    >>> gradingStudents([73, 67, 38, 33])
    [75, 67, 40, 33]
    >>> gradingStudents([44, 41, 39, 38, 37])
    [45, 41, 40, 40, 37]
    """

    rounded_grades = []
    j = 0
    while j < len(grades):
        adder = 1
        while not (grades[j] + adder) % 5 == 0:
            adder += 1

        if (grades[j] + adder) - grades[j] < 3 and grades[j] >= 38:
            rounded_grades.append(grades[j] + adder)
        else:
            rounded_grades.append(grades[j])
        j += 1

    return rounded_grades
