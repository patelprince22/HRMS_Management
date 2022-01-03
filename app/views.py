from django.shortcuts import redirect, render
from .models import *

from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.

def Home(request):
    if 'id' in request.session:
        em =Employee.objects.count()
        hr = HR.objects.count()
        emreq = EmRequest.objects.all().filter(status="pending").count()
        hrreq = HrRequest.objects.all().filter(status="pending").count()

        return render(request,'app/index.html',{'employee':em,'hrdata':hr,'emreq':emreq,'hrreq':hrreq})
    else:
        return redirect("login")
    
def Activites(request):
    return render(request,'app/activities.html')

def Assets(request):
    return render(request,'app/assets.html')

def Attendance_employee(request):
    return render(request,'app/attendance-employee.html')

def Attendance(request):
    return render(request,'app/attendance.html')

def Blank_Page(request):
    return render(request,'app/blank-page.html')

def Change_password(request):
    return render(request,'app/change-password.html')

def client_profile(request):
    return render(request,'app/client-profile.html')

def client_list(request):
    return render(request,'app/clients-list.html')

def clients(request):
    return render(request,'app/clients.html')

def Create_estimate(request):
    return render(request,'app/create-estimate.html')

def Create_invoice(request):
    return render(request,'app/create-invoice.html')

def Departments(request):
    return render(request,'app/departments.html')

def Designations(request):
    return render(request,'app/designations.html')

def Edit_estimate(request):
    return render(request,'app/edit-estimate.html')

def Edit_invoice(request):
    return render(request,'app/edit-invoice.html')

def Employee_Dashboard(request):
    return render(request,'app/employee-dashboard.html')

def Employees_list(request):
    return render(request,'app/employees-list.html')

def Employees(request):
    if 'id' in request.session:
        em = Employee.objects.all()
        return render(request,'app/Addemployees.html',{'em':em})
    else:
        return redirect('login')

def AddHR(request):
    if 'id' in request.session:
        hr= HR.objects.all()
        return render(request,'app/Addhr.html',{'hr':hr})
    else:
        return redirect('login')

def Estimate_view(request):
    return render(request,'app/estimate-view.html')

def Estimates(request):
    return render(request,'app/estimates.html')

def Expense_reports(request):
    return render(request,'app/expense-reports.html')

def Expenses(request):
    return render(request,'app/expenses.html')

def FAQ(request):
    return render(request,'app/faq.html')

def forgot_password(request):
    return render(request,'app/forgot-password.html')

def Goal_tracking(request):
    return render(request,'app/goal-tracking.html')

def Goal_type(request):
    return render(request,'app/goal-type.html')

def Holidays(request):
    return render(request,'app/holidays.html')

def invoice_reports(request):
    return render(request,'app/invoice-reports.html')

def invoice_view(request):
    return render(request,'app/invoice-view.html')

def invoices(request):
    return render(request,'app/invoices.html')

def job_applicants(request):
    return render(request,'app/job-applicants.html')

def job_details(request):
    return render(request,'app/job-details.html')

def jobs(request):
    return render(request,'app/jobs.html')

def knowledgebase_view(request):
    return render(request,'app/knowledgebase-view.html')

def knowledgebase(request):
    return render(request,'app/knowledgebase.html')

def leads(request):
    return render(request,'app/leads.html')

def leave_settings(request):
    return render(request,'app/leave-settings.html')

def leave_type(request):
    return render(request,'app/leave-type.html')

def leaves_employee(request):
    return render(request,'app/leaves-employee.html')


def leaves(request):
    if 'id' in request.session:       
        emreq=EmRequest.objects.filter(status="pending")
        
        return render(request,'app/leaves.html',{'em':emreq })
    else:
        return redirect('login')

def hrleaves(request):
    if 'id' in request.session:
       
        hrreq=HrRequest.objects.filter(status="pending")
        
        return render(request,'app/hrleaves.html',{'em':hrreq })
    else:
        return redirect('login')


