import check50
import check50.c
import re


@check50.check()
def exists():
    """half.c exists"""
    check50.exists("half.c")


@check50.check(exists)
def compiles():
    """half.c compiles"""
    check50.c.compile("half.c", lcs50=True)


@check50.check(compiles)
def simple():
    """Bill of $50, with 10% tax and 20% tip, creates output of $33.00"""
    check_half(bill="50", tax="10", tip="20", expected="33.00")


@check50.check(compiles)
def decimal_tax():
    """Bill of $50, with 12.5% tax and 20% tip, creates output of $33.75"""
    check_half(bill="50", tax="12.5", tip="20", expected="33.75")


@check50.check(compiles)
def rounding_up():
    """Bill of $100, with 12.5% tax and 15% tip, creates output of $64.69"""
    check_half(bill="100", tax="12.5", tip="15", expected="64.69")


@check50.check(compiles)
def rounding_down():
    """Bill of $96.40, with 13% tax and 14% tip, creates output of $62.09"""
    check_half(bill="96.40", tax="13", tip="14", expected="62.09")


# Helpers
def regex(input):
    """Match with any non-numeric characters on either end of input"""
    return rf'^\D*\${re.escape(input)}\D*$'


def check_half(bill: str, tax: str, tip: str, expected: str):
    check50.run("./half").stdin(bill).stdin(tax).stdin(tip).stdout(regex(expected), expected, regex=True)