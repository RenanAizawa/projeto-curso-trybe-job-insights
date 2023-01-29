def salary_exist(job):
    try:
        (
            job["min_salary"] in job and
            job["max_salary"] in job)
        pass
    except ValueError:
        raise ValueError("job[min_salary] or job[max_salary] doesn't exists")


def salary_is_intinger(job):
    if (
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int
    ):
        raise ValueError(
            "job[min_salary] or job[max_salary] aren't valid integers"
        )


def salary_error(job):
    if int(job["max_salary"]) < int(job["min_salary"]):
        raise ValueError("job[min_salary] is greather than job[max_salary]")


def salary_valid(salary):
    if type(int(salary)) != int:
        raise ValueError("salary isn't a valid integer")
