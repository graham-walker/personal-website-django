wt -w 0 new-tab cmd /k "call .\env\Scripts\activate.bat && python manage.py runserver"
wt -w 0 new-tab cmd /k "sass --watch .\personal\static\sass\main.scss:.\personal\static\css\custom.min.css --style compressed --no-source-map"
start http://localhost:8000
