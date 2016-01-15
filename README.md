A simple flask app that can receive alerts from loggly and reformat them before posting to slack.

== Deploying to Heroku ==
Create a heroku account, install the heroku tools, and configure a slack incoming webhook.


```
heroku create
heroku apps:rename app-name
heroku config:set WEBHOOK_URL="https://hooks.slack.com/services/..."
git push heroku master
```