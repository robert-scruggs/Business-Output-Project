import pdfplumber

listoffiles = ["report/pdfs/6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf",
               "report/pdfs/6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf",
               "report/pdfs/6_2015 Income Tax Return_ CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf",
               "report/pdfs/6_2015 Income Tax Return_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf",
               "report/pdfs/6_2016 Income Tax Return_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf",
               "report/pdfs/6_2016 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf",
               "report/pdfs/6_2018 ITR_1065_OVERHOLT INVESTMENTS LLC SAFE SEND.pdf",
                "report/pdfs/6_2019 ITR 1120S_Hannon Foods of Tallulah.pdf",
                "report/pdfs/6_2017_CRG Amended 2017 Taxes.pdf",
                "report/pdfs/6_2017_CHR Amended 2017 Taxes.pdf",
                "report/pdfs/6_2018 ITR_1065_OVERHOLT INVESTMENTS LLC SAFE SEND.pdf",
                "report/pdfs/6_2019 1120S_Hannon Foods of Vicksburg.pdf",
                "report/pdfs/6_2019 ITR 1120S_Hannon Foods of Tallulah.pdf",
                "report/pdfs/6_2019 ITR_1065_OVERHOLT INVESTMENTS LLC SAFE SEND.pdf",
                "report/pdfs/6_2020 ITR 1065_OVERHOLT INVESTMENTS_ LLC_2020_1065_Tax Returns.pdf",
                "report/pdfs/6_2020 ITR 1120S Hannon Foods of Tallulah.pdf",
                "report/pdfs/6_2020 ITR 1120S Hannon Foods of Vicksburg.pdf",
                "report/pdfs/6_2020 ITR_Delish Brands LLC .pdf",
                "report/pdfs/2015 Income Tax Return_Patel_JEWELL SOUTH 2015.pdf"
               ]

secondListoffiles = ["report/pdfs/6_2018 ITR_1065_OVERHOLT INVESTMENTS LLC SAFE SEND.pdf",
                    "report/pdfs/6_2019 1120S_Hannon Foods of Vicksburg.pdf",
                    "report/pdfs/6_2019 ITR 1120S_Hannon Foods of Tallulah.pdf",
                    "report/pdfs/6_2019 ITR_1065_OVERHOLT INVESTMENTS LLC SAFE SEND.pdf",
                    "report/pdfs/6_2020 ITR 1065_OVERHOLT INVESTMENTS_ LLC_2020_1065_Tax Returns.pdf",
                    "report/pdfs/6_2020 ITR 1120S Hannon Foods of Tallulah.pdf",
                    "report/pdfs/6_2020 ITR 1120S Hannon Foods of Vicksburg.pdf",
                    "report/pdfs/6_2020 ITR_Delish Brands LLC .pdf",
                    "report/pdfs/2015 Income Tax Return_Patel_JEWELL SOUTH 2015.pdf"
                    ]

filesthatdontwork = [
                    #"report/pdfs/6_2019 ITR 1065_Delish Real Estate Holdings LLC.pdf",
                    #"report/pdfs/6_2019 ITR_1065 Delish Brands, LLC.pdf",
                    #"report/pdfs/6_2020 ITR_Delish Real Estate  Holdings, LLC.pdf",
    ]
pdf = pdfplumber.open(secondListoffiles[0])
text = pdf.pages[6].extract_text()
if "cBalance. Subtract line 1b from line 1a" in text:
    print("found")


# pdf = pdfplumber.open(secondListoffiles[1])
# text = pdf.pages[8].extract_text()
# print(text)
# print("------------------------------------")

# pdf = pdfplumber.open(secondListoffiles[2])
# text = pdf.pages[4].extract_text()
# print(text)
# print("------------------------------------")

