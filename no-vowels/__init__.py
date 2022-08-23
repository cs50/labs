import check50
import check50.c


@check50.check()
def exists():
    """no-vowels.c exists"""
    check50.exists("no-vowels.c")


@check50.check(exists)
def compiles():
    """no-vowels.c compiles"""
    check50.c.compile("no-vowels.c", lcs50=True)


@check50.check(compiles)
def simple():
    """Input of \"hello\" produces output \"h3ll0\""""
    check_no_vowels(input="hello", output="h3ll0")


@check50.check(compiles)
def longer_word():
    """Input of \"pseudocode\" produces output \"ps3ud0c0d3\""""
    check_no_vowels(input="pseudocode", output="ps3ud0c0d3")


@check50.check(compiles)
def capital_letters():
    """Input of \"Hello World\" produces output \"H3ll0 W0rld\""""
    check_no_vowels(input="\"Hello World\"", output="H3ll0 W0rld")


@check50.check(compiles)
def numbers():
    """Input of \"This is CS50\" produces output \"Th1s 1s CS50\""""
    check_no_vowels(input="\"This is CS50\"", output="Th1s 1s CS50")


# Helpers
def check_no_vowels(input: str, output: str):
    check50.run(f"./no-vowels {input}").stdout(output)