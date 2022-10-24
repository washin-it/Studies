from datetime import *
from dateutil.relativedelta import *

class Exercise36:
    global installment

    def __init__(self, housePrice, buyerSalary, yearsToPay):
        self.housePrice = housePrice
        self.buyerSalary = buyerSalary
        self.yearsToPay = yearsToPay

    def calcInstallment(self):
        monthsToPay = (self.yearsToPay*12)
        installment = self.housePrice / monthsToPay
        return installment


    def creditAnalysis(self, installment):
        x = lambda a: (a * 0.3) / float(installment)
        calcAppr = x(self.buyerSalary)
        approved = True if calcAppr >= 1 else False

        return approved

class Exercise37:

    def __init__(self, numToConvert):
        self.conversionDict = {
            '1': 'BINARY',
            '2': 'OCTAL',
            '3': 'HEXADECIMAL',
        }

        self.hexaDecimalDict = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }

        self.numToConvert = numToConvert


    def convertToBinary(self):
        convertedNum = ''
        binNum = []
        num = self.numToConvert

        if num > 0:
            while num > 1:
                binNum.append(num % 2)
                num //= 2
        else:
            num += 2**16
            while num > 1:
                binNum.append(num % 2)
                num //= 2

        binNum.append(num)
        binNum.reverse()

        for i in binNum:
            convertedNum += str(i)


        return convertedNum

    def convertToOctal(self):
        convertedNum = ''
        octNum = []
        num = self.numToConvert

        if num > 0:
            while num > 1:
                octNum.append(num % 8)
                num //= 8
        else:
            num += 2**16
            while num > 1:
                octNum.append(num % 8)
                num //= 8

        octNum.append(num)
        octNum.reverse()

        for i in octNum:
            convertedNum += str(i)

        return convertedNum

    def convertToHexa(self):
        convertedNum = ''
        hexNum = []
        num = self.numToConvert

        if num > 0:
            while num > 1:
                remain = num % 16
                hexNum.append(remain if remain < 10 else self.hexaDecimalDict[remain])
                num //= 16
        else:
            num += 2**32
            while num > 1:
                remain = num % 16
                hexNum.append(remain if remain < 10 else self.hexaDecimalDict[remain])
                num //= 16

        hexNum.append(num)
        hexNum.reverse()

        for i in hexNum:
            convertedNum += str(i)

        return convertedNum

class Exercicio39:

    def __init__(self, birthDate):
        def calcAge(birthDate):
            birthDate = datetime.strptime(birthDate, '%d/%m/%Y')
            today = datetime.today().date()

            age = relativedelta(today, birthDate).years
            yearsToEnlist = (18 - age)
            enlistYear = (today.year + yearsToEnlist)

            return age, enlistYear

        self.birthDate = birthDate
        self.age, self.enlistYear = calcAge(self.birthDate)

    def getAge(self):
        return self.age
    def getEnlistYear(self):
        return self.enlistYear


class Exercicio44:
    def __init__(self, purchasePrice, pymtMeth, numOfInstallments):
        self.purchasePrice = purchasePrice
        self.pymtMeth = pymtMeth
        self.numOfInstallments = numOfInstallments

    def getFinalPrice(self):
        purchasePrice = self.purchasePrice
        pymtMeth = self.pymtMeth
        numOfInstallments = self.numOfInstallments

        if pymtMeth == 1:
            finalPrice = purchasePrice - (purchasePrice * 0.1)
            msg = f'Your purchase will be in {finalPrice} by cash or bank check considering 10% discount'
        elif pymtMeth == 2:
            finalPrice = purchasePrice - (purchasePrice * 0.05)
            msg = f'Your purchase will be in {finalPrice} by cash or bank check considering 5% discount'
        elif pymtMeth == 3:
            installment = purchasePrice / 2
            msg = f'Your purchase will be in two installments of ${installment} each'
        elif pymtMeth == 4:
            finalPrice = purchasePrice * 1.2
            installment = finalPrice / numOfInstallments
            msg = f'Your purchase will be in {numOfInstallments} installments of ${installment} each'
            msg += f'\nYour amount paid will be ${finalPrice} at the end'

        return finalPrice, installment, msg




class CustomExceptions(Exception):
    pass

class NonExistentOptionError(CustomExceptions):
    pass