import check50
from re import search
from re import findall

@check50.check()
def exists():
    """answers.txt exists"""
    check50.exists("answers.txt")

@check50.check(exists)
def sorts():
    """correctly identifies each sort"""

    check50.log("checking that sorts are classified correctly...")

    expected = ["sort1 uses: [Bb]ubble", "sort2 uses: [Mm]erge", "sort3 uses: [Ss]election"]
    actual = open("answers.txt", "r").read()

    for e in expected:
        if not search(e, actual):
            raise check50.Failure("Incorrect assignment of sorts.")

    if (len(findall("sort[1-3]", actual)) != 3):
        raise check50.Failure("Incorrect formatting.")
