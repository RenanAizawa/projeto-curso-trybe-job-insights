import pytest


def salary_exist(job):
    with pytest.raises(ValueError):
        if job["min_salary"] and job["max_salary"]:
            return False
        else:
            return True
