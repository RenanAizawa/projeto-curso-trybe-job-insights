from src.pre_built.counter import count_ocurrences


def test_counter():
    data1 = count_ocurrences("data/jobs.csv", "JavaScript")
    data2 = count_ocurrences("data/jobs.csv", "Python")
    print("data >>>>>>>>", data1)
    print("data 2 >>>>>>>", data2)
    assert type(data1) == int
    assert type(data2) == int
    assert data1 >= 0
    assert data2 >= 0
    assert data1 == 122
    assert data2 == 1639
