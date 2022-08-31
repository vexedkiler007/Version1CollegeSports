import unittest
from deffinistion_football_ import teamsfinder, matching_games, find_team_average, average_dif_oppenents


class TestStringMethods(unittest.TestCase):

    def test_filtered_team_nomatching_games(self):
        teams_played = [('OleMiss', '43', 'Louisville', '24'), ('FloridaState', '38', 'NotreDame', '41'),
                        ('GeorgiaSt', '10', 'Army', '43'), ('BostonCollege', '51', 'Colgate', '0')]
        ourteam = 'OleMiss'
        other_team = 'Louisville'
        solution_team1 = [('OleMiss', '43', 'Louisville', '24')]
        solution_team2 = [('OleMiss', '43', 'Louisville', '24')]
        actuly_team1, actual_team2 = teamsfinder(games=teams_played, team1=other_team, team2=ourteam)
        self.assertEqual(solution_team1, actuly_team1)
        self.assertEqual(solution_team2, actual_team2)


class Testingteam(unittest.TestCase):
    def test_matching_games(self):
        team1 = [('apples', '43', 'bannas', '24'), ('apples', '43', 'greapes', '24'),
                 ('apples', '43', 'grapefruit', '24')]
        team2 = [('pineable', '43', 'bannas', '24'), ('pineable', '43', 'greapes', '24'),
                 ('pineable', '43', 'grapefruit', '24')]
        solution = {'bannas', 'greapes', 'grapefruit'}
        self.assertTrue(solution == matching_games((team1, team2), 'pineable', 'apples'))


class Testing_differnece(unittest.TestCase):
    def test_matching_games(self):
        team1 = [('apples', '3', 'bannas', '24'), ('apples', '443', 'greapes', '53'),
                 ('apples', '43', 'grapefruit', '22'), ('bannas', '43', 'apples', '24')]

        team2 = [('pineable', '43', 'bannas', '24'), ('pineable', '43', 'greapes', '24'),
                 ('pineable', '43', 'grapefruit', '24')]
        matching_set = {'bannas', 'greapes', 'grapefruit'}

        self.assertTrue(19.0, (find_team_average(matching_set, team2)))

        self.assertEqual(92.75, find_team_average(matching_set, team1))


class Testing_put_together(unittest.TestCase):
    teams_played = [('OleMiss', '43', 'Army', '24'), ('FloridaState', '38', 'NotreDame', '41'),
                    ('OleMiss', '43', 'Colgate', '24'), ('OleMiss', '51', 'NotreDame', '55'),
                    ('GeorgiaSt', '10', 'Army', '43'), ('BostonCollege', '51', 'Army', '0'),
                    ('BostonCollege', '51', 'Colgate', '69'), ('BostonCollege', '51', 'NotreDame', '55')]
    print(average_dif_oppenents(teams_played, 'BostonCollege', 'OleMiss'))



test_case_1 = TestStringMethods()
test_case_1.test_filtered_team_nomatching_games()

    # import os

    # cwd = os.getcwd()
    # print(entries)
