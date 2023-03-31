from PyPDF2 import PdfReader
import re

listoffiles = ["6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf",
               "6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf"]
pages = []

currFile = "6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf"
reader = PdfReader(currFile)
currFile2 = "6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf"
reader2 = PdfReader(currFile2)

splitText = reader.pages[67].extract_text().split(" ")
amortizationIndex = reader.pages[67].extract_text().split(
    " ").index("901.\n19,874.\n22,029.\n11530319")
finalResult = splitText[amortizationIndex].split("\n")[2].replace(".", "")

splitText2 = reader2.pages[25].extract_text().split(" ")
print(splitText)
print("\n")
print(splitText2)
#amortizationIndex2 = reader2.pages[57].extract_text().split(" ").index("26-3047014\n16,404.\n16,404.\n11440320")
# finalResult2 = splitText2[amortizationIndex].split("\n")[2].replace(".","")
#58!!!!!!!!!!
# getting text from amortization page in income tax return cutter restaraunt group llc
#print(splitText2)

#for page in reader2.pages:
    #if "44 Total." in page.extract_text():
        #print("found")
    #else:
        #print("not found")


# for file in listoffiles:
#    currFile = open(file,"rb")
#    reader = PdfReader(currFile)

#    for page in reader.pages:
#        if "Amortization" in page.extract_text():
#            pages.append(page.extract_text())
# print(pages[0].split(" ").index("26-3047014\n-105,310.\n-105,310.\n83,242."))
# print(pages[0].split(" "))
# print("\n")
# print(pages[2].split(" "))
# print(pages[1].split(" ").index("26-3047014\n-105,310.\n-105,310.\n83,242."))


# file = open("6_2014_CUTTER HIGHLANDS RANCH, LLC 1065 CLNT.pdf", "rb")
# file2 = open("6_2014 Income Tax Return_CUTTER RESTAURANT GROUP, LLC 1065 CLNT.pdf", "rb")

# reader = PdfReader(file)
# reader2 = PdfReader(file2)
# page = reader.pages[22]
# print(page.extract_text())
# text = reader.pages[53].extract_text().split(" ")
# text2 = reader2.pages[63].extract_text().split(" ")
# number = text.index("26-3047014\n-105,310.\n-105,310.\n83,242.")
# number2 = text2.index("26-0555883\n-275,247.\n-275,247.\n37,629.")
# finalNumber = text[number].split("\n")[1]
# finalNumber2 = text2[number2].split("\n")[1]
# actualFinalNumber = finalNumber.replace("-","").replace(".","").replace(",","")
# print(text.__len__())
# print("\n")
# print("\n")
# print(finalNumber)
# print(finalNumber2)
# print("\n")
# print("\n")
# print(text2.__len__())
