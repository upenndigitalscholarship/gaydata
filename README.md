# gaydata

Basic care of [gaydata.apjan.co](https://gaydata.apjan.co/)
To access the server, type `ssh yourUsername@gaydata.apjan.co`  
This is a FastAPI application ([docs](https://fastapi.tiangolo.com/)). The Python virtual env lives here `/srv/gaydata/venv`. To activate, `source venv/bin activate`.  It uses jinja2 templates to render dynamic HTML. 
It saves the form text as json in `app/data/json` and an uploaded image to `app/data/images`. The form will only accept jpeg or png. That can be changed by the user, so I added validation on the server as well.  
```
/srv/gaydata
- app
  - main.py # script for the FastAPI app
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
The VM currently has 25G of storage. 
