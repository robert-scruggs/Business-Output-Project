import pdfplumber
listoffiles = ['report/pfs/2_PFS_JAMEY CUTTER_052018s.pdf','report/pfs/2_PFS_N MERAIYA FEB 2018.pdf']


# pdf = pdfplumber.open(listoffiles[0])
# print(pdf.pages[0].extract_text()
#       .replace("_","")
#     #   .replace("…","")
#       .replace(".","")
#       .replace("\n"," ")
#       .split(" ")
#     )

# indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Bonds…………………………………$")
# print(pdf.pages[0].extract_text()
#       .replace("_","")
#     #   .replace("…","")
#       .replace(".","")
#       .replace("\n"," ")
#       .split(" ")[indexRightAfterBonds + 1]
#     )




def getCashOnHand(fileList):
    myList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterCash = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Cash")
        cashNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterCash - 1]
        if cashNumber == '':
            myList.append(0)
        else:
            myList.append(int(cashNumber))
    return myList

def getSavingsAccount(fileList):
    myList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterCash = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Accounts…………………………………$")
        cashNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterCash + 1]
        if cashNumber == '':
            myList.append(0)
        else:
            myList.append(int(cashNumber))
    return myList

def getCash():
    cashOnHandList = getCashOnHand(listoffiles)
    savingsAccountList = getSavingsAccount(listoffiles)
    cashList = []
    for x, y in zip(cashOnHandList,savingsAccountList):
        sum = x + y
        cashList.append(sum)
    return cashList


def getMarketableSecurities(fileList):
    marketableSecuritiesList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Bonds…………………………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ")[indexRightAfterBonds + 1]
        if stocksAndBondsNumber == '':
            marketableSecuritiesList.append(0)
        else:
            marketableSecuritiesList.append(int(stocksAndBondsNumber))
    return marketableSecuritiesList

def getTotalLiquidAssets():
    totalLiquidAssetList = []
    cashList = getCash()
    marketableSecuritiesList = getMarketableSecurities(listoffiles)
    for x, y in zip(cashList,marketableSecuritiesList):
        sum = x + y
        totalLiquidAssetList.append(sum)

    return totalLiquidAssetList

def getPrimaryResidence(fileList):
    #real estate
    primarResidenceList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Estate…………………………………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 2]
        if stocksAndBondsNumber == '':
            primarResidenceList.append(0)
        else:
            primarResidenceList.append(int(stocksAndBondsNumber))
    return primarResidenceList

def getIRA(fileList):
    #ira or other retirement account
    iraList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Account………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
        if stocksAndBondsNumber == '':
            iraList.append(0)
        else:
            iraList.append(int(stocksAndBondsNumber))
    return iraList

def getLifeInsurance(fileList):
    #life insurance
    lifeInsurance = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Only……$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
        if stocksAndBondsNumber == '':
            lifeInsurance.append(0)
        else:
            lifeInsurance.append(int(stocksAndBondsNumber))
    return lifeInsurance


def getNotesReceivable(fileList):
    #accounts & notes receivable
    notesReceivableList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Receivable……………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
        if stocksAndBondsNumber == '':
            notesReceivableList.append(0)
        else:
            notesReceivableList.append(int(stocksAndBondsNumber))
    return notesReceivableList

def getBusinessValues(fileList):
    #other assets
    businessValuesList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Assets…………………………………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 3]
        if stocksAndBondsNumber == '':
            businessValuesList.append(0)
        else:
            businessValuesList.append(int(stocksAndBondsNumber))
    return businessValuesList

def getAutomobiles(fileList):
    #automobiles
    automobilesList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        try:
            indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Automobiles…………………………………………$")
            stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 1]
            if stocksAndBondsNumber == '':
                automobilesList.append(0)
            else:
                automobilesList.append(int(stocksAndBondsNumber))
        except:
                automobilesList.append(0)
    return automobilesList

def getPersonalProperty(fileList):
    #automobiles
    personalProperyList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        try:
            indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Property……………………………$")
            stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 3]
            if stocksAndBondsNumber == '':
                personalProperyList.append(0)
            else:
                personalProperyList.append(int(stocksAndBondsNumber))
        except:
                personalProperyList.append(0)
    return personalProperyList

