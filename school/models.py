from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date
import twilio
import random
from twilio.rest import Client
from django.utils import timezone
# Create your models here.

heads = (
('Salary', 'Salary'),
('Fee Collection', 'Fee Collection'),
('Current Bill', 'Current Bill'),
('Telephone Bills', 'Telephone Bills'),
('Misllanious', 'Misllanious'),
('Rent', 'Rent'),
('Transportation', 'Transportation'),
('Capitals', 'Capitals'),
('Loans', 'Loans'),
('Advances', 'Advances'),
)
class Usersdata(models.Model):
    username=models.CharField(max_length=255,blank=True)
    email=models.CharField(max_length=255,blank=True)
    gname=models.CharField(max_length=255,blank=True)
    role=models.CharField(max_length=255,blank=True)
    isactive=models.BooleanField(default=True)
    lastlogin=models.CharField(max_length=255,null=True,blank=True)
    datejoined=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.username
class Groupsdata(models.Model):
    gname=models.CharField(max_length=255,blank=True)
    pername=models.CharField(max_length=255,blank=True)   
    
    def __str__(self):
        return self.gname

class Rfr(models.Model):
    refcode=models.CharField(max_length=255,blank=True)
    def __str__(self):
        return self.refcode
class Referral(models.Model):
    referralcode=models.CharField(max_length=255,blank=True)
    def __str__(self):
        return self.referralcode
class Signup(models.Model):
    first_name=models.CharField(max_length=255, blank=True)
    last_name=models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255,unique=False, blank=True)
    email=models.CharField(max_length=255,unique=False, blank=True)
    password = models.CharField(max_length=255,  blank=True, null=True)
    role = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    graceperiod = models.CharField(max_length=255, blank=True, null=True)
    mobileno = models.BigIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True) 

    def __str__(self):
        return self.username
    def __str__(self):
        return self.username

class rpt_bankwise(models.Model):
    #date = models.DateField(null=True,blank=True)
    route_number  = models.CharField(max_length=255,null=True,blank=True)
    supervisor = models.CharField(max_length=255,null=True,blank=True)
    centre_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    branch = models.CharField(max_length=255,null=True,blank=True)
    ifsc=models.CharField(max_length=255,null=True,blank=True)
    amount  = models.FloatField(default=0.00)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    total =     models.FloatField(default=0.00)
    ddate = models.DateField(null=True,blank=True)
    net = models.FloatField(default=0.00)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. centercode
#class RPT_Centerwisesreport(models.Model):
 #   branch =  models.CharField(max_length=255, null=True, blank=True)
 #   routecode = models.CharField(max_length=255, null=True, blank=True)
  #  centercode = models.CharField(max_length=255, null=True, blank=True)
  #  date = models.DateField(null=True,blank=True)
  #  shift = models.CharField(max_length=255,null=True,blank=True)
  #  milk_type = models.CharField(max_length=255, null=True, blank=True)
  #  fat = models.FloatField(default=0.00,null=True, blank=True)
  #  snf = models.FloatField(default=0.00,null=True, blank=True)
  #  routename =  models.CharField(max_length=255, null=True, blank=True)
  #  centername =  models.CharField(max_length=255, null=True, blank=True)
  #  amount  = models.FloatField(default=0.00,null=True, blank=True)
  #  ltrrate  = models.FloatField(default=0.00,null=True, blank=True)

  #  def _str_(self):
  #      return self. centercode
