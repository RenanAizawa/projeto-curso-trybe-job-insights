from src.pre_built.counter import count_ocurrences


def test_counter():
    data = count_ocurrences("data/jobs.csv", "salary")
    print("data >>>>>>>>", data)
    assert type(data) == int
    assert data >= 0
    assert data == 324
