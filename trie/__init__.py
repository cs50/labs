import check50
import check50.c

@check50.check()
def exists():
    """trie.c exists"""
    check50.exists("trie.c")
    check50.include("names")

@check50.check(exists)
def compiles():
    """trie.c compiles"""
    check50.c.compile("trie.c", lcs50=True)

@check50.check(compiles)
def noargs():
    """check number of command line arguments (no args)"""
    check50.run("./trie").exit(1)

@check50.check(compiles)
def toomanyargs():
    """check number of command line arguments (too many args)"""
    check50.run("./trie aaa.txt bbb.txt").exit(1)

@check50.check(compiles)
def nofile():
    """checks for non-existing file"""
    check50.run("./trie names/test.txt").exit(1)

@check50.check(compiles)
def test1():
    """checks for Molly"""
    check50.run("./trie names/dog_names.txt").stdin("Molly").stdout("Found!").exit()

@check50.check(compiles)
def test2():
    """checks for Lucy"""
    check50.run("./trie names/dog_names.txt").stdin("Lucy").stdout("Found!").exit()

@check50.check(compiles)
def test3():
    """checks for Prudence"""
    check50.run("./trie names/dog_names.txt").stdin("Prudence").stdout("Not Found.").exit()

@check50.check(compiles)
def test4():
    """checks for mOLLy (ignores case)"""
    check50.run("./trie names/dog_names.txt").stdin("mOLLy").stdout("Found!").exit()

# names from https://www.ssa.gov/oact/babynames/decades/century.html
@check50.check(compiles)
def test5():
    """checks for other names (Found)"""
    check50.run("./trie names/other_names.txt").stdin("JENNIFER").stdout("Found!").exit()

@check50.check(compiles)
def test6():
    """checks for other names (Not Found)"""
    check50.run("./trie names/other_names.txt").stdin("Jenni").stdout("Not Found.").exit()

