from django.shortcuts import render
from django.http import HttpResponse


import mysql.connector as m

# database connectivity

mydatabase=m.connect(host="localhost",user="root",password="rootsql123",database="turfBS")
query1="insert into turf_users(turf,nopeople,btime,bdate,bname) values(%s,%s,%s,%s,%s)"         #  must be "s"
query2="SELECT * FROM turf_users WHERE bname = %s"
query3 = "select * from turf_users"
cursor=mydatabase.cursor()

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def result(request):
    turfname = request.POST.get("option")
    nofpeople = request.POST.get("number")
    btime = request.POST.get("btime")
    bdate = request.POST.get("bdate")
    bname = request.POST.get("bname")
    cursor.execute(query1,[turfname,nofpeople,btime,bdate,bname])
    mydatabase.commit()
    return render(request,'home.html')

def BookSlot(request):
    return render(request, 'form.html')

#def CheckBooking(request):
    # if request.method == 'GET':
    #     username = request.POST.get('bname')
    #     print("Username from form:", username)
    #     query2 = "SELECT * FROM turf_users WHERE bname = %s"
    #     print("Query:", query2)
    #     cursor.execute(query2, (username,))
    #     record = cursor.fetchone()
    #     print("Fetched record:", record)
    #     context = {'record': record}
    #     return render(request, 'check.html', context)
    # else:
    #     return HttpResponse("Invalid request method")


def CheckBooking(request):
    cursor.execute(query3)
    record = cursor.fetchone()
    context = {'record': record}
    return render(request,'check.html', context)

def login(request):
    return render(request, 'check.html')
