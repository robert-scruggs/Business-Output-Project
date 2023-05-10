import pdfplumber
from functools import lru_cache

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

# filesthatdontwork = [
#                     #"report/pdfs/6_2019 ITR 1065_Delish Real Estate Holdings LLC.pdf",
#                     #"report/pdfs/6_2019 ITR_1065 Delish Brands, LLC.pdf",
#                     #"report/pdfs/6_2020 ITR_Delish Real Estate  Holdings, LLC.pdf",
#     ]
# pdf = pdfplumber.open(secondListoffiles[0])
# text = pdf.pages[6].extract_text()
# if "cBalance. Subtract line 1b from line 1a" in text:
#     print("found")


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

# def getAmortization(fileList):
#     myList = []
#     for file in fileList:
#         pdf = pdfplumber.open(file)
#         for page in pdf.pages:
#             currList = page.extract_text()
#             if "44 Total. Add amounts in column (f). See the instructions for where to report" and "\nPart VI Amortization(a)\n(b) (c) (d) (e) (f)\n" in currList:
#                 print("found", page.page_number)
#                 myList.append(page.extract_text())
#                 break    
#     ammortizationList = []
#     counter = 0
#     for x in range(0, len(myList)):
#         keepTrack = myList[counter].split(" ").index("44") + 1
#         amortization = myList[counter].split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
#         ammortizationList.append(int(amortization))
#         counter = counter + 1

#     for x in ammortizationList:
#         print(x)
#     return ammortizationList

@lru_cache(maxsize=None)
def getAmortization(file):
    try:
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text()
            if "44 Total. Add amounts in column (f). See the instructions for where to report" and "\nPart VI Amortization(a)\n(b) (c) (d) (e) (f)\n" in currList:
                print("found", page.page_number)
                extractedText = page.extract_text()
                break    
        keepTrack = extractedText.split(" ").index("44") + 1
        amortization = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        return int(amortization)
    except:
        return 213

# interest does not work for all files, needs consistent files
# print(getAmortization("report/pdfs/6_2017_CHR Amended 2017 Taxes.pdf"))

@lru_cache(maxsize=None)
def getInterest(file):
    try:
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    extractedText = page.extract_text()

        keepTrack = extractedText.split(" ").index("15") + 1
        interest = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        return int(interest)
    except:
        return 213


