from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.
def date_time_view(r):
    dt=datetime.datetime.now()
    data=f"""
    <html>
    <head>
    <title>Date_Time App</title>
    </head>
    <body bgcolor="red">
    <h1>Current Date and Time:</h1><h3>{dt}</h3>
    </body>
    </html>
    """
    return HttpResponse(data)