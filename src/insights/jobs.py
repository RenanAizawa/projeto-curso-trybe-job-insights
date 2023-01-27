import csv
# import json
from functools import lru_cache
from typing import Dict, List

# from src.insights.filters_func import fylter_job_type


@lru_cache
def read(path: str) -> List[Dict]:
    data_changed = []
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        data = csv.DictReader(file)
        for row in data:
            data_changed.append(row)
        return data_changed
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = []
    data = read(path)

    for row in data:
        if row["job_type"] not in jobs:
            jobs.append(row["job_type"])
    return jobs
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    data = list(filter(lambda j: j["job_type"] == job_type, jobs))
    # print("data >>>>>>>>", data)
    return data
    raise NotImplementedError
