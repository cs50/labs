import check50
import check50.c

@check50.check()
def exists():
    """population.c exists"""
    check50.exists("population.c")

@check50.check(exists)
def compiles():
    """population.c compiles"""
    check50.c.compile("population.c", lcs50=True)

@check50.check(compiles)
def start_less():
    """handles starting values less than 9"""
    check50.run("./population").stdin("8").stdin("8").reject()

@check50.check(compiles)
def end_less():
    """handles ending values less than starting values"""
    check50.run("./population").stdin("50").stdin("49").reject()

@check50.check(compiles)
def decimal_truncation():
    """handles decimal number of llamas"""
    check50.run("./population").stdin("1100").stdin("1192").stdout("Years: 2").exit(0)

@check50.check(compiles)
def same_value():
    """handles same starting and ending sizes"""
    check50.run("./population").stdin("100").stdin("100").stdout("Years: 0").exit(0)

@check50.check(compiles)
def test1():
    """handles starting population of 1200"""
    check50.run("./population").stdin("1200").stdin("1300").stdout("Years: 1").exit(0)

@check50.check(compiles)
def test2():
    """rejects invalid populations and then handles population 9"""
    check50.run("./population").stdin("-5").stdin("3").stdin("9").stdin("5").stdin("18").stdout("Years: 8").exit(0)

@check50.check(compiles)
def test3():
    """rejects invalid populations and then handles population 20"""
    check50.run("./population").stdin("20").stdin("1").stdin("10").stdin("100").stdout("Years: 20").exit(0)

@check50.check(compiles)
def test4():
    """handles starting population of 100"""
    check50.run("./population").stdin("100").stdin("1000000").stdout("Years: 115").exit(0)
