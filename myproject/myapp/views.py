from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector


# Create your views here.

def home(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def addmission(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='school'
        )
        mycur=mydb.cursor()
        sql = "insert into addmission(username,password)values(%s,%s)"
        val = (username,password)
        mycur.execute(sql,val)
        mydb.commit()
        return render(request,"student.html")
    

def student_login(request):
    if request.method=='POST':
        # id = request.POST['id']
        username = request.POST['username']
        password = request.POST['password']

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school",
        )
        mycur = mydb.cursor()
        sql = "select * from addmission where username=%s and password=%s"
        val = (username,password)
        mycur.execute(sql,val)
        row = mycur.fetchall()
        mydb.commit()
        return render(request,"student.html",{'obj':row})
    


def admin(request):
    return render(request,"admin.html")
    

def admin_login(request):
    if request.method=='POST':
        # id = request.POST['id']
        username = request.POST['username']
        password = request.POST['password']

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school",
        )
        mycur = mydb.cursor()
        sql = "select * from admin where username=%s and password=%s"
        val = (username,password)
        mycur.execute(sql,val)
        row = mycur.fetchall()
        mydb.commit()
        return render(request,"adminpage.html",{'obj':row})
    
def add_course(request):
    if request.method=='POST':
            course_name = request.POST['name']
            course_duration = request.POST['duration']
            course_fees = request.POST['fees']
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school",
)
            
            mycur = mydb.cursor()
            sql = "insert into course(course_name,course_duration,course_fees)values(%s,%s,%s)"
            val = (course_name,course_duration,course_fees)
            mycur.execute(sql,val)
            mydb.commit()
            mycur=mydb.cursor()
            sql = "select * from course"
            mycur.execute(sql)
            row = mycur.fetchall()
            mydb.commit()
            return render(request,"course_view.html",{'obj':row})        # return render(request,"course_view.html")
    
    

    
def course_view(request):
    return render(request,"course_view.html")


def course_dekho(request):
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'school',
    )
    mycur=mydb.cursor()
    sql = "select * from course"
    mycur.execute(sql)
    row = mycur.fetchall()
    mydb.commit()
    return render(request,"course_view.html",{'obj':row})

def edit_course(request,id):
     mydb=mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="school",
     )
     mycur=mydb.cursor()
     sql="select * from course where id=%s"
     val=(id,)
     mycur.execute(sql,val)
     row=mycur.fetchall()
     mydb.commit()
     return render(request,"course_edit.html",{'obj':row})


def update_course(request,id):
    if request.method=='POST':
        course_name = request.POST['name']
        course_duration = request.POST['duration']
        course_fees = request.POST['fees']
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school",
        )
        mycur=mydb.cursor()
        sql="update course set course_name=%s,course_duration=%s,course_fees=%s where id=%s"
        val=(course_name,course_duration,course_fees,id)
        mycur.execute(sql,val)
        mydb.commit()

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school",
    )
    mycur=mydb.cursor()
    sql="select * from course"
    mycur.execute(sql)
    row = mycur.fetchall()
    mydb.commit()
    return render(request,"course_view.html",{'obj':row})


def delete_course(request,id):

        mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school",
        )
        mycur=mydb.cursor()
        sql="delete from course where id=%s"
        val=(id,)
        mycur.execute(sql,val)
        mydb.commit()
        sql="select * from course"
        mycur.execute(sql)
        row  = mycur.fetchall()
        mydb.commit()
        return render(request,"course_view.html",{'obj': row})
    


def view_subject(request):
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'school',
        )
        mycur=mydb.cursor()
        sql = "select * from subject"
        mycur.execute(sql)
        row = mycur.fetchall()
        mydb.commit()
        return render(request,"subject_view.html",{'obj':row})

def student(request):
     return render(request,"student_list.html")


def student_list(request):
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'school',
    )
    mycur=mydb.cursor()
    sql = "select * from addmission"
    mycur.execute(sql)
    row = mycur.fetchall()
    mydb.commit()
    return render(request,"student_list.html",{'obj':row})
