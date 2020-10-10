import os
import re
import check50
import check50.py

BRACKET2=[{'team': 'Uruguay', 'rating': 976}, {'team': 'Portugal', 'rating': 1306}]
BRACKET4=[{'team': 'Uruguay', 'rating': 976}, {'team': 'Portugal', 'rating': 1306}, {'team': 'France', 'rating': 1166}, {'team': 'Argentina', 'rating': 1254}]
BRACKET8=[{'team': 'Uruguay', 'rating': 976}, {'team': 'Portugal', 'rating': 1306}, {'team': 'France', 'rating': 1166}, {'team': 'Argentina', 'rating': 1254}, {'team': 'Brazil', 'rating': 1384}, {'team': 'Mexico', 'rating': 1008}, {'team': 'Belgium', 'rating': 1346}, {'team': 'Japan', 'rating': 528}]
BRACKET16=[{'team': 'Uruguay', 'rating': 976}, {'team': 'Portugal', 'rating': 1306}, {'team': 'France', 'rating': 1166}, {'team': 'Argentina', 'rating': 1254}, {'team': 'Brazil', 'rating': 1384}, {'team': 'Mexico', 'rating': 1008}, {'team': 'Belgium', 'rating': 1346}, {'team': 'Japan', 'rating': 528}, {'team': 'Spain', 'rating': 1162}, {'team': 'Russia', 'rating': 493}, {'team': 'Croatia', 'rating': 975}, {'team': 'Denmark', 'rating': 1054}, {'team': 'Sweden', 'rating': 889}, {'team': 'Switzerland', 'rating': 1179}, {'team': 'Colombia', 'rating': 989}, {'team': 'England', 'rating': 1040}]

@check50.check()
def exists():
    """tournament.py exists"""
    check50.exists("tournament.py")
    check50.include("2018m.csv", "2019w.csv")

@check50.check(exists)
def imports():
    """tournament.py imports"""
    check50.py.import_("tournament.py")

@check50.check(imports)
def sim_tournament_2():
    """simulate_tournament handles a bracket of size 2"""
    check_tournament(BRACKET2)

@check50.check(imports)
def sim_tournament_4():
    """simulate_tournament handles a bracket of size 4"""
    check_tournament(BRACKET4)

@check50.check(imports)
def sim_tournament_8():
    """simulate_tournament handles a bracket of size 8"""
    check_tournament(BRACKET8)

@check50.check(imports)
def sim_tournament_16():
    """simulate_tournament handles a bracket of size 16"""
    check_tournament(BRACKET16)

@check50.check(imports)
def counts():
    """correctly keeps track of wins"""
    actual = check50.run("python3 tournament.py 2018m.csv").stdout()
    percents = re.findall("[0-9]*\.[0-9]", actual)
    percents = [float(x) for x in percents]
    if (sum(percents) < 99 or sum(percents) > 101):
        raise check50.Failure("fails to keep track of wins")

@check50.check(imports)
def correct_teams1():
    """correctly reports team information for Men's World Cup"""
    actual = check50.run("python3 tournament.py 2018m.csv").stdout()
    expected = ["Belgium", "Brazil", "Portugal", "Spain"]
    not_expected = ["Germany"]
    for team in expected:
        if team not in actual:
            raise check50.Failure(f"did not find team {team}")
    for team in not_expected:
        if team in actual:
            raise check50.Failure(f"incorrectly found team {team}")

@check50.check(imports)
def correct_teams2():
    """correctly reports team information for Women's World Cup"""
    actual = check50.run("python3 tournament.py 2019w.csv").stdout()
    expected = ["Germany", "United States", "England"]
    not_expected = ["Belgium"]
    for team in expected:
        if team not in actual:
            raise check50.Failure(f"did not find team {team}")
    for team in not_expected:
        if team in actual:
            raise check50.Failure(f"incorrectly found team {team}")

    percents = re.findall("[0-9]*\.[0-9]", actual)
    percents = [float(x) for x in percents]
    if (sum(percents) < 99 or sum(percents) > 101):
        raise check50.Failure("fails to keep track of wins")

def check_round(*args):
    tournament = check50.py.import_("tournament.py")
    actual = tournament.simulate_round(args[0])

    for i in range(len(actual)):
        expected = [args[0][2 * i], args[0][2 * i + 1]]
        if (not (actual[i] in expected)):
            raise check50.Failure("simulate_round fails to determine winners in a round")

def check_tournament(*args):
    tournament = check50.py.import_("tournament.py")
    actual = tournament.simulate_tournament(args[0])
    teams = [x["team"] for x in args[0]]

    if (not actual in teams):
        raise check50.Failure("simulate_tournament fails to return the name of 1 winning team")
