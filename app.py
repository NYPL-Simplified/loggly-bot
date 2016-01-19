import os
from flask import Flask, request
import requests
import json
import traceback
import re
from pdb import set_trace

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log():
    try:
        webhook_url = os.environ['WEBHOOK_URL']
        data = json.loads(request.data)
        alert_name = data.get('alert_name')
        num_hits = data.get('num_hits')
        recent_hits = data.get('recent_hits')
        search_link = data.get('search_link')
        text = "%s: <%s|%s hits>" % (alert_name, search_link, num_hits)
        try:
            hits = json.loads(recent_hits)
            fields = [{'value': hit['message'], 'short':True} for hit in hits]
        except Exception as e:
            # The recent hits might not be valid json, so we'll just try to find them in the string..
            # This happens in loggly when there's a traceback in the hit.
            recent_hits_re = re.compile("\"recent_hits\"\s:(.*)")
            hits = recent_hits_re.search(request.data)
            if hits:
                fields = [{'value': hits.group(1)}]
            else:
                # Didn't find any recent hits in the request, so we'll just send the whole thing.
                fields = [{'value': request.data}]
        attachment = {"fallback":text, "pretext":text, "fields": fields}
        payload = json.dumps({"attachments":[attachment]})
        requests.post(webhook_url, data={'payload':payload})
    except Exception as e:
        message = "Sorry, there was an alert from loggly but I couldn't process it: %s" % e
        payload = json.dumps({"attachments": [{"fallback": message, "pretext": message, "fields": []}]})
        print e
        traceback.print_exc()
        requests.post(webhook_url, data={'payload':payload})
    return ""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
