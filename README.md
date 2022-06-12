# gaydata

Basic care and feeding of gaydata.apjan.co 
To access the server, type `ssh yourUsername@gaydata.apjan.co`  
This is a FastAPI application. The Python virtual env lives here `/srv/gaydata/venv`.  It uses jinja2 templates to render dynamic HTML. 
It saves the form text as json in `app/data/json` and an uploaded image to `app/data/images`  
```
/srv/gaydata
- app
  - main.py # script for the FastAPI all
  - templates
    - base.html
    - index.html
    - success.html
  - data
    - json
    - images
```

Web server: is nginx with certbot for HTTPS.  
Application server: is gunicorn running as as a systemd service.  To restart the app, `service gaydata restart`
Logs live in `/srv/gaydata` as `error.log` and `access.log`
API docs: https://gaydata.apjan.co/docs
See current posts: https://gaydata.apjan.co/results
Get the results as json: https://gaydata.apjan.co/data  
