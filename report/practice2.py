import PyPDF2
import pdfplumber

listoffiles = ["6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf",
               "6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf",
               "6_2015 Income Tax Return_ CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf",
               "6_2015 Income Tax Return_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf",
               "6_2016 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf",
               "6_2016 Income Tax Return_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf",
               "6_2017_CRG Amended 2017 Taxes.pdf",
               "6_2017_CHR Amended 2017 Taxes.pdf"]


# amortization
def getAmortization():
    myList = []
    for file in listoffiles:
        pdf = pdfplumber.open(file)
        for page in pdf.pages:
            currList = page.extract_text().split(" ")
            for item in currList:
                if "Amortization(a)\n(b)" and "Amortizable" in item:
                    print("found")
                    myList.append(page.extract_text())
    ammortizationList = []
    counter = 1
    for x in range(1, len(myList), 2):
        keepTrack = myList[counter].split(" ").index("44") + 1
        amortization = myList[counter].split(" ")[keepTrack].split("\n")[
            0].replace(",", "").replace(".", "")
        ammortizationList.append(amortization)
        counter = counter + 2

    for x in ammortizationList:
        print(x)


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
        interestList.append(interest)
        counter = counter + 2

    for x in interestList:
        print(x)


# depreciation
pdf = pdfplumber.open(listoffiles[1])
page = pdf.pages[17].extract_text().split(" ")
indextorecall = pdf.pages[17].extract_text().split(" ").index("16a") + 1
depreciation = pdf.pages[17].extract_text().split(" ")[indextorecall].split("\n")[
    0].replace(",", "").replace(".", "")
print(depreciation)
