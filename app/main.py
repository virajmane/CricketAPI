from flask import *
from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()
match = c.matches()
mid = (match[0]['id'])
livescore = c.livescore(mid=mid)
scorecard = c.scorecard(mid=mid)
matchinfo = c.matchinfo(mid=mid)
commentary = c.commentary(mid=mid)

result = {"matches": match, "livescore": livescore, "scorecard": scorecard, "matchinfo": matchinfo, "commentary": commentary}
final = json.dumps(result, indent=4)

app = Flask('__init__')
@app.route("/")
def index():
  return f"<code>{final}</code>"