class rpt_excel_bankwise(models.Model):
    #date = models.DateField(null=True,blank=True)
    route_number  = models.CharField(max_length=255,null=True,blank=True)
    supervisor = models.CharField(max_length=255,null=True,blank=True)
    centre_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    branch = models.CharField(max_length=255,null=True,blank=True)
    ifsc=models.CharField(max_length=255,null=True,blank=True)
    amount  = models.FloatField(default=0.00,null=True,blank=True)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    total = models.FloatField(default=0.00,null=True,blank=True)
    ddate = models.DateField(null=True,blank=True)
    net = models.FloatField(default=0.00,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. centercode

class extendeduser(models.Model):    
    role = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    #graceperiod = models.CharField(max_length=255, blank=True, null=True)
    referral=models.CharField(max_length=255, blank=True, null=True)    
    mobileno = models.BigIntegerField(blank=True,null=True)
    otp=models.IntegerField(blank=True, unique=True, null=True)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        otp=random.randint(100000,999999)
        account_sid = 'AC96de24b505c2e90d0f1ace3507a0f389'
        auth_token = '28affb4eba1dccfccd88b0a7100917da'
        client = Client(account_sid, auth_token)
        message=client.messages.create(
        to=self.mobileno,
        from_="+17205805470",
        body="Your OTP is "+str(otp),
        #otp=random.randint(100000,999999)
        #account_sid = 'ACb126d536a892a500164566c41bea712c'
        #auth_token = 'ad46cbb4d2d6a7955817a13f862ebf59'
        #client = Client(account_sid, auth_token)
        #message=client.messages.create(
        #to=self.mobileno,
        #from_="+14234012250",
        #body="Your OTP is "+str(otp),
        )
        self.otp=otp
        return super(extendeduser,self).save(*args, **kwargs)

class Address_Ledger(models.Model):
    ledger_code = models.CharField(max_length=255, blank=True)
    house_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    colony = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.IntegerField()

    def __str__(self):
        return self.ledger_code
        
class Cloan(models.Model):
    loan_type = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    transaction_type = models.CharField(max_length=255,null=True,blank=True)
    route = models.CharField(max_length=255,null=True,blank=True)
    center = models.CharField(max_length=255,null=True,blank=True)
    loan_no = models.CharField(max_length=255,null=True,blank=True)
    loan_date = models.DateField(null=True,blank=True)
    principal_amt = models.IntegerField(null=True,blank=True)
    interest_rate = models.FloatField(default=0.00)
    flat_deminished = models.CharField(max_length=255,null=True,blank=True)
    loan_duration = models.FloatField(null=True,blank=True)
    interest_amt = models.FloatField(default=0.00,null=True, blank=True)
    noofinstallments = models.IntegerField(null=True,blank=True)
    installment_amt = models.FloatField(default=0.00,null=True, blank=True)
    total = models.FloatField(default=0.00,null=True, blank=True)
    closingdate = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.loan_no

class Dashboard_branch(models.Model):
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00,null=True, blank=True)
    Fat=models.FloatField(default=0.00,null=True, blank=True)
    Snf=models.FloatField(default=0.00,null=True, blank=True)
    RateLTR=models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    gamount  = models.FloatField(default=0.00,null=True, blank=True)
    branch=models.CharField(max_length=255)

    
    def str(self):
        return self. centercode
        
class Refund(models.Model):
    date = models.DateField(null=True,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    issuedto = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    loan_no=models.CharField(max_length=255,null=True,blank=True)
    depositno = models.CharField(max_length=255, null=True, blank=True)
    transporter =  models.CharField(max_length=255, null=True, blank=True)
    modeofreturn = models.CharField(max_length=255, null=True, blank=True)
    routename = models.CharField(max_length=255, null=True, blank=True)
    checkorddno = models.IntegerField(default=0, null=True, blank=True)
    rtgs = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(default=0)
    remarks =  models.CharField(max_length=255, null=True, blank=True)
    issueddate = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.loan_no

class Additions(models.Model):
    date = models.DateField(null=True,blank=True)
    cartage = models.FloatField(default=0.00,null=True, blank=True)
    cattlefeed = models.FloatField(default=0.00,null=True, blank=True)
    centercode = models.CharField(max_length=255,null=True, blank=True)
    autofine = models.FloatField(default=0.00,null=True, blank=True)
    stores=models.FloatField(default=0.00,null=True, blank=True)
    aarrears = models.FloatField(default=0.00,null=True, blank=True)
    medicine =  models.FloatField(default=0.00,null=True, blank=True)
    aothers = models.FloatField(default=0.00,null=True, blank=True)
    stationary = models.FloatField(default=0.00,null=True, blank=True)
    commission = models.FloatField(default=0.00,null=True, blank=True)
    emtcharges = models.FloatField(default=0.00,null=True, blank=True)
    seed = models.FloatField(default=0.00,null=True, blank=True)
    insurance =  models.FloatField(default=0.00,null=True, blank=True)
    rarrears = models.FloatField(default=0.00,null=True, blank=True)
    rothers = models.FloatField(default=0.00,null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.centercode

class Dashboard(models.Model):
    address_detail = models.ForeignKey(Address_Ledger,blank=True, null=True,on_delete=models.CASCADE)
    heads = models.CharField(choices=heads,max_length=255)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='Dashboard',null=True,blank=True)
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True,blank=True)
    expenses_details = models.CharField(max_length=255)
    receviable = models.FloatField(default=0.0)
    payment = models.FloatField(default=0.0)
    date_year = models.IntegerField(default=0)
    date_month = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.expenses_details
        
class Deposit(models.Model):
    date = models.DateField(null=True,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    issuedto = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    depositno=models.IntegerField(default=0, null=True, blank=True)
    transporter =  models.CharField(max_length=255, null=True, blank=True)
    modeofdeposit = models.CharField(max_length=255, null=True, blank=True)
    routename = models.CharField(max_length=255, null=True, blank=True)
    checkorddno = models.IntegerField(default=0, null=True, blank=True)
    rtgs = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField(default=0.00)
    remarks =  models.CharField(max_length=255, null=True, blank=True)
    closingdate = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self): 
        return self.centercode 

