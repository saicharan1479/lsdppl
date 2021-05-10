from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from school.models import daily_data_excel,centerdata,Logmatch,Logfile,Branch1,Branchlog,Daily_dataaa,Logfileee,Loogfileee,Logfilee,Daily_dataa,centerbank,Groupsdata,Usersdata,Additions,RPT_Milkbillvoucher,rpt_cowmilk,rpt_bufallomilk,Loanbillsdata,Person,Excelupload,milkdata,extendeduser,RPT_consolidatedreport,Role,Rfr,RPT_Daywisesreport,Referral,Department,Office,Signup,DoK_Create,QC_Create,QC_Bank,rpt_bankwise,BufalloMilkCenter,BufalloMilkCategory,BufalloMilkRoute,Dashboard,Cloan,Deposit,Refund,Address_Ledger,Route,Daily_data,Daily_trans,QC_Entry,DoK_Entry,Milktype,Branch,Supervisor,Category,Formulae,Village,Bank,Agent,Center,CowMilkCategory,CowMilkCenter, CowMilkRoute,Transcation,MinMaxFat,MinMaxBuff
# Register your models here.

@admin.register(Excelupload)
class ExceluploadAdmin(ImportExportModelAdmin):
    list_display = ('date','Shift', 'Milktype','kgs','Ltrs', 'Fat', 'Snf', 'RateLTR', 'Netamount', 'PiExp', 'Total','center','bank','ifsc', 'accholdername',  'routename') 


admin.site.register(Dashboard)
admin.site.register(rpt_cowmilk)
admin.site.register(RPT_Milkbillvoucher)
admin.site.register(rpt_bufallomilk)
admin.site.register(Additions)
admin.site.register(Address_Ledger)
admin.site.register(daily_data_excel)
admin.site.register(Loanbillsdata)
admin.site.register(centerdata)
admin.site.register(milkdata)
admin.site.register(centerbank)
admin.site.register(Route)
admin.site.register(Deposit)
admin.site.register(RPT_consolidatedreport)
admin.site.register(Refund)
admin.site.register(Cloan)
admin.site.register(Signup)
admin.site.register(Supervisor)
admin.site.register(Category)
admin.site.register(Usersdata)
admin.site.register(Groupsdata)
admin.site.register(Formulae)
admin.site.register(Village)
admin.site.register(Bank)
admin.site.register(rpt_bankwise)
admin.site.register(Milktype)
admin.site.register(Branch)
admin.site.register(Agent)
admin.site.register(Center)
admin.site.register(Role)
admin.site.register(Referral)
admin.site.register(Rfr)
admin.site.register(Department)
admin.site.register(Office)
admin.site.register(DoK_Create)
admin.site.register(QC_Create)
admin.site.register(RPT_Daywisesreport)
admin.site.register(CowMilkCategory)
admin.site.register(CowMilkCenter)
admin.site.register(CowMilkRoute)
admin.site.register(BufalloMilkCenter)
admin.site.register(BufalloMilkRoute)
admin.site.register(BufalloMilkCategory)
admin.site.register(MinMaxBuff)
admin.site.register(Transcation)
admin.site.register(MinMaxFat)
admin.site.register(QC_Entry)
admin.site.register(DoK_Entry)
admin.site.register(QC_Bank)
admin.site.register(Logfile)
admin.site.register(Logfilee)
admin.site.register(Logfileee)
admin.site.register(Loogfileee)
admin.site.register(Logmatch)
admin.site.register(Branchlog)
admin.site.register(Daily_dataa)
admin.site.register(Daily_dataaa)
admin.site.register(Daily_trans)
admin.site.register(Branch1)
admin.site.register(Daily_data)
admin.site.register(extendeduser)
# admin.site.register(Dailyproc)