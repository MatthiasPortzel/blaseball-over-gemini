from itertools import chain

from blaseball_mike.models.simulation_data import SimulationData
from blaseball_mike.models.season import Season

sim = SimulationData.load()


def get_top_teams(division):
    standings = Season.load(sim.season).standings

    # Standings.wins is a dict {"TEAM-UUID": INT_NUM_WINS, ...}, sorted by wins
    # We conve
    # teams_from_standings_filtered = {t:w for (t,w) in season_standings.wins.items() if (t in division.teams)}

    teams = list(division.teams.values())
    teams.sort(key=lambda t: standings.wins[t.id], reverse=True)
    return teams


# A list of 4 tuples of a division and a list of teams, sorted by Wins. Teams should have a .wins, .unLoses, and .loses
def standings():
    divisions = chain.from_iterable([subleague.divisions.values() for subleague in sim.league.subleagues.values()])

    standings = [(division, get_top_teams(division)) for division in divisions]

    return standings


def format_standings():
    s = ""
    for (d, teams) in standings():
        s += f"# {d.name}\n"
        for t in teams:
            s += f"{t.location} {t.nickname}\n"
        s += "\n"
    return s

if __name__ == "__main__":
    print(format_standings())
