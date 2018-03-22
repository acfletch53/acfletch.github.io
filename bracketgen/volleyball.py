from python-constraint-1.2 import *
import sys
import random

"""
Each team can be identified by their Division plus their number.

Variables -> Domains




"""



COURTS = range(1, 25) # 24 courts

# 12 divisions
NUM_DIVISIONS = 12 # safety first, kids

DIVISIONS = ["11/12 Open",
             "13 Open",
             "14 Club",
             "14 Open",
             "15 Club",
             "15 Open",
             "16 Club",
             "16 Open",
             "17 Club",
             "17 Open",
             "18 Club",
             "18 Open"]

# Because I'm lazy, lest just assume each team has a number. Yeah.
TEAMS = [range(8 + random.randint(0, 4) for x in xrange(12))]


ACTUAL_TEAMS = ["Atlanta Extreme",
         "ATLBoom",
         "TCA",
         "Cobb Atlanta",
         "Crossfire Third Degree Hybrid",
         "MIDTN VBC",
         "NAVC",
         "A5",
         "GA5",
         "Tsunami",
         "A5 South",
         "VerticleOne"]

# Six possible times for each team to play
# Teams are either in the morning or the evening. All pools are in the same wave
MORNING_WAVE = ["8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM"]
EVENING_WAVE = ["2:30 PM", "3:30 PM", "4:30 PM", "5:30 PM", "6:30 PM", "7:30 PM"]



WAVE = ["AM", "PM"]

# Each game has a home team, an away team, and a reffing team. Ideally all in the same pool.
GAME = ["Ref", "Home", "Away", "Off"]

ALL_TEAM_NAMES = []




def main():
    problem = Problem()
    # Set up problem
    for division_num in len(DIVISIONS):
        num_teams = 8 + random.randint(0, 4)
        # If divisible by 4, we want pools of 4. (Minimum of 8 teams in a division)
        # If not, then we need remaining pools of 3.
        pools_of_3 = (4 - (num_teams % 4)) % 4
        # If leftover teams is 1, we have 3 pools of 3
        # 2, 2 pools of 3
        # 3, 1 pool of 3 and 0... 0
        num_pools = math.ceil(num_teams / 4.0)
        # Probably don't need this?
        ALL_TEAM_NAMES[division_num]= [ACTUAL_TEAMS[x] + " " + DIVISIONS(division_num) for x in xrange(1, num_teams + 1)]
        for team_name in ALL_TEAM_NAMES[division_num]:
            problem.addVariable(team_name + " Wave", WAVE)
            problem.addVariable(team_name + " Pool", range(1, num_pools + 1))
            for time in MORNING_WAVE + EVENING_WAVE:
                # At every time slot, a team is either reffing, playing, or off
                problem.addVariable(team_name + " " + time, GAME)
        for pool_num in xrange(1, num_pools + 1):
            if pool
    for ALL_TEAM_NAMES