# randomFile = 'report/pdfs/report/pdfs/5_2020 ITR_Josh & Laura Overholt.pdf'
# amortization does not work for all files, needs consistent files
# def getAmortization(fileList):
#     myList = []
#     for file in fileList:
#         pdf = pdfplumber.open(file)
#         for page in pdf.pages:
#             currList = page.extract_text().split(" ")
#             for item in currList:
#                 if "Amortization(a)\n(b)" and "Amortizable" in item:
#                     print("found")
#                     print(page.extract_text(), page.page_number)
#                     myList.append(page.extract_text())
#     ammortizationList = []
#     counter = 1
#     for x in range(1, len(myList), 2):
#         keepTrack = myList[counter].split(" ").index("44") + 1
#         amortization = myList[counter].split(" ")[keepTrack].split("\n")[
#             0].replace(",", "").replace(".", "")
#         ammortizationList.append(int(amortization))
#         counter = counter + 2

#     for x in ammortizationList:
#         print(x)
#     return ammortizationList

def getAmortization(fileList):
    myList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text()
            if "44 Total. Add amounts in column (f). See the instructions for where to report" and "\nPart VI Amortization(a)\n(b) (c) (d) (e) (f)\n" in currList:
                print("found", page.page_number)
                myList.append(page.extract_text())
                break    
    ammortizationList = []
    counter = 0
    for x in range(0, len(myList)):
        keepTrack = myList[counter].split(" ").index("44") + 1
        amortization = myList[counter].split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        ammortizationList.append(int(amortization))
        counter = counter + 1

    for x in ammortizationList:
        print(x)
    return ammortizationList

# interest does not work for all files, needs consistent files


def getInterest():
    interestPages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    interestPages.append(page.extract_text())
    interestList = []
    counter = 1
    for x in range(1, len(interestPages), 2):
        keepTrack = interestPages[counter].split(" ").index("15") + 1
        interest = interestPages[counter].split(" ")[keepTrack].split("\n")[
            0].replace(",", "").replace(".", "")
        interestList.append(int(interest))
        counter = counter + 2

    for x in interestList:
        print(x)
    return interestList