class RPT_consolidatedreport(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    routename= models.CharField(max_length=255, null=True, blank=True)
    centername = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00)
    Ltrs=models.FloatField(default=0.00)
    afat = models.FloatField(default=0.00)
    asnf = models.FloatField(default=0.00)
    Fat=models.FloatField(default=0.00)
    Snf=models.FloatField(default=0.00)
    RateLTR=models.FloatField(default=0.00)
    tsrate = models.FloatField(default=0.00)
    pel = models.FloatField(default=0.00)
    gamount  = models.FloatField(default=0.00)
    net  = models.FloatField(default=0.00, null=True, blank=True)
    ltrtsrate= models.FloatField(default=0.00)
    kgtsrate = models.FloatField(default=0.00)
   
    def _str_(self):
        return self. centercode

# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='Dashboard',null=True,blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)


class daily_data_excel(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='HDFC',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    BranchCode=models.CharField(max_length=255)
    date = models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    CenterCode=models.CharField(max_length=255)
    MilkType = models.CharField(max_length=255)
    Good_Sour=models.CharField(max_length=255)
    SampleNo=models.FloatField(default=0.0)
    Cans=models.FloatField(default=0.0)
    Kgs=models.FloatField(default=0.0)
    Fat=models.FloatField(default=0.0)
    SNF=models.FloatField(default=0.0)
    CLR=models.FloatField(default=0.0)
    TSRATE=models.FloatField(default=0.0)
    Rate = models.FloatField(default=0.0)
    Comm = models.FloatField(default=0.0)
    Amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.CenterCode

class centerdata(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    CCode=models.CharField(max_length=255)
    CenterName = models.CharField(max_length=255)
    AgentName=models.CharField(max_length=255)
    RName=models.CharField(max_length=255)
    BC=models.CharField(max_length=255)
    ContactNo=models.CharField(max_length=255,null=True,blank=True)
    

    def __str__(self):
        return self.CCode

class  RPT_Milkbilldate(models.Model):
    datefrom = models.DateField(null=True,blank=True)
    dateto = models.DateField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    

    def _str_(self):
        return self. datefrom

class milkdata(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00)
    Ltrs=models.FloatField(default=0.00)
    Fat=models.FloatField(default=0.00)
    Snf=models.FloatField(default=0.00)
    RateLTR=models.FloatField(default=0.00)
    Netamount=models.FloatField(default=0.00)
    PiExp=models.FloatField(default=0.00,null=True)
    Total=models.FloatField(default=0.00)
    centercode = models.CharField(max_length=255,null=True,blank=True) 
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)
    branch = models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.Shift

class centerbank(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00)
    Ltrs=models.FloatField(default=0.00)
    Fat=models.FloatField(default=0.00)
    Snf=models.FloatField(default=0.00)
    RateLTR=models.FloatField(default=0.00)
    Netamount=models.FloatField(default=0.00)
    PiExp=models.FloatField(default=0.00)
    Total=models.FloatField(default=0.00)

    def __str__(self):
        return self.bankno 

class Excelupload(models.Model):
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255,null=True)
    Milktype=models.CharField(max_length=255,null=True)
    kgs=models.FloatField(default=0.00,null=True)
    Ltrs=models.FloatField(default=0.00,null=True)
    Fat=models.FloatField(default=0.00,null=True)
    Snf=models.FloatField(default=0.00,null=True)
    RateLTR=models.FloatField(default=0.00,null=True)
    Netamount=models.FloatField(default=0.00,null=True)
    PiExp=models.FloatField(default=0.00,null=True)
    Total=models.FloatField(default=0.00,null=True)
    center = models.CharField(max_length=255,null=True,blank=True) 
    bank = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self. date

class Person(models.Model):
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255,null=True)
    Milktype=models.CharField(max_length=255,null=True)
    kgs=models.FloatField(default=0.0,null=True)
    Ltrs=models.FloatField(default=0.0,null=True)
    Fat=models.FloatField(default=0.0,null=True)
    Snf=models.FloatField(default=0.0,null=True)
    RateLTR=models.FloatField(default=0.0,null=True)
    Netamount=models.FloatField(default=0.0,null=True)
    PiExp=models.FloatField(default=0.0,null=True)
    Total=models.FloatField(default=0.0,null=True)
    center = models.CharField(max_length=255,null=True,blank=True) 
    bank = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)

class Route(models.Model):
    Route_number = models.CharField(unique = True,max_length=255)
    Route_name = models.CharField(max_length=255)
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True) 
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.Route_name

class Route1(models.Model):
    Route_number = models.CharField(unique = True,max_length=255)
    Route_name = models.CharField(max_length=255)
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True) 

    def __str__(self):
        return self.Route_name

