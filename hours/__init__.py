import check50
import check50.c


@check50.check()
def exists():
    """hours.c exists"""
    check50.exists("hours.c")


@check50.check(exists)
def compiles():
    """hours.c compiles"""
    check50.c.compile("hours.c", lcs50=True)


@check50.check(compiles)
def sum_3_weeks():
    """hours sums hours over 3 weeks."""
    check_hours(type="T", data=[8, 8, 10], expected="26")


@check50.check(compiles)
def sum_5_weeks():
    """hours sums hours over 5 weeks."""
    check_hours(type="T", data=[5, 5, 6, 7, 8], expected="31")


@check50.check(compiles)
def average_3_weeks():
    """hours averages hours over 3 weeks."""
    check_hours(type="A", data=[8, 9, 10], expected="9")


@check50.check(compiles)
def average_5_weeks():
    """hours averages hours over 4 weeks."""
    check_hours(type="A", data=[8, 8, 8, 6], expected="7.5")


# Helpers
def check_hours(type: str, data: list, expected: str):
    program = check50.run("./hours").stdin(str(len(data)))
    for hours in data:
        program.stdin(str(hours))
    program.stdin(type).stdout(expected)