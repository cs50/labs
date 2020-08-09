import check50
import check50.c

@check50.check()
def exists():
    """scrabble.c exists"""
    check50.exists("scrabble.c")

@check50.check(exists)
def compiles():
    """scrabble.c compiles"""
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compiles)
def tie_letter_case():
    """handles letter cases correctly"""
    check50.run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout("Tie!").exit(0)

@check50.check(compiles)
def tie_punctuation():
    """handles punctuation correctly"""
    check50.run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout("Tie!").exit(0)

@check50.check(compiles)
def test1():
    """handles specification test 1"""
    check50.run("./scrabble").stdin("Question?").stdin("Question!").stdout("Tie!").exit(0)

@check50.check(compiles)
def test2():
    """handles specification test 2"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout("Player 2 wins!").exit(0)

@check50.check(compiles)
def test3():
    """handles specification test 3"""
    check50.run("./scrabble").stdin("COMPUTER").stdin("science").stdout("Player 1 wins!").exit(0)

@check50.check(compiles)
def test4():
    """handles specification test 4"""
    check50.run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout("Player 1 wins!").exit(0)

@check50.check(compiles)
def complex_case():
    """handles complex cases"""
    check50.run("./scrabble").stdin("figure?").stdin("Skating!").stdout("Player 2 wins!").exit(0)