class Supervisor(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255)
    Route_attached1 = models.CharField(max_length=255)
    Route_attached2 = models.CharField(max_length=255)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Supervisor1(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    Route_attached1 = models.CharField(max_length=255,null=True,blank=True)
    Route_attached2 = models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.name

class Agent(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    Route_attached1 = models.CharField(max_length=255,null=True,blank=True)
    Route_attached2 = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.name

class Agent1(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    Route_attached1 = models.CharField(max_length=255,null=True,blank=True)
    Route_attached2 = models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.name

class Village(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Milktype(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code

class Milktype1(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code

class Category(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code
class Category1(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code

class Formulae(models.Model):
    name = models.CharField(max_length=255,unique=True)
    desc = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
class Formulae1(models.Model):
    name = models.CharField(max_length=255,unique=True)
    desc = models.CharField(max_length=255,unique=True)
   # remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
class Role(models.Model):
    rcode = models.CharField(max_length=255,unique=True)
    rname = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.rcode
class Role1(models.Model):
    rcode = models.CharField(max_length=255,unique=True)
    rname = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.rcode

class Office(models.Model):
    ocode = models.CharField(max_length=255,unique=True)
    oname = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.ocode
class Office1(models.Model):
    ocode = models.CharField(max_length=255,unique=True)
    oname = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.ocode
class Department(models.Model):
    dcode = models.CharField(max_length=255,unique=True)
    dname = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.dcode

class Department1(models.Model):
    dcode = models.CharField(max_length=255,unique=True)
    dname = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.dcode
#class Village(models.Model):
#    name = models.CharField(max_length=255,null=True,blank=True)

#    def __str__(self):
#        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    fullname= models.CharField(max_length=255,null=True,blank=True)
    branch   = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.fullname
class Bank1(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    fullname= models.CharField(max_length=255,null=True,blank=True)
    branch   = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.fullname
        
class Branch(models.Model):
    code = models.CharField(max_length=255,unique = True)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(default=1,null=True, blank=True)
    contno = models.BigIntegerField(default=1,null=True, blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Branch1(models.Model):
    code = models.CharField(max_length=255,null=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(default=1,null=True, blank=True)
    contno = models.BigIntegerField(default=1,null=True, blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    creaated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='lccrreate')
    crreaatedd = models.DateTimeField(default=timezone.now,null=True)
    code1 = models.CharField(max_length=255,null=True)
    name1 = models.CharField(max_length=255,null=True,blank=True)
    address1 = models.CharField(max_length=255,null=True,blank=True)
    pin1 = models.IntegerField(default=1,null=True, blank=True)
    contno1 = models.BigIntegerField(default=1,null=True, blank=True)
    email1 = models.CharField(max_length=255,null=True,blank=True)
    uppt_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='luupdattte')
    updaatedd = models.DateTimeField(default=timezone.now,null=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Branchlog(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(default=1,null=True, blank=True)
    contno = models.BigIntegerField(default=1,null=True, blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    creaated_by = models.CharField(max_length=255,null=True,blank=True)
    crreaatedd = models.DateTimeField(default=timezone.now,null=True)
    code1 = models.CharField(max_length=255,null=True)
    name1 = models.CharField(max_length=255,null=True,blank=True)
    address1 = models.CharField(max_length=255,null=True,blank=True)
    pin1 = models.IntegerField(default=1,null=True, blank=True)
    contno1 = models.BigIntegerField(default=1,null=True, blank=True)
    email1 = models.CharField(max_length=255,null=True,blank=True)
    uppt_by = models.CharField(max_length=255,null=True,blank=True)
    updaatedd = models.DateTimeField(default=timezone.now,null=True)


    def __str__(self):
        return self.name







class Center(models.Model):
    centre_code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255)
    milk_type = models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=255,null=True,blank=True)
    Formula = models.CharField(max_length=255,null=True,blank=True)
    #name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255,null=True,blank=True)
    supervisor = models.CharField(max_length=255,null=True,blank=True)
    #route_number  = models.IntegerField(null=True,blank=True)
    #
    village_name = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    address =  models.TextField(null=True,blank=True)
    actholdername = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    branch = models.CharField(max_length=255,null=True,blank=True)
    Distance = models.IntegerField(null=True,blank=True)
    Email = models.CharField(max_length=225,null=True,blank=True)
    #ifsc=models.CharField(max_length=255,null=True,blank=True)
    #kilo = models.IntegerField(null=True,blank=True)
    BM_Comm_unit = models.CharField(max_length=255,null=True,blank=True)
    CM_Comm_unit = models.CharField(max_length=255,null=True,blank=True)
    BM_Cartage_unit = models.CharField(max_length=255,null=True,blank=True)
    CM_Cartage_unit =  models.CharField(max_length=255,null=True,blank=True)
    Fat = models.CharField(max_length=255,null=True,blank=True)
    Document = models.FileField(upload_to='centerimage',null=True,blank=True)
    active = models.BooleanField(default=True) 
    BM_comm_amount = models.IntegerField(default=0.0,null=True,blank=True)
    BM_Cartage_amount = models.IntegerField(default=0.0,null=True,blank=True)
    #cm = models.CharField(max_length=255,null=True,blank=True)
    CM_comm_amount = models.FloatField(default=0.0,null=True,blank=True)
    CM_Cartage_amount = models.IntegerField(default=0.0,null=True,blank=True)
    route_number  = models.CharField(max_length=255,null=True,blank=True)
    #bm_cartage = models.CharField(max_length=255,null=True,blank=True)
    #bm_cartage_amount = models.IntegerField(null=True,blank=True)
    #cm_cartage =  models.CharField(max_length=255,null=True,blank=True)
    #cm_cartage_amount = models.IntegerField(null=True,blank=True)
    #fat = models.CharField(max_length=255,null=True,blank=True)
    #document = models.FileField(upload_to='centerimage',null=True,blank=True)
    #active = models.BooleanField(default=True) 
    ifsc=models.CharField(max_length=255,null=True,blank=True)
    bankname1 = models.CharField(max_length=255,null=True,blank=True)
    branch1 = models.CharField(max_length=255,null=True,blank=True)
    ifsc1=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
        
class CowMilkCategory(models.Model):
    # centercode =  models.ForeignKey(Center,blank=True, null=True,on_delete=models.CASCADE)
    category = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0, null=True, blank=True)
    min_rate = models.FloatField(default=0.0, null=True, blank=True)
    sour_milkrate = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.category

class CowMilkCenter(models.Model):
    centercode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.centercode


class CowMilkRoute(models.Model):
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.Routecode
class BufalloMilkCategory(models.Model):
    # centercode =  models.ForeignKey(Center,blank=True, null=True,on_delete=models.CASCADE)
    category = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0, null=True, blank=True)
    min_rate = models.FloatField(default=0.0, null=True, blank=True)
    sour_milkrate = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.category

class BufalloMilkCenter(models.Model):
    centercode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.centercode
class BufalloMilkRoute(models.Model):
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.Routecode

class rpt_bufallomilk(models.Model):
    category = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255,null=True,blank=True)
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    min_fat = models.FloatField(default=0.0,null=True,blank=True)
    max_fat = models.FloatField(default=0.0,null=True,blank=True)
    min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    tsrate = models.FloatField(default=0.0,null=True,blank=True)
    categoryid = models.IntegerField(default=0,null=True,blank=True)
    routeid = models.IntegerField(default=0,null=True,blank=True)
    centerid = models.IntegerField(default=0,null=True,blank=True)
    brid = models.IntegerField(default=0,null=True,blank=True)
    bcenterid = models.IntegerField(default=0,null=True,blank=True)
    bcategoryid = models.IntegerField(default=0,null=True,blank=True)
    bfrom_date = models.DateField(null=True,blank=True)
    bto_date = models.DateField(null=True,blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    snf_deduction = models.FloatField(default=0.0,null=True,blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)


    def __str__(self):
        return self.Routecode

class rpt_cowmilk(models.Model):
    category = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255,null=True,blank=True)
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    min_fat = models.FloatField(default=0.0,null=True,blank=True)
    max_fat = models.FloatField(default=0.0,null=True,blank=True)
    min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    tsrate = models.FloatField(default=0.0,null=True,blank=True)
    categoryid = models.IntegerField(default=0,null=True,blank=True)
    routeid = models.IntegerField(default=0,null=True,blank=True)
    centerid = models.IntegerField(default=0,null=True,blank=True)
    crid = models.IntegerField(default=0,null=True,blank=True)
    ccenterid = models.IntegerField(default=0,null=True,blank=True)
    ccategoryid = models.IntegerField(default=0,null=True,blank=True)
    cfrom_date = models.DateField(null=True,blank=True)
    cto_date = models.DateField(null=True,blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    snf_deduction = models.FloatField(default=0.0,null=True,blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.Routecode


class MinMaxFat(models.Model):    
    min_fat = models.FloatField(default=0.00,null=True,blank=True)
    max_fat = models.FloatField(default=0.00,null=True,blank=True)
    min_SNF = models.FloatField(default=0.00,null=True,blank=True)
    max_SNF = models.FloatField(default=0.00,null=True,blank=True)
    tsrate = models.FloatField(default=0.00,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
   # commission = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    routecode =  models.ForeignKey(CowMilkRoute,blank=True, null=True,on_delete=models.CASCADE)
    centercode =  models.ForeignKey(CowMilkCenter,blank=True, null=True,on_delete=models.CASCADE)
    category =  models.ForeignKey(CowMilkCategory,blank=True, null=True,on_delete=models.CASCADE)
    category1 = models.CharField(max_length=255,null=True,blank=True)
    routecode1 = models.CharField(max_length=255,null=True,blank=True)
    centercode1 = models.CharField(max_length=255,null=True,blank=True)
    def __int__(self):
        return self.min_fat
class MinMaxBuff(models.Model):    
    min_fat = models.FloatField(default=0.00,null=True,blank=True)
    max_fat = models.FloatField(default=0.00,null=True,blank=True)
    min_SNF = models.FloatField(default=0.00,null=True,blank=True)
    max_SNF = models.FloatField(default=0.00,null=True,blank=True)
    tsrate = models.FloatField(default=0.00,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    #commission = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    routecode =  models.ForeignKey(BufalloMilkRoute,blank=True, null=True,on_delete=models.CASCADE)
    centercode =  models.ForeignKey(BufalloMilkCenter,blank=True, null=True,on_delete=models.CASCADE)
    category =  models.ForeignKey(BufalloMilkCategory,blank=True, null=True,on_delete=models.CASCADE)
    category1 = models.CharField(max_length=255,null=True,blank=True)
    routecode1 = models.CharField(max_length=255,null=True,blank=True)
    centercode1 = models.CharField(max_length=255,null=True,blank=True)
    
    def __int__(self):
        return self.min_fat

class Transcation(models.Model):
    date = models.DateField(null=True,blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    good_sour = models.CharField(max_length=255, null=True, blank=True)
    centre_code = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can = models.IntegerField(null=True,blank=True, default=1)
    qty = models.FloatField(default=0.0)
    exp = models.FloatField(default=0.0,null=True,blank=True)
    rate = models.FloatField(default=0.0,null=True,blank=True)
    fat = models.FloatField(default=0.0,null=True,blank=True)
    cartage =  models.FloatField(default=0.0,null=True,blank=True)
    pen = models.FloatField(default=0.0)
    clr = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)
    total_amount = models.FloatField(default=0.0)
    snf = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.milk_type 



class Matchlog(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can = models.IntegerField(default=0,null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1 = models.IntegerField(default=0,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    hcreated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='hccrreate')
    hupdatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. branch  


class Logmatch(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can = models.IntegerField(default=0,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1 = models.IntegerField(default=0,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    hcreated_by = models.CharField(max_length=255, null=True, blank=True)
    hupdatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. branch  





class QC_Entry(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    samplecode = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(QC_Entry, self).save(*args, **kwargs)
class QC_Bank(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    samplecode = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(QC_Bank, self).save(*args, **kwargs)
class Logfilee(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    uupdaated_by = models.CharField(max_length=255, null=True, blank=True)
    ccreated_by = models.CharField(max_length=255, null=True, blank=True)
    uupdatedd = models.DateTimeField(default=timezone.now)
    ccrreatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. shift



class QC_Create(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    samplecode = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255, null=True, blank=True)
    samplecode1 = models.CharField(max_length=255, null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    remove1 = models.CharField(max_length=255, null=True, blank=True)
    upt_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='uupdattte')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='ccrreate')
    updatedd = models.DateTimeField(default=timezone.now)
    crreatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(QC_Create, self).save(*args, **kwargs)

class DoK_Entry(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    center_name = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    sour = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0,null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    samplecode =  models.IntegerField(default=0)

    def __str__(self):
        return self. branch




class Logfile(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0)
    crreateddd_by = models.CharField(max_length=255, null=True, blank=True)
    crreatedddd = models.DateTimeField(default=timezone.now)
    Quantity1 = models.FloatField(default=0.00,null=True, blank=True)
    cans1 = models.IntegerField(default=0)
    uppdated_by = models.CharField(max_length=255, null=True, blank=True)
    upppdated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. code


class DoK_Create(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    center_name = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    sour = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    samplecode =  models.CharField(max_length=255, null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)
    center_name1 = models.CharField(max_length=255, null=True, blank=True)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    sour1 = models.CharField(max_length=255, null=True, blank=True)
    Quantity1 = models.FloatField(default=0.00,null=True, blank=True)
    cans1 = models.IntegerField(default=0)
    routecode1 = models.CharField(max_length=255, null=True, blank=True)
    remove1 = models.CharField(max_length=255, null=True, blank=True)
    samplecode1 =  models.CharField(max_length=255, null=True, blank=True)
    createddd_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='updattee')
    up_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='cupdate')
    updated = models.DateTimeField(default=timezone.now)
    create= models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        super(DoK_Create, self).save(*args, **kwargs)    
class Excelextraction(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    bankno = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.0)
    Ltrs=models.FloatField(default=0.0)
    Fat=models.FloatField(default=0.0)
    Snf=models.FloatField(default=0.0)
    RateLTR=models.FloatField(default=0.0)
    Netamount=models.FloatField(default=0.0)
    PiExp=models.FloatField(default=0.0)
    Total=models.FloatField(default=0.0)


    def __str__(self):
        return self.bankno 

class Daily_trans(models.Model):
    date = models.DateField(null=True,blank=True)
    time = models.CharField(max_length=255,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.0)
    qty = models.FloatField(default=0.0)
    fat = models.FloatField(default=0.0)
    snf = models.FloatField(default=0.0)
    clr  = models.FloatField(default=0.0)

    def __str__(self):
        return self. centercode


class Logfileee(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    crea_by = models.CharField(max_length=255, null=True, blank=True)
    crb = models.DateTimeField(default=timezone.now)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    updatedd_by = models.CharField(max_length=255, null=True, blank=True)
    updateddd = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. centercode







class Loogfileee(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True)
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    crrea_by = models.CharField(max_length=255, null=True, blank=True)
    crb = models.DateTimeField(default=timezone.now)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrs1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate1  = models.FloatField(default=0.00,null=True, blank=True)
    net1  = models.FloatField(default=0.00,null=True, blank=True)
    pel1 = models.FloatField(default=0.00,null=True, blank=True) 
    amount1  = models.FloatField(default=0.00,null=True, blank=True)
    csv_file=models.CharField(max_length=255,null=True)
    uppdatedd_by = models.CharField(max_length=255, null=True, blank=True)
    updateddd = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. centercode

class Daily_dataaa(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0)
    sampno2 =  models.IntegerField(default=0)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    routecode1 = models.CharField(max_length=255, null=True, blank=True)
    centercode1 = models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255,null=True,blank=True)
    sampno1 =  models.IntegerField(default=0)
    sampno21 =  models.IntegerField(default=0)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrs1 = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate1 = models.FloatField(default=0.00,null=True, blank=True)
    comm1  = models.FloatField(default=0.00,null=True, blank=True)
    pel1 = models.FloatField(default=0.00,null=True, blank=True) 
    amount1  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate1  = models.FloatField(default=0.00,null=True, blank=True)
    net1  = models.FloatField(default=0.00,null=True, blank=True)
    csv_file=models.CharField(max_length=255,null=True)
    crrea_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='crear')
    updar_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='updar')
    updar = models.DateTimeField(default=timezone.now)
    crbb = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. centercode
    def save(self, *args, **kwargs):
        super(Daily_dataaa, self).save(*args, **kwargs)








class Daily_dataa(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0)
    sampno2 =  models.IntegerField(default=0)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    routecode1 = models.CharField(max_length=255, null=True, blank=True)
    centercode1 = models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255,null=True,blank=True)
    sampno1 =  models.IntegerField(default=0)
    sampno21 =  models.IntegerField(default=0)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrs1 = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate1 = models.FloatField(default=0.00,null=True, blank=True)
    comm1  = models.FloatField(default=0.00,null=True, blank=True)
    pel1 = models.FloatField(default=0.00,null=True, blank=True) 
    amount1  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate1  = models.FloatField(default=0.00,null=True, blank=True)
    net1  = models.FloatField(default=0.00,null=True, blank=True)
    
    crea_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='ugpdattee')
    updatedd_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='klupdatee')
    updateddd = models.DateTimeField(default=timezone.now)
    crb = models.DateTimeField(default=timezone.now)
   
   # active = models.BooleanField(default=True)

    def __str__(self):
        return self. centercode
    def save(self, *args, **kwargs):
        super(Daily_dataa, self).save(*args, **kwargs)


class Daily_data(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0)
    sampno2 =  models.IntegerField(default=0)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    ltrtsrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    routename =  models.CharField(max_length=255, null=True, blank=True)
    centername =  models.CharField(max_length=255, null=True, blank=True)
   # active = models.BooleanField(default=True)

    def __str__(self):
        return self. centercode


        
class RPT_Daywisesreport(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True) 
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    #can  = models.FloatField(default=0.0,null=True, blank=True)
    #scan  = models.FloatField(default=0.0,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True) 
    sqty = models.FloatField(default=0.00,null=True, blank=True)
    sltrs = models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00,null=True, blank=True)
    kfat = models.FloatField(default=0.00,null=True, blank=True)
    ksnf = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    gamount  = models.FloatField(default=0.00,null=True, blank=True)
    
    

    def __str__(self):
        return self. centercode

class Loanbillsdata(models.Model):
    sdate = models.DateField(null=True,blank=True)
    idate = models.DateField(null=True,blank=True)
    #time = models.CharField(max_length=255,null=True,blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    installment_amt  = models.FloatField(default=0.00,null=True, blank=True)
    interest_amt = models.FloatField(default=0.00,null=True, blank=True)
    total = models.FloatField(default=0.00,null=True, blank=True)
    noofinstallments = models.FloatField(default=0.00,null=True, blank=True)
   # clr  = models.FloatField(default=0.0)

    def __str__(self):
        return self. centercode

class rpt_dailydata(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0,null=True,blank=True)
    sampno2 =  models.IntegerField(default=0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    ltrtsrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    routename =  models.CharField(max_length=255, null=True, blank=True)
    centername =  models.CharField(max_length=255, null=True, blank=True)
   # active = models.BooleanField(default=True)

    def _str_(self):
        return self. centercode

class RPT_consolidated(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00,null=True, blank=True)
    Fat=models.FloatField(default=0.00,null=True, blank=True)
    Snf=models.FloatField(default=0.00,null=True, blank=True)
    RateLTR=models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    gamount  = models.FloatField(default=0.00,null=True, blank=True)

    
    def _str_(self):
        return self. centercode


class RPT_Daywiseabstract(models.Model):
    date=models.DateField(null=True,blank=True)
    routecode = models.CharField(max_length=255,null= True,blank=True)
    centercode = models.CharField(max_length=255)
    Shift = models.CharField(max_length=255,null=True, blank=True) 
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    fatkgs = models.FloatField(default=0.00,null=True, blank=True)
    snfkgs = models.FloatField(default=0.00,null=True, blank=True)
    Fat=models.FloatField(default=0.00,null=True, blank=True)
    Snf=models.FloatField(default=0.00,null=True, blank=True)
    tsrate=models.FloatField(default=0.00,null=True, blank=True)
    amount = models.FloatField(default=0.00,null=True, blank=True) 
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    comm = models.FloatField(default=0.00,null=True, blank=True) 
    #cartage = models.FloatField(default=0.00,null=True, blank=True) 
   # incentive = models.FloatField(default=0.00,null=True, blank=True) 
    net = models.FloatField(default=0.00,null=True, blank=True) 
    rate = models.FloatField(default=0.00,null=True, blank=True) 
    gamount  = models.FloatField(default=0.00,null=True, blank=True)

    
    def _str_(self):
        return self. centercode

class RPT_Routewisebillabstract(models.Model):
    date=models.DateField(null=True,blank=True)
    routecode = models.CharField(max_length=255,null= True,blank=True)
    centercode = models.CharField(max_length=255,null= True,blank=True)  
    qty = models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    aarrears = models.FloatField(default=0.00,null=True, blank=True)
    total = models.FloatField(default=0.00,null=True, blank=True)
    fatkgs = models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00)
    snfkgs = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00)
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    Snf1=models.FloatField(default=0.00,null=True, blank=True)
    comm = models.FloatField(default=0.00,null=True, blank=True) 
    exsamt = models.FloatField(default=0.00,null=True, blank=True)
    cartage = models.FloatField(default=0.00)
    aothers = models.FloatField(default=0.00)
    gamount  = models.FloatField(default=0.00,null=True, blank=True)
    loan_no = models.CharField(max_length=255,null=True,blank=True)
    stores=models.FloatField(default=0.00)
    rothers = models.FloatField(default=0.00)
    net = models.FloatField(default=0.00,null=True, blank=True) 
    def _str_(self):
        return self. routecode

class  RPT_Milkbillreport(models.Model):
   
    centercode = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return self. centercode


class  RPT_Milkbillvoucher(models.Model):
   # branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255,null= True,blank=True)
    routename = models.CharField(max_length=255,null= True,blank=True)
    centre_code = models.CharField(max_length=255,null= True,blank=True)
    branch = models.CharField(max_length=255,null=True, blank=True)
    centername = models.CharField(max_length=255,null=True, blank=True)
    centercode = models.CharField(max_length=255,null= True,blank=True)
    Shift = models.CharField(max_length=255,null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    milk_type=models.CharField(max_length=255,null=True, blank=True)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    ltrs=models.FloatField(default=0.00,null=True, blank=True)
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    fat=models.FloatField(default=0.00,null=True, blank=True)
    snf=models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    #center = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.BigIntegerField(blank=True,  null=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bank_branch = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    comm = models.FloatField(default=0.00,null=True, blank=True) 
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    net=models.FloatField(default=0.00,null=True, blank=True)
    agent_name=models.CharField(max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(null=True,blank=True)
    sdate = models.DateField(null=True,blank=True)
    idate = models.DateField(null=True,blank=True)
    installment_amt  = models.FloatField(default=0.00)
    interest_amt = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00,null=True, blank=True)
    payable = models.FloatField(default=0.00,null=True, blank=True)
    adate = models.DateField(null=True,blank=True)
    cartage = models.FloatField(default=0.00)
    cattlefeed = models.FloatField(default=0.00)
    acentercode = models.FloatField(default=0.00)
    autofine = models.FloatField(default=0.00)
    stores=models.FloatField(default=0.00)
    aarrears = models.FloatField(default=0.00) 
    medicine =  models.FloatField(default=0.00)
    aothers = models.FloatField(default=0.00)
    stationary = models.FloatField(default=0.00)
    commission = models.FloatField(default=0.00)
    emtcharges = models.FloatField(default=0.00)
    seed = models.FloatField(default=0.00)
    insurance =  models.FloatField(default=0.00)
    rarrears = models.FloatField(default=0.00)
    rothers = models.FloatField(default=0.00)


   # active = models.BooleanField(default=True)

    def str(self):
        return self. centercode