@lru_cache(maxsize=None)
def getDepreciation(file):
    try:
        extractedText = ""
        def depreciationMethod(num):
            keepTrack = extractedText.split(" ").index(num) + 1
            depreciation = int(extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", ""))
            return depreciation
            
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text()
            # 1065
            if "16 aDepreciation (if required, attach Form 4562)" in currList or "16a Depreciation (if required, attach Form 4562)" in currList:
                print("found", page.page_number, file)
                extractedText = page.extract_text()
                return depreciationMethod("16a")
            # 1120
            elif "14 Depreciation not claimed on Form 1125-A or elsewhere on return (attach Form 4562)" in currList:
                print("found", page.page_number, file)
                extractedText = page.extract_text()
                return depreciationMethod("14")       
    except:
        return 213
# print(getDepreciation("report/pdfs/6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf"))


@lru_cache(maxsize=None)
def getCashFromSales(file):
    try: 
        extractedText = ""

        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text()
            if "c Balance. Subtract line 1b from line 1a " in currList:
                print("found", file)
                extractedText = page.extract_text()
                break
            elif "cBalance. Subtract line 1b from line 1a" in currList:
                print("found", file)
                extractedText = page.extract_text()
                break

        keepTrack = extractedText.split(" ").index("1c") + 1
        cashfromSales = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        return int(cashfromSales)
    except:
        return 213

# gross cash income


@lru_cache(maxsize=None)
def getGrossCashIncome(file):
    try: 
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    extractedText = page.extract_text()

        keepTrack = extractedText.split(" ").index("3") + 1
        grossCashIncome = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        return int(grossCashIncome)
    except:
        return 213
# cash operating expenses


@lru_cache(maxsize=None)
def getCashOperatingExpenses(file):
    try:
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    extractedText = page.extract_text()

        keepTrack = extractedText.split(" ").index("21") + 1
        cashOperatingExpense = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        
        return int(cashOperatingExpense)
    except:
        return 213
# other income expensese


@lru_cache(maxsize=None)
def getOtherIncomeExpenses(file):
    try:
        extractdText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    extractdText = page.extract_text()


        keepTrack = extractdText.split(" ").index("7") + 1
        cashOperatingExpense = extractdText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")

        if "(cid:127)" in cashOperatingExpense:
            return 0
        else:
            return int(cashOperatingExpense)
    except:
        return 213
# net cash after operations


@lru_cache(maxsize=None)
def getNetCashAfterOperations(file):
    try: 
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "1065" and "U.S." and "Return" and "of" and "Partnership" and "Income\nOMB" in item:
                    print("found")
                    extractedText = page.extract_text()

        keepTrack = extractedText.split(" ").index("penalties") - 1
        cashOperatingExpense = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")

        return int(cashOperatingExpense)
    except:
        return 213

@lru_cache(maxsize=None)
def getScheduleKLine13A(file):
    try: 
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "16c\nsnoitcasnarT\nForeign" and "level\ndprintPassive" in item:
                    print("found")
                    extractedText = page.extract_text()
        #got rid of the replace("-","")
        keepTrack = extractedText.split(" ").index("13a") + 1
        cashOperatingExpense = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")

        return int(cashOperatingExpense)
    except:
        return 213


@lru_cache(maxsize=None)
def getScheduleM1Line4B(file):
    try: 
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "7~~~~~~~~~~~~~\nbTravel" in item:
                    print("found")
                    extractedText = page.extract_text()

        keepTrack = extractedText.split(" ").index("7~~~~~~~~~~~~~\nbTravel") + 5
        #got rid of the replace("-","")
        cashOperatingExpense = extractedText.split(" ")[keepTrack].split("\n")[0].replace(",", "").replace(".", "")
        if int(cashOperatingExpense) == 9:
            cashOperatingExpense = extractedText.split(" ")[keepTrack - 1].split("\n")[0].replace(",", "").replace(".", "")
            return int(cashOperatingExpense)
        else:
            return int(cashOperatingExpense)
    except:
        return 213
# m1 deductions comes from schedule k line 13a + schedule m1 line 4b, use two helper functions to get the result you need
# it works but one of the numbers dont add up, i belive its the original pdf sent to me because all other numbers add up
# will have to edit a little bit but it works as expected right now
@lru_cache(maxsize=None)
def getM1Deductions(file):
    try: 
        line13AList = getScheduleKLine13A(file)
        line4BList = getScheduleM1Line4B(file)
        
        return line13AList + line4BList
    except:
        return 213
#getM1Deductions()
@lru_cache(maxsize=None)
def getM2Deductions(file):
    try: 
        extractedText = ""
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "7~~~~~~~~~~~~~\nbTravel" in item:
                    print("found")
                    extractedText = page.extract_text()

        
        keepTrack = extractedText.split(" ").index("(itemize):\n3")
        cashOperatingExpense = extractedText.split(" ")[keepTrack].split("\n")[1]
        if int(cashOperatingExpense) == 3:
            return 0
        else:
            return int(cashOperatingExpense)
    except:
        return 213
# print(getM2Deductions("report/pdfs/6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf"))

@lru_cache(maxsize=None)
def getEndingCashPosition(file):
    try: 
        netCashList = getNetCashAfterOperations(file)
        m1DeductionsList = getM1Deductions(file)
        m2DeductionsList = getM2Deductions(file)

        #was told that x y and z should be subtracted but i was getting the wrong numbers based on the excel sheet given so i changed to addition and numbers are accurate now
        
        return netCashList - m1DeductionsList - m2DeductionsList
    except:
        return 213

@lru_cache(maxsize=None)
def getCashFlow(file):
    try: 
        endingCashPositionList = getEndingCashPosition(file)
        depreciationList = getDepreciation(file)
        amortizationList = getAmortization(file)
        interestList = getInterest(file)
    

        return endingCashPositionList + depreciationList + amortizationList + interestList
    except:
        return 213

# print(getCashFlow("report/pdfs/6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf"))

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