def getDepreciation(fileList):
    depreciationPages = []
    depreciationNumList = []
    counter = 0

    def depreciationMethod(num):
        keepTrack = depreciationPages[counter].split(" ").index(num) + 1
        depreciation = int(depreciationPages[counter].split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", ""))
        depreciationNumList.append(depreciation)
         

    for file in fileList:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text()
            # 1065
            if "16 aDepreciation (if required, attach Form 4562)" in currList or "16a Depreciation (if required, attach Form 4562)" in currList:
                print("found", page.page_number, file)
                depreciationPages.append(page.extract_text())
                depreciationMethod("16a")
                counter = counter + 1
                break
            # 1120
            elif "14 Depreciation not claimed on Form 1125-A or elsewhere on return (attach Form 4562)" in currList:
                print("found", page.page_number, file)
                depreciationPages.append(page.extract_text())
                depreciationMethod("14")
                counter = counter + 1
                break
                
    for x in depreciationNumList:
        print(x)
    return depreciationNumList
#getDepreciation(listoffiles)
#getDepreciation(secondListoffiles)


# cashflow not done yet, will come back to finish
def getCashFlow():
    cashFlowList = []
    ammortizationList = getAmortization()
    interestList = getInterest()
    depreciationList = getDepreciation()

    cashFlowList.append(
        ammortizationList[0] + interestList[0] + depreciationList[0])

    print(ammortizationList[0], interestList[0], depreciationList[0])
    print(cashFlowList[0])
# cash from sales 1c.


def getCashFromSales(fileList):
    cashFromSalesPages = []
    cashFromSalesList = []
    counter = 0

    for file in fileList:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text()
            if "c Balance. Subtract line 1b from line 1a " in currList:
                print("found", file)
                cashFromSalesPages.append(page.extract_text())
                break
            elif "cBalance. Subtract line 1b from line 1a" in currList:
                print("found", file)
            else:
                print("not found", file)
                break
    
    for x in range(0, len(cashFromSalesPages)):
        keepTrack = cashFromSalesPages[counter].split(" ").index("1c") + 1
        cashfromSales = cashFromSalesPages[counter].split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        cashFromSalesList.append(int(cashfromSales))
        counter = counter + 1
    
    for x in cashFromSalesList:
        print(x)
    return cashFromSalesList
getCashFromSales(secondListoffiles)
# gross cash income


def getGrossCashIncome():
    grossCashIncomePages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    grossCashIncomePages.append(page.extract_text())
    grossCashIncomeList = []
    counter = 1
    for x in range(1, len(grossCashIncomePages), 2):
        keepTrack = grossCashIncomePages[counter].split(" ").index("3") + 1
        grossCashIncome = grossCashIncomePages[counter].split(
            " ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        grossCashIncomeList.append(int(grossCashIncome))
        counter = counter + 2
    for x in grossCashIncomeList:
        print(x)
    return grossCashIncomeList
# cash operating expenses


def getCashOperatingExpenses():
    cashOperatingExpensesPages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    cashOperatingExpensesPages.append(page.extract_text())
    cashOperatingExpensesList = []
    counter = 1
    for x in range(1, len(cashOperatingExpensesPages), 2):
        keepTrack = cashOperatingExpensesPages[counter].split(
            " ").index("21") + 1
        cashOperatingExpense = cashOperatingExpensesPages[counter].split(
            " ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        cashOperatingExpensesList.append(int(cashOperatingExpense))
        counter = counter + 2
    for x in cashOperatingExpensesList:
        print(x)
    return cashOperatingExpensesList
# other income expensese


def getOtherIncomeExpenses():
    otherIncomeExpensesPages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    otherIncomeExpensesPages.append(page.extract_text())
    otherIncomeExpensesList = []
    counter = 1
    for x in range(1, len(otherIncomeExpensesPages), 2):
        keepTrack = otherIncomeExpensesPages[counter].split(" ").index("7") + 1
        cashOperatingExpense = otherIncomeExpensesPages[counter].split(
            " ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        # print(cashOperatingExpense, x)
        if "(cid:127)" in cashOperatingExpense:
            otherIncomeExpensesList.append(0)
        else:
            otherIncomeExpensesList.append(int(cashOperatingExpense))
        counter = counter + 2
    for x in otherIncomeExpensesList:
        print(x)
    return otherIncomeExpensesList
# net cash after operations


def getNetCashAfterOperations():
    netCashAfterOperationsPages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    netCashAfterOperationsPages.append(page.extract_text())
    netCashAfterOperationsList = []
    counter = 1
    for x in range(1, len(netCashAfterOperationsPages), 2):
        keepTrack = netCashAfterOperationsPages[counter].split(
            " ").index("penalties") - 1
        cashOperatingExpense = netCashAfterOperationsPages[counter].split(
            " ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        netCashAfterOperationsList.append(int(cashOperatingExpense))
        counter = counter + 2
    for x in netCashAfterOperationsList:
        print(x)
    return netCashAfterOperationsList


def getScheduleKLine13A():
    netCashAfterOperationsPages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "16c\nsnoitcasnarT\nForeign" and "level\ndPassive" in item:
                    print("found")
                    netCashAfterOperationsPages.append(page.extract_text())
    netCashAfterOperationsList = []
    counter = 1
    #got rid of the replace("-","")
    for x in range(1, len(netCashAfterOperationsPages), 2):
        keepTrack = netCashAfterOperationsPages[counter].split(
            " ").index("13a") + 1
        cashOperatingExpense = netCashAfterOperationsPages[counter].split(
            " ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        netCashAfterOperationsList.append(int(cashOperatingExpense))
        counter = counter + 2
    for x in netCashAfterOperationsList:
        print(x)
    return netCashAfterOperationsList


def getScheduleM1Line4B():
    netCashAfterOperationsPages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "7~~~~~~~~~~~~~\nbTravel" in item:
                    print("found")
                    netCashAfterOperationsPages.append(page.extract_text())
    netCashAfterOperationsList = []
    counter = 1
    for x in range(1, len(netCashAfterOperationsPages), 2):
        keepTrack = netCashAfterOperationsPages[counter].split(" ").index("7~~~~~~~~~~~~~\nbTravel") + 5
        #got rid of the replace("-","")
        cashOperatingExpense = netCashAfterOperationsPages[counter].split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        if int(cashOperatingExpense) == 9:
            cashOperatingExpense = netCashAfterOperationsPages[counter].split(" ")[keepTrack - 1].split("\n")[0].replace(",", "").replace(".", "")
            netCashAfterOperationsList.append(int(cashOperatingExpense))
        else:
            netCashAfterOperationsList.append(int(cashOperatingExpense))
        counter = counter + 2
    for x in netCashAfterOperationsList:
        print(x)
    return netCashAfterOperationsList
# m1 deductions comes from schedule k line 13a + schedule m1 line 4b, use two helper functions to get the result you need
# it works but one of the numbers dont add up, i belive its the original pdf sent to me because all other numbers add up
# will have to edit a little bit but it works as expected right now
def getM1Deductions():
    line13AList = getScheduleKLine13A()
    line4BList = getScheduleM1Line4B()
    m1DeductionsList = []
    for x, y in zip(line13AList,line4BList):
        sum = x + y
        m1DeductionsList.append(sum)
    print(m1DeductionsList)
    return m1DeductionsList
#getM1Deductions()
def getM2Deductions():
    netCashAfterOperationsPages = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "7~~~~~~~~~~~~~\nbTravel" in item:
                    print("found")
                    netCashAfterOperationsPages.append(page.extract_text())
    netCashAfterOperationsList = []
    counter = 1
    for x in range(1, len(netCashAfterOperationsPages), 2):
        keepTrack = netCashAfterOperationsPages[counter].split(" ").index("(itemize):\n3")
        cashOperatingExpense = netCashAfterOperationsPages[counter].split(" ")[keepTrack].split("\n")[1]
        if int(cashOperatingExpense) == 3:
            netCashAfterOperationsList.append(0)
        else:
            netCashAfterOperationsList.append(int(cashOperatingExpense))
        counter = counter + 2
    for x in netCashAfterOperationsList:
        print(x)
    return netCashAfterOperationsList

def getEndingCashPosition():
    netCashList = getNetCashAfterOperations()
    m1DeductionsList = getM1Deductions()
    m2DeductionsList = getM2Deductions()
    endingCashPositionList = []
    #was told that x y and z should be subtracted but i was getting the wrong numbers based on the excel sheet given so i changed to addition and numbers are accurate now
    for x,y,z in zip(netCashList,m1DeductionsList,m2DeductionsList):
        sum = x - y - z
        endingCashPositionList.append(sum)
    print("Ending cash position list:", endingCashPositionList)
    return endingCashPositionList
#getEndingCashPosition()

def getCashFlow():
    endingCashPositionList = getEndingCashPosition()
    depreciationList = getDepreciation()
    amortizationList = getAmortization()
    interestList = getInterest()
    netcashlist = getNetCashAfterOperations()
    cashFlowList = []

    for x,y,z,p in zip(endingCashPositionList,depreciationList,amortizationList,interestList):
        sum = x + y + z + p
        cashFlowList.append(sum)
    print("net cash list:",netcashlist)
    print("ending cash position list:", endingCashPositionList)
    print("depreciation list:", depreciationList)
    print("amortization list:", amortizationList)
    print("interest list:", interestList)
    print("Cash flow list:", cashFlowList)

# pdf = pdfplumber.open(listoffiles[1])
# page = pdf.pages[21].extract_text().split(" ")
# indextorecall = pdf.pages[21].extract_text().split(" ").index("(itemize):\n3")
# #depreciation = pdf.pages[21].extract_text().split(" ")[indextorecall].split("\n")[0].replace(",", "").replace(".", "").replace("-", "")
# depreciation = pdf.pages[21].extract_text().split(" ")[indextorecall].split("\n")[0].index(":") + 1
# if int(pdf.pages[21].extract_text().split(" ")[indextorecall].split("\n")[1]) == 3:
#     print("number")
# else:
#     print(0)
#print(pdf.pages[21].extract_text().split(" ")[indextorecall].split("\n"))
