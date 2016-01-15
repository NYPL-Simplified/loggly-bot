A simple flask app that can receive alerts from loggly and reformat them before posting to slack.
## Deploying to Heroku
Create a heroku account, install the heroku tools, and configure a slack incoming webhook.


```
heroku create
heroku apps:rename app-name
heroku config:set WEBHOOK_URL="https://hooks.slack.com/services/..."
git push heroku master
```

## Configuring loggly
In loggly, create an alert HTTP/S endpoint with the url https://<app-name>.herokuapp.com/log, with method GET.

## License
```
Copyright © 2015 The New York Public Library, Astor, Lenox, and Tilden Foundations

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
