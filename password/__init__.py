import check50
import check50.c


@check50.check()
def exists():
    """password.c exists"""
    check50.exists("password.c")


@check50.check(exists)
def compiles():
    """password.c compiles"""
    check50.c.compile("password.c", lcs50=True)


@check50.check(compiles)
def valid():
    """Password of 3PQvbQ6_GvneW!3R is accepted."""
    check_password(password="3PQvbQ6_GvneW!3R", valid=True)


@check50.check(compiles)
def no_uppercase():
    """Password of hqsk3wb. is rejected for lack of uppercase characters."""
    check_password(password="hqsk3wb.", valid=False)


@check50.check(compiles)
def no_lowercase():
    """Password of F-WH8PQP is rejected for lack of lowercase characters."""
    check_password(password="F-WH8PQP", valid=False)


@check50.check(compiles)
def no_symbol():
    """Password of VnrHMtV4 is rejected for lack of symbols."""
    check_password(password="VnrHMtV4", valid=False)


@check50.check(compiles)
def no_number():
    """Password of iWnktW*q is rejected for lack of numbers."""
    check_password(password="iWnktW*q", valid=False)


# Helpers
def check_password(password: str, valid: bool):
    program = check50.run("./password").stdin(password)
    if valid:
        program.stdout("Your password is valid!")
    else:
        program.stdout("Your password needs at least one uppercase letter, lowercase letter, number and symbol")