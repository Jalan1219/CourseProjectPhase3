def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter the start date (mm/dd/yyyy): ")
    todate = input("Enter the end date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input("Enter the amount of hours worked: "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
    
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
    
        TotEmployees += 1
        TotHours += hours
        TotGrossPaay += grosspay
        TotTax += incometax
        TotNetPay += netpay
    
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay
    
def PrintTotals(EmpTotals):
    print()
    print(f"Total number of employees: {EmpTotals['TotEmp']}")
    print(f"Total hours worked: {EmpTotals['TotHrs']}")
    print(f"Total gross pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total income tax: {EmpTotals['TotTax']:,.1%}")
    print(f"Total net pay: {EmpTotals['TotNetPay']:,.2f}")
    
def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def GetFromDate():
    valid = False
    fromdate = ""
    
    while not valid:
        fromdate = input("Enter from date (mm/dd/yyyy): ")
        if (len(fromdate.split('/')) !=3 and fromdate.upper() != 'ALL'):
            print("Invalid date format")
        else:
            valid = True 
            
    return fromdate 

def ReadEmployeeInformation(fromdate):
    


    

