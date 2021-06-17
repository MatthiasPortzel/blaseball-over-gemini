from jetforce import JetforceApplication, Response, Status

# Add the parent directory to the python path so that we can import blaseball
#import os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from blaseball.standings import format_standings

app = JetforceApplication()

@app.route("", strict_trailing_slash=False)
def index(request):
    return Response(Status.SUCCESS, "text/gemini", """# Blaseball Over Gemini
Blaseball Over Gemini is in an experimental state. Code is on Github:
=> https://github.com/MatthiasSaihttam/blaseball-over-gemini
## Standings
""" + format_standings())


