import check50
import check50.c


@check50.check()
def exists():
    """license.c exists"""
    check50.exists("license.c")
    check50.include("plates.txt")


@check50.check(exists)
def compiles():
    """license.c compiles"""
    check50.c.compile("license.c", lcs50=True)


@check50.check(compiles)
def valid():
    """license prints all plates."""
    check50.run("./license plates.txt").stdout("11ZT00\n1KAD21\n78ZZ01\n99ZZ11\n72ZZ21\n98ZZ31\n44ZW41\n34ZZ51")


@check50.check(compiles)
def frees_memory():
    """results in no memory leakages"""
    check50.c.valgrind("./license plates.txt").exit(0)
