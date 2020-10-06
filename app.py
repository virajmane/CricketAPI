from flask import *
from pycricbuzz import Cricbuzz
import json

app = Flask(__name__)
@app.route("/")
def index():
  c = Cricbuzz()
  match = c.matches()
  mid = (match[0]['id'])
  livescore = c.livescore(mid=mid)
  scorecard = c.scorecard(mid=mid)
  matchinfo = c.matchinfo(mid=mid)
  commentary = c.commentary(mid=mid)

  result = {"matches": match, "livescore": livescore, "scorecard": scorecard, "matchinfo": matchinfo, "commentary": commentary}
  final = json.dumps(result)
  return f"<code>{final}</code>"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True)
