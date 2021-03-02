# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                  ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                  ("Kings", (15, 15)), ("Chargers", (20, 10)),
                  ("Jets", (16, 14)), ("Warriors", (25, 5))]
    
    
    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    
    # TODO: create an ordered dictionary of the teams
    # teams = OrderedDict(sortedTeams)
    # print(teams)
    """
    OrderedDict([('Warriors', (25, 5)), 
                ('Rockets', (24, 6)), 
                ('Dragons', (22, 8)), 
                ('Cardinals', (20, 10)), 
                ('Chargers', (20, 10)), 
                ('Royals', (18, 12)), 
                ('Jets', (16, 14)), 
                ('Kings', (15, 15))])
    """

    # TODO: Use popitem to remove the top item
    # tm, wl = teams.popitem(False)
    # print("Top team:", tm, wl)
    # ('Top team:', 'Warriors', (25, 5))

    # TODO: What are next the top 4 teams?
    # for i, team in enumerate(teams, start=1):
    #     print(i, team)
    #     if i == 4:
    #         break  
    """Out
    (1, 'Warriors')
    (2, 'Rockets')
    (3, 'Dragons')
    (4, 'Cardinals')
    """
    
    # TODO: test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2,})
    print("Equality Test:", a == b)
    # ('Equality Test:', True)   # (Python2)
    # ('Equality Test:', False)  # (Python3)
    
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality Test:", a == b)
    # ('Equality Test:', True)   # (Python2)
    # ('Equality Test:', False)  # (Python3)
    
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = {"a": 1, "c": 3, "b": 2}
    # ('Equality Test:', True)  # (Python2 & Python3)
    
    print("Equality Test:", a == b)
if __name__ == "__main__":
    main()