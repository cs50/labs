import check50

@check50.check()
def exists():
    """mario.py exists."""
    check50.exists("mario.py")

@check50.check(exists)
def compiles():
    """no syntax errors in mario.py."""
    check50.run("python -m py_compile mario.py").exit(0)

@check50.check(compiles)
def prints_four_question_marks():
    """prints four question marks"""
    check50.run("python mario.py").stdout("\?\?\?\?", "????").exit(0)
