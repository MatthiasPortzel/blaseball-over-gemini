from itertools import chain

from blaseball_mike.models.simulation_data import SimulationData
from blaseball_mike.models.season import Season

sim = SimulationData.load()

class TeamStanding:
    def __init__ (self, team, standings):
        self.team = team
        self.wins = standings.wins[team.id]
        self.losses = standings.losses[team.id]
        self.games = standings.games_played[team.id]
        self.unLosses = self.games - self.losses

    def __repr__(self):
        return f"[{self.wins}] {self.team.location} {self.team.nickname} ({self.unLosses}-{self.losses})"

def get_top_teams(division):
    standings = Season.load(sim.season).standings

    # Standings.wins is a dict {"TEAM-UUID": INT_NUM_WINS, ...}
    teams = [TeamStanding(team, standings) for team in division.teams.values()]
    teams.sort(key=lambda t: t.wins, reverse=True)
    return teams


# A list of 4 tuples of a division and a list of teams, sorted by Wins. Teams should have a .wins, .unLosses, and .losses
def standings():
    divisions = chain.from_iterable([subleague.divisions.values() for subleague in sim.league.subleagues.values()])

    standings = [(division, get_top_teams(division)) for division in divisions]

    return standings


def format_standings():
    s = ""
    for (d, teams) in standings():
        s += f"## {d.name}\n"
        for team in teams:
            s += f"{team}\n"
        s += "\n"
    return s

if __name__ == "__main__":
    print(format_standings())
