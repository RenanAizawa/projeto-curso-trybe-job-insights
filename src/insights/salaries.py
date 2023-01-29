from typing import Dict, List, Union

# from src.insights.filters_func import (salary_error, salary_exist,
#                                        salary_is_intinger, salary_valid)
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    max_salary_str = []
    max_salary_int = []
    data = read(path)
    for row in data:
        if row["max_salary"] not in max_salary_str:
            max_salary_str.append(row["max_salary"])
    for salary in max_salary_str:
        if salary == 'invalid':
            pass
        else:
            max_salary_int.append(int(float(salary.strip() or 0)))
    return max(max_salary_int)
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    min_salary_str = []
    min_salary_int = []
    data = read(path)
    for row in data:
        if row["min_salary"] not in min_salary_str:
            min_salary_str.append(row["min_salary"])
    for salary in min_salary_str:
        if salary == 'invalid' or salary == '':
            pass
        else:
            min_salary_int.append(int(salary))

    return min(min_salary_int)
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        salary_int = int(salary)
        # salary_exist(job)
        # salary_is_intinger(job)
        # salary_error(job)
        # salary_valid(salary)
        # return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except Exception:
        raise ValueError('algo não estava certo')
    if max < min:
        raise ValueError('Error entre max and min')
    return min <= salary_int <= max


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filter_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job=job, salary=salary):
                filter_jobs.append(job)
        except ValueError:
            pass
    return filter_jobs
    raise NotImplementedError
