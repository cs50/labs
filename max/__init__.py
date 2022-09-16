import check50
import check50.c


@check50.check()
def exists():
    """max.c exists"""
    check50.exists("max.c")


@check50.check(exists)
def compiles():
    """max.c compiles"""
    check50.c.compile("max.c", lcs50=True)


@check50.check(compiles)
def simple():
    """Returns 3 from 0, 1, 3"""
    check_max(elements=[0, 1, 3])


@check50.check(compiles)
def negative():
    """Returns 4 from -10, 4, 2"""
    check_max(elements=[-10, 4, 2])


@check50.check(compiles)
def negative_max():
    """Returns -10 from -10, -50, -100"""
    check_max(elements=[-10, -50, -100])


# Helpers
def check_max(elements: list):
    program = check50.run("./max")
    program.stdin(str(len(elements)))
    for number in elements:
        print(program.stdin(str(number)))
    program.stdout(str(max(elements)))