def allleaveEm(request):
    if 'id' in request.session:
        emid = Admin.objects.get(id=request.session['id'])
        em = Employee.objects.get(Admin=emid)
        emall= EmRequest.objects.all().filter(Em=em) 
        return  render(request,'app/allerleave.html',{'Emall':emall})
    else:
        return redirect('login')

def allleavehr(request):
    if 'id' in request.session:
        hrid = Admin.objects.get(id=request.session['id'])
        hr = HR.objects.get(Admin=hrid)
        emall= HrRequest.objects.all().filter(hr=hr) 
        return  render(request,'app/allhrleave.html',{'Emall':emall})
    else:
        return redirect('login')

def allleave(request):
    if 'id' in request.session:
        emreq = EmRequest.objects.all()
        return render(request,'app/allleave.html',{'Emall':emreq})
    else:
        return redirect('login')

def allhrleave(request):
    if 'id' in request.session:
        req = HrRequest.objects.all()
        return render(request,'app/allleavehr.html',{'Emall':req})
    else:
        return redirect('login')


def localization(request):
    return render(request,'app/localization.html')

def login(request):
    return render(request,'app/login.html')

def OTP(request):
    return render(request,'app/otp.html')

def overtime(request):
    return render(request,'app/overtime.html')

def payments(request):
    return render(request,'app/payments.html')

def payroll_items(request):
    return render(request,'app/payroll-items.html')

def performance_appraisal(request):
    return render(request,'app/performance-appraisal.html')

def performance_indicator(request):
    return render(request,'app/performance-indicator.html')

def performance(request):
    return render(request,'app/performance.html')

def policies(request):
    return render(request,'app/policies.html')

def privacy_policy(request):
    return render(request,'app/privacy-policy.html')

def profile(request):
    if 'id' in request.session:
        admin=Admin.objects.get(id=request.session['id'])
        if admin.Role=="HR":
            user=HR.objects.get(Admin=admin)
        elif admin.Role=="Employee":
            user=Employee.objects.get(Admin=admin)
        else:
            user=Admin.objects.get(id=request.session['id'])
        
            
        return render(request,'app/profile.html',{'uid':user})
    else:
        return redirect("login")

def project_list(request):
    return render(request,'app/project-list.html')

def project_view(request):
    return render(request,'app/project-view.html')

def projects(request):
    return render(request,'app/projects.html')

def promotion(request):
    return render(request,'app/promotion.html')

def provident_fund(request):
    return render(request,'app/provident-fund.html')

def register(request):
    return render(request,'app/register.html')

def resignation(request):
    return render(request,'app/resignation.html')

def roles_permissions(request):
    return render(request,'app/roles-permissions.html')

def salary_view(request):
    return render(request,'app/salary-view.html')

def salary(request):
    return render(request,'app/salary.html')

def search(request):
    return render(request,'app/search.html')

def setting(request):
    return render(request,'app/settings.html')

def task_board(request):
    return render(request,'app/task-board.html')

def taxes(request):
    return render(request,'app/taxes.html')

def termination(request):
    return render(request,'app/termination.html')

def terms(request):
    return render(request,'app/terms.html')

def ticket_view(request):
    return render(request,'app/ticket-view.html')

def tickets(request):
    return render(request,'app/tickets.html')

def timesheet(request):
    return render(request,'app/timesheet.html')

def trainers(request):
    return render(request,'app/trainers.html')

def training_type(request):
    return render(request,'app/training-type.html')

def training(request):
    return render(request,'app/training.html')

def users(request):
    return render(request,'app/users.html')

def Reset_Password(request):
    if 'femail' in request.session:
        em=Admin.objects.get(Email=request.session['femail'])
        return render(request,'app/Reset-password.html',{'us':em})
    else:
        return redirect("forgot_password")

