from typing import Dict, List

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    unique_industries = []
    data = read(path)
    for row in data:
        if row["industry"] not in unique_industries:
            unique_industries.append(row["industry"])
    for name in unique_industries:
        if name == '':
            unique_industries.remove('')
    return unique_industries
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    data = list(filter(lambda ind: ind["industry"] == industry, jobs))
    return data
    raise NotImplementedError
