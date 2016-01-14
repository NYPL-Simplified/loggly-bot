import os
from flask import Flask, request
import requests
import json
from pdb import set_trace

app = Flask(__name__)

@app.route("/log")
def log():
    webhook_url = os.environ['WEBHOOK_URL']
    alert_name = request.args.get('alert_name')
    num_hits = request.args.get('num_hits')
    recent_hits = request.args.get('recent_hits')
    search_link = request.args.get('search_link')
    text = "%s: <%s|%s hits>, including:" % (alert_name, search_link, num_hits)
    fields = [{'value': hit['message'], 'short':True} for hit in json.loads(recent_hits)]
    attachment = {"fallback":text, "pretext":text, "fields": fields}
    payload = json.dumps({"attachments":[attachment]})
    requests.post(webhook_url, data={'payload':payload})
    return ""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
