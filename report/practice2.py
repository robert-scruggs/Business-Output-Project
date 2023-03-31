import PyPDF2
import pdfplumber

listoffiles = ["6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf","6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf","6_2015 Income Tax Return_ CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf","6_2015 Income Tax Return_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf"]
myList = []
pdf = pdfplumber.open("6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf")
pdf2 = pdfplumber.open("6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf")
#print(pdf2.pages[25].extract_text().split(" "))
# print("\n")
#print(pdf.pages[67].extract_text().split(" "))
for file in listoffiles:
    pdf = pdfplumber.open(file)
    for page in pdf.pages:
        currList = page.extract_text().split(" ")
        for item in currList:
            if "Amortization(a)\n(b)" and "Amortizable" in item:
                print("found")
                myList.append(page.extract_text())
                break;
ammortizationList = []
counter = 1
for x in range(1, len(myList), 2):
     keepTrack = myList[counter].split(" ").index("44") + 1
     amortization = myList[counter].split(" ")[keepTrack].split("\n")[0].replace(",","").replace(".","")
     ammortizationList.append(amortization)
     counter = counter + 2

for x in ammortizationList:
    print(x)

# keepTrack = myList[1].split(" ").index("44") + 1
# keepTrack2 = myList[3].split(" ").index("44") + 1
# amortization = myList[1].split(" ")[keepTrack].split("\n")[0].replace(",","").replace(".","")
# amortization2 = myList[3].split(" ")[keepTrack2].split("\n")[0].replace(",","").replace(".","")




