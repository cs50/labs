import check50
import check50.c


@check50.check()
def exists():
    """helpers.c exists"""
    check50.exists("helpers.c")
    check50.include("Makefile", "bmp.h", "helpers.h", "colorize.c", "smiley.bmp")


@check50.check(exists)
def compiles():
    """colorize compiles"""
    check50.c.compile("colorize.c", "helpers.c", lcs50=True)


@check50.check(compiles)
def test_image_creation():
    """colorize creates an image"""
    check50.run("./colorize smiley.bmp smiley_out.bmp").exit(0)
    check50.exists("smiley_out.bmp")


@check50.check(test_image_creation)
def different_color():
    """colorize changes image colors"""
    check50.run("./colorize smiley.bmp smiley_out.bmp")
    if check50.hash("smiley_out.bmp") == "1c137ffd2d7adeae0f22e00136d187f6237a4128e2dd8a413c8f9372db673a05":
        raise check50.Failure("colorize did not change image")