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
final = json.dumps(result)

app = Flask('__init__')
@app.route("/")
def index():
  return f"<code>{final}</code>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