def EmployeeRequest(request):
    if 'id' in request.session:
        cat_leave=RequestName.objects.all()
        return render(request,'app/Emrequest.html',{'cat':cat_leave})
    else:
        return redirect("main")

def HRRequest(request):
    if 'id' in request.session:
        cat_leave=RequestName.objects.all()
        return render(request,'app/Hrrequest.html',{'cat':cat_leave})
    else:
        return redirect("main")



# Functional Logic :-

def logindata(request):
    role = request.POST['role']
    email = request.POST['email']
    passwd = request.POST['passwd']

    print(f"{role}-> {email} {passwd}")
    
    admin=Admin.objects.filter(Role=role,Email=email)

    if len(admin)>0:
        if admin[0].Password==passwd:
            print("Login Sucessfully")
            if admin[0].Role=="Admin":
                request.session['arole']=admin[0].Role
                request.session['id']=admin[0].id
                request.session['aemail']=admin[0].Email
                return redirect('main')
            elif admin[0].Role=="HR":
                hr=HR.objects.get(Admin=admin[0])
                request.session['hrole']=admin[0].Role
                request.session['id']=admin[0].id
                request.session['hemail']=admin[0].Email
                request.session['hname']=hr.Firstname
                return redirect('main')
            elif admin[0].Role=="Employee":
                emp=Employee.objects.get(Admin=admin[0])
                request.session['erole']=admin[0].Role
                request.session['id']=admin[0].id
                request.session['eemail']=admin[0].Email
                request.session['ename']=emp.Firstname
                return redirect('main')

        else:
            msg="Please Check Your Password..."
            return render(request,'app/login.html',{'err':msg})

    else:
        msg="User Doesn't Exit , Please Check Detail"
        return render(request,'app/login.html',{'err':msg})


def logout(request):   
    logadmin=Admin.objects.get(id=request.session['id'])
    if logadmin.Role == "Admin":
        del request.session['arole']
        del request.session['id']
        del request.session['aemail']
        return redirect('login')
    elif logadmin.Role == "HR":
        del request.session['hrole']
        del request.session['id']
        del request.session['hemail']
        del request.session['hname']
        return redirect('login')
        
    elif logadmin.Role == "HR":
        del request.session['erole']
        del request.session['id']
        del request.session['eemail']
        del request.session['ename']
        return redirect('login')

        
    else:
        pass

def verifyforgotemail(request):
    em =request.POST['email']
    print(em)

    admin=Admin.objects.filter(Email=em)
    if len(admin)>0:
        print("Got Email")

        # Otp Genrate :-
        otp = random.randint(100000,999999)
        print(f"OTP ------>{otp}")
        admin[0].Fotp=otp
        admin[0].save()

        # Email Sending
        subject = 'Forgot Password Verification Code...'
        message = f'Hii, Your OTP is {otp}'
        emailfrom = settings.EMAIL_HOST_USER
        recipientlist = [em, ]
        send_mail( subject, message, emailfrom, recipientlist )

        request.session['femail']=em
        return redirect("Reset-Password")

    else:
        msg="Email Doesn't Exits!!"
        return render(request,'app/forgot-password.html',{'err':msg})

def verifyotp(request):
    otp = int(request.POST['otp'])
    npasswd = request.POST['npasswd']
    cpasswd = request.POST['cpasswd']
    print(otp, npasswd ,cpasswd)

    admin=Admin.objects.get(Email=request.session['femail'])

    if admin.Fotp==otp:
        if npasswd==cpasswd:
            admin.Password=cpasswd
            admin.save()
            del request.session['femail']
            return redirect('login')
        else:
            msg="Your Password is Not Correct"
            return render(request,'app/Reset-Password.html',{'err':msg})

    else:
        msg="Please Check Your OTP"
        return render(request,'app/Reset-Password.html',{'err':msg})

