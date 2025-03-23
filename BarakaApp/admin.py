from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customers)
admin.site.register(Employees)
admin.site.register(Locations)
admin.site.register(Dbts)
admin.site.register(Cylinder)
admin.site.register(SalesTab)
admin.site.register(CreditTransaction)
admin.site.register(CylinderWeight)
admin.site.register(CylinderType)
admin.site.register(TypeOfSale)
admin.site.register(SalesTeam)
admin.site.register(AssignedCylinders)
admin.site.register(Messages)
admin.site.register(CylinderStore)
admin.site.register(OtherProducts)
admin.site.register(TypeOfSalesTeam)
admin.site.register(AssignedOtherProducts)
admin.site.register(ReturnClylindersReciept)
admin.site.register(AssignedCylindersRecipt)
admin.site.register(CylinderLost)
admin.site.register(CylinderLessPay)
admin.site.register(Expenses)
admin.site.register(Advances)
admin.site.register(MonthlySalary)