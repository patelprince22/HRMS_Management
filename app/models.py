from django.db import models

# Create your models here.
class Admin(models.Model):
    Email=models.EmailField(max_length=100,default="Email")
    Password=models.CharField(max_length=100,default="Password")
    Role=models.CharField(max_length=100,default="Role")
    Department=models.CharField(max_length=100,default="Depaetment")
    Salary=models.BigIntegerField(default=10000)
    Fotp=models.BigIntegerField(default=123456)
    # t_c=models.BooleanField(default=False)
    Is_Created=models.DateTimeField(auto_now_add=True)
    Is_Activated=models.BooleanField(default=True)

class HR(models.Model):
    Admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=100,default="Firstname")
    Lastname=models.CharField(max_length=100,default="Lastname")
    Gender=models.CharField(max_length=100,default="Gender")
    Address=models.CharField(max_length=100,default="Address")
    Phone=models.BigIntegerField(default=1234567890)
    Bdate=models.DateField(auto_now_add=True)

class Employee(models.Model):
    Admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    # HR=models.ForeignKey(HR,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=100,default="Firstname")
    Lastname=models.CharField(max_length=100,default="Lastname")
    Gender=models.CharField(max_length=100,default="Gender")
    Address=models.CharField(max_length=100,default="Address")
    Phone=models.BigIntegerField(default=1234567890)
    Bdate=models.DateField(auto_now_add=True)


class RequestName(models.Model):
    req_name=models.CharField(max_length=200)

    def __str__(self):
        return self.req_name

class EmRequest(models.Model):
    Em=models.ForeignKey(Employee,on_delete=models.CASCADE)
    reqna=models.ForeignKey(RequestName,on_delete=models.CASCADE)
    startdate=models.DateField()
    enddate=models.DateField()
    reason=models.CharField(max_length=100,default="Reason")
    status=models.CharField(default="pending",max_length=200)

class HrRequest(models.Model):
    hr=models.ForeignKey(HR,on_delete=models.CASCADE)
    reqna=models.ForeignKey(RequestName,on_delete=models.CASCADE)
    startdate=models.DateField()
    enddate=models.DateField()
    reason=models.CharField(max_length=100,default="Reason")
    status=models.CharField(default="pending",max_length=200)