def updatedata(request):
    admin=Admin.objects.get(id=request.session['id'])

    if admin.Role == "Admin":
        chk=Admin.objects.filter(Email=request.POST['email'])
        if len(chk)>0:
            msg="Email is Already Exists!!!"
            return render(request,'app/profile.html',{'err':msg,'uid':admin})
        else:
            admin.Email=request.POST['email'] if request.POST['email'] else admin.Email
        admin.Password=request.POST['passwd'] if request.POST['passwd'] else admin.Password

        admin.save()
        return redirect("profile")
    
    elif admin.Role == "HR":
        hr =HR.objects.get(Admin=admin)

        hr.Firstname = request.POST['fname'] if request.POST['fname'] else hr.Firstname
        hr.Lastname = request.POST['lname'] if request.POST['lname'] else hr.Lastname
        hr.Gender = request.POST['gender'] if request.POST['gender'] else hr.Gender
        hr.Address = request.POST['address'] if request.POST['address'] else hr.Address
        hr.Phone = request.POST['phone'] if request.POST['phone'] else hr.Phone
        hr.Bdate = request.POST['bdate'] if request.POST['bdate'] else hr.Bdate

 
        chk=Admin.objects.filter(Email=request.POST['email'])
        if len(chk)>0:
            msg="Email is Already Exists!!!"
            return render(request,'app/profile.html',{'err':msg,'uid':hr})
        else:
            admin.Email=request.POST['email'] if request.POST['email'] else admin.Email
        admin.Password=request.POST['passwd'] if request.POST['passwd'] else admin.Password

        hr.save()
        admin.save()
        return redirect("profile")
    elif admin.Role == "Employee":
        em =Employee.objects.get(Admin=admin)

        em.Firstname = request.POST['fname'] if request.POST['fname'] else em.Firstname
        em.Lastname = request.POST['lname'] if request.POST['lname'] else em.Lastname
        em.Gender = request.POST['gender'] if request.POST['gender'] else em.Gender
        em.Address = request.POST['address'] if request.POST['address'] else em.Address
        em.Phone = request.POST['phone'] if request.POST['phone'] else em.Phone
        em.Bdate = request.POST['bdate'] if request.POST['bdate'] else em.Bdate

 
        chk=Admin.objects.filter(Email=request.POST['email'])
        if len(chk)>0:
            msg="Email is Already Exists!!!"
            return render(request,'app/profile.html',{'err':msg,'uid':em})
        else:
            admin.Email=request.POST['email'] if request.POST['email'] else admin.Email
        admin.Password=request.POST['passwd'] if request.POST['passwd'] else admin.Password

        em.save()
        admin.save()
        return redirect("profile")       
    else:
        pass

def AddEmp(request):
    if request.method == "POST":
        role = request.POST['rol']
        Department = request.POST['dep']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gen = request.POST['gender']
        bdate = request.POST['bdate']
        email = request.POST['email']
        phn = request.POST['phone']
        sal = request.POST['sal']
        address = request.POST['address']

        print(f"{role,Department,fname,lname,gen,bdate,email,phn,sal,address}")

              
        admin = Admin.objects.filter(Email=email)
        if len(admin)>0:
            msg="User Already Exist"
            return render(request,"app/Addemployees.html",{'err':msg})
        else:
            createadmin=Admin.objects.create(Role=role,Email=email,Department=Department,Salary=sal)
           
            if createadmin.Role == "Employee":
                createuser=Employee.objects.create(Admin=createadmin,Firstname=fname,Lastname=lname,Address=address,Phone=phn,Bdate=bdate,Gender=gen)

                passwd = random.randint(100000,999999)
                print(f"Password ------>{passwd}")
  
                adm = Admin.objects.get(Email=email)
                adm.Password=passwd
                adm.save()

                # Email Sending
                subject = 'Login Employee'
                message = f'Hii,Your link is Link http://127.0.0.1:8000/ , Your Password is {passwd}'
                emailfrom = settings.EMAIL_HOST_USER
                recipientlist = [email, ]
                send_mail( subject, message, emailfrom, recipientlist )

                return redirect('main')
            
            else:
                msg="Your Data is not correct Role!! Please Doesn't Change"
                return render(request,"app/Addemployees.html",{'err':msg})

    else:
        print("Data Not Valid")

