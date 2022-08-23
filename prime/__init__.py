import check50
import check50.c


@check50.check()
def exists():
    """prime.c exists"""
    check50.exists("prime.c")


@check50.check(exists)
def compiles():
    """prime.c compiles"""
    check50.c.compile("prime.c", lcs50=True)


@check50.check(compiles)
def up_to_10():
    """Input of 1 and 10 yields all prime numbers between 1 and 10, inclusive"""
    check50.run("./prime").stdin("1").stdin("10").stdout("2\n3\n5\n7")


@check50.check(compiles)
def between_10_and_50():
    """Input of 10 and 25 yields all prime numbers between 10 and 25, inclusive"""
    check50.run("./prime").stdin("10").stdin("25").stdout("11\n13\n17\n19\n23")


@check50.check(compiles)
def between_50_and_60():
    """Input of 50 and 60 yields all prime numbers between 50 and 60, inclusive"""
    check50.run("./prime").stdin("50").stdin("60").stdout("53\n59")