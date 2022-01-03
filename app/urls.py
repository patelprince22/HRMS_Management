from django.contrib import admin
from django.urls import path 
from app.views import *

urlpatterns = [
    path('main/',Home,name="main"),
    path('Activites/',Activites,name="Activites"),
    path('Assets/',Assets,name="Assets"),
    path('Attendance-employee/',Attendance_employee,name="Attendance-employee"),
    path('Attendance/',Attendance,name="Attendance"),
    path('Blank_Page/',Blank_Page,name="Blank_Page"),
    path('Change_password/',Change_password,name="Change_password"),
    path('client_profile/',client_profile,name="client_profile"),
    path('client_list/',client_list,name="client_list"),
    path('clients/',clients,name="clients"),
   
    path('Create_estimate/',Create_estimate,name="Create_estimate"),
    path('Create_invoice/',Create_invoice,name="Create_invoice"),
    path('Departments/',Departments,name="Departments"),
    path('Designations/',Designations,name="Designations"),
    path('Edit_estimate/',Edit_estimate,name="Edit_estimate"),
    path('Edit_invoice/',Edit_invoice,name="Edit_invoice"),
    
    path('Employee_Dashboard/',Employee_Dashboard,name="Employee_Dashboard"),
    path('Employees_list/',Employees_list,name="Employees_list"),
    path('Employees/',Employees,name="Employees"),
    path('AddHR/',AddHR,name="Addhr"),
    path('Estimate_view/',Estimate_view,name="Estimate_view"),
    path('Estimates/',Estimates,name="Estimates"),
    path('Expense_reports/',Expense_reports,name="Expense_reports"),
    path('Expenses/',Expenses,name="Expenses"),
    path('FAQ/',FAQ,name="FAQ"),
    path('forgot_password/',forgot_password,name="forgot_password"),
    path('Goal_tracking/',Goal_tracking,name="Goal_tracking"),
    path('Goal_type/',Goal_type,name="Goal_type"),
    path('Holidays/',Holidays,name="Holidays"),
    path('invoice_reports/',invoice_reports,name="invoice_reports"),
    
    path('invoice_view/',invoice_view,name="invoice_view"),
    path('invoices/',invoices,name="invoices"),
    path('job_applicants/',job_applicants,name="job_applicants"),
    path('job_details/',job_details,name="job_details"),
    
    
    path('jobs/',jobs,name="jobs"),
    path('knowledgebase_view/',knowledgebase_view,name="knowledgebase_view"),
    path('knowledgebase/',knowledgebase,name="knowledgebase"),
    path('leads/',leads,name="leads"),
    path('leave_settings/',leave_settings,name="leave_settings"),
    path('leave_type/',leave_type,name="leave_type"),
    path('leaves_employee/',leaves_employee,name="leaves_employee"),
    
    path('leaves/',leaves,name="leaves"),
    path('hrleaves/',hrleaves,name="hrleaves"),


    path('All-leave-Em/',allleaveEm,name="allleaveEm"),
    path('All-leave-HR/',allleavehr,name="allleavehr"),

    path('All-Leave(Employee)/',allleave,name="allleave"),
    path('All-Leave(HR)/',allhrleave,name="allhrleave"),


    path('localization/',localization,name="localization"),
    
    path('',login,name="login"),
  
    path('OTP/',OTP,name="OTP"),
    path('overtime/',overtime,name="overtime"),
    path('payments/',payments,name="payments"),
    path('payroll_items/',payroll_items,name="payroll_items"),
    path('performance_appraisal/',performance_appraisal,name="performance_appraisal"),
    path('performance_indicator/',performance_indicator,name="performance_indicator"),
    path('performance/',performance,name="performance"),
    path('policies/',policies,name="policies"),
    path('privacy_policy/',privacy_policy,name="privacy_policy"),
    path('profile/',profile,name="profile"),
    path('project_list/',project_list,name="project_list"),
    path('project_view/',project_view,name="project_view"),
    path('projects/',projects,name="projects"),
    path('promotion/',promotion,name="promotion"),
    path('provident_fund/',provident_fund,name="provident_fund"),
    path('register/',register,name="register"),
    path('resignation/',resignation,name="resignation"),
    path('roles_permissions/',roles_permissions,name="roles_permissions"),
  
    path('salary_view/',salary_view,name="salary_view"),
    path('salary/',salary,name="salary"),
    path('search/',search,name="search"),
    path('settings/',setting,name="settings"),
    path('task_board/',task_board,name="task_board"),
    
    path('taxes/',taxes,name="taxes"),
    path('termination/',termination,name="termination"),
    path('terms/',terms,name="terms"),
   
    path('ticket_view/',ticket_view,name="ticket_view"),
    path('tickets/',tickets,name="tickets"),
    path('timesheet/',timesheet,name="timesheet"),
    path('trainers/',trainers,name="trainers"),
    path('training_type/',training_type,name="training_type"),
    path('training/',training,name="training"),
    path('users/',users,name="users"),
    path('Reset-Password/',Reset_Password,name="Reset-Password"),
    path('EmployeeRequest/',EmployeeRequest,name="EmployeeRequest"),
    path('HR-Request/',HRRequest,name="HRRequest"),


    # Functional Url :-
    path('logindata/',logindata,name="logindata"),
    path('logout/',logout,name="logout"),
    path('verifyforgotemail/',verifyforgotemail,name="verifyforgotemail"),
    path('verifyotp/',verifyotp,name="verifyotp"),
    path('Update_data/',updatedata,name="updatedata"),
    path('AddEmp/',AddEmp,name="AddEmp"),
    path('joinHR/',joinhr,name="joinhr"),
    path('Addemrequest/',addemrequest,name="addemrequest"),
    path('addhrrequest/',addhrrequest,name="addhrrequest"),

    path('Accept<int:pk>/',Accept,name="Accept"),
    path('Denay<int:pk>/',Denay,name="Denay"),

    path('Accepthr<int:pk>/',Accepthr,name="Accepthr"),
    path('Denayhr<int:pk>/',Denayhr,name="Denayhr"),



 
]