def getTotalOtherAssets(fileList):
    totalOtherAssetsList = []
    iraList = getIRA(listoffiles)
    lifeInsuranceList = getLifeInsurance(listoffiles)
    notesReceivableList = getNotesReceivable(listoffiles)
    businessValuesList = getBusinessValues(listoffiles)
    automobilesList = getAutomobiles(listoffiles)
    personalPropertyList = getPersonalProperty(listoffiles)

    for a, b, c, d, e ,f in zip(notesReceivableList,lifeInsuranceList,iraList,businessValuesList,automobilesList,personalPropertyList):
        sum = a + b + c + d + e + f
        totalOtherAssetsList.append(sum)
    return totalOtherAssetsList

def getTotalAssets(fileList):
    totalAssetsList = []
    totalOtherAssetsList = getTotalOtherAssets(listoffiles)
    primaryResidenceList = getPrimaryResidence(listoffiles)
    totalLiquidAssetsList = getTotalLiquidAssets()

    for a, b, c in zip(totalOtherAssetsList,primaryResidenceList,totalLiquidAssetsList):
        sum = a + b + c
        totalAssetsList.append(sum)
    return totalAssetsList


def getTotalREMortgage(fileList):
    #automobiles
    mortgageList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        try:
            indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Estate…………………$")
            stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
            if stocksAndBondsNumber == '':
                mortgageList.append(0)
            else:
                mortgageList.append(int(stocksAndBondsNumber))
        except:
                mortgageList.append(0)
    return mortgageList

def getAccountsPayable(fileList):
    #automobiles
    accountsPayableList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        try:
            indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Payable……………………………$")
            stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
            if stocksAndBondsNumber == '':
                accountsPayableList.append(0)
            else:
                accountsPayableList.append(int(stocksAndBondsNumber))
        except:
                accountsPayableList.append(0)
    return accountsPayableList

def getNotesPayable(fileList):
    #automobiles
    notesPayableList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        try:
            indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Others………$")
            stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
            if stocksAndBondsNumber == '':
                notesPayableList.append(0)
            else:
                notesPayableList.append(int(stocksAndBondsNumber))
        except:
                notesPayableList.append(0)
    return notesPayableList

def getInstallmentAccountsAuto(fileList):
    #automobiles
    installmentAccountsAutoList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        try:
            indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("(Auto)…………………$")
            stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 7]
            if stocksAndBondsNumber == '':
                installmentAccountsAutoList.append(0)
            else:
                installmentAccountsAutoList.append(int(stocksAndBondsNumber))
        except:
                installmentAccountsAutoList.append(0)
    return installmentAccountsAutoList

def getInstallmentAccountsOther(fileList):
    #automobiles
    installmentAccountsOtherList = []
    for file in fileList:
        pdf = pdfplumber.open(file)
        try:
            indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("(Other)………………$")
            stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 7]
            if stocksAndBondsNumber == '':
                installmentAccountsOtherList.append(0)
            else:
                installmentAccountsOtherList.append(int(stocksAndBondsNumber))
        except:
                installmentAccountsOtherList.append(0)
    return installmentAccountsOtherList

def getInstallmentAccounts(fileList):
    #automobiles
    installmentAccountsList = []
    totalOtherAssetsList = getInstallmentAccountsAuto(listoffiles)
    primaryResidenceList = getInstallmentAccountsOther(listoffiles)

    for a, b in zip(totalOtherAssetsList,primaryResidenceList):
        sum = a + b
        installmentAccountsList.append(sum)
    return installmentAccountsList

def getTotalLiabilities():

    totalLiabilitiesList = []
    totalREMortageList = getTotalREMortgage(listoffiles)
    accountsPayableList = getAccountsPayable(listoffiles)
    notesPayableList = getNotesPayable(listoffiles)
    installmentAccountsList = getInstallmentAccounts(listoffiles)

    for a, b, c, d in zip(totalREMortageList,accountsPayableList,notesPayableList,installmentAccountsList):
        sum = a + b + c + d
        totalLiabilitiesList.append(sum)
    return totalLiabilitiesList

def getNetWorth():

    netWorthList = []
    totalAssetsList = getTotalAssets(listoffiles)
    totalLiabilities = getTotalLiabilities()

    for a, b in zip(totalAssetsList,totalLiabilities):
        sum = a - b
        netWorthList.append(sum)
    return netWorthList

def getAbsoluteTotal():
    #this total is the same as total assets but im gonna rewrite it just because
    absoluteTotal = getTotalAssets(listoffiles)
    return absoluteTotal
print(getAbsoluteTotal())