def joinhr(request):
    if request.method == "POST":
        role = request.POST['rol']
        Department = request.POST['dep']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gen = request.POST['gender']
        bdate = request.POST['bdate']
        email = request.POST['email']
        phn = request.POST['phone']
        sal = request.POST['sal']
        address = request.POST['address']

        print(f"{role,Department,fname,lname,gen,bdate,email,phn,sal,address}")

              
        admin = Admin.objects.filter(Email=email)
        if len(admin)>0:
            msg="User Already Exist"
            return render(request,"app/Addhr.html",{'err':msg})
        else:
            createadmin=Admin.objects.create(Role=role,Email=email,Department=Department,Salary=sal)
           
            if createadmin.Role == "HR":
                createuser=HR.objects.create(Admin=createadmin,Firstname=fname,Lastname=lname,Address=address,Phone=phn,Bdate=bdate,Gender=gen)

                passwd = random.randint(100000,999999)
                print(f"Password ------>{passwd}")
  
                adm = Admin.objects.get(Email=email)
                adm.Password=passwd
                adm.save()

                # Email Sending
                subject = 'Login HR'
                message = f'Hii,Your link is Link http://127.0.0.1:8000/ , Your Password is {passwd}'
                emailfrom = settings.EMAIL_HOST_USER
                recipientlist = [email, ]
                send_mail( subject, message, emailfrom, recipientlist )

                return redirect('main')
                
            else:
                msg="Your Data is not correct Role!! Please Doesn't Change"
                return render(request,"app/Addhr.html",{'err':msg})


    else:
        print("Data Not Valid")

def addemrequest(request):
    letype=request.POST['leavetype']
    startdate=request.POST['sdate']
    enddate=request.POST['edate']
    reason=request.POST['reason']

    print(letype,startdate,enddate,reason)
    adminid = Admin.objects.get(id=request.session['id'])
    getid=Employee.objects.get(Admin=adminid)
    letype= RequestName.objects.get(req_name=letype)

    emreq = EmRequest.objects.create(Em=getid,reqna=letype,startdate=startdate,enddate=enddate,reason=reason)
    print("Sucessfully Added")

    return redirect("EmployeeRequest")

def addhrrequest(request):
    letype=request.POST['leavetype']
    startdate=request.POST['sdate']
    enddate=request.POST['edate']
    reason=request.POST['reason']

    print(letype,startdate,enddate,reason)
    adminid = Admin.objects.get(id=request.session['id'])
    getid=HR.objects.get(Admin=adminid)
    letype= RequestName.objects.get(req_name=letype)

    emreq = HrRequest.objects.create(hr=getid,reqna=letype,startdate=startdate,enddate=enddate,reason=reason)


    return redirect("HRRequest")

def Accept(request,pk):
    if 'id'in request.session:
        emreq=EmRequest.objects.get(id=pk)
        emreq.status='Accept'
        emreq.save()
        return redirect('allleave')
    else:
        return redirect('login')

def Denay(request,pk):
    if 'id'in request.session:     
        emreq=EmRequest.objects.get(id=pk)
        emreq.status='Reject'
        emreq.save()
        return redirect('allleave')
    else:
        return redirect('login')

def Accepthr(request,pk):
    if 'id'in request.session:
        req=HrRequest.objects.get(id=pk)
        req.status='Accept'
        req.save()
        return redirect('allhrleave')
    else:
        return redirect('login')

def Denayhr(request,pk):
    if 'id'in request.session:     
        req=HrRequest.objects.get(id=pk)
        req.status='Reject'
        req.save()
        return redirect('allhrleave')
    else:
        return redirect('login')
