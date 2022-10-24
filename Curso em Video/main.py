# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from cev_exercises_world2 import Exercise36, Exercise37, Exercicio39, Exercicio44
from datetime import datetime

if __name__ == '__main__':
      try:
            practiceNum = int(input('Which practice would you like to test? [36-71]'))

            if practiceNum == 36:
                  housePrice = float(input('''What is the house's price in US dollar?'''))
                  buyerSalary = float(input('How much is your monthly wage in US dollar?'))
                  yearsToPay = float(input('How long do you want to pay in years?'))

                  approve = Exercise36(housePrice, buyerSalary, yearsToPay)

                  installment = approve.calcInstallment()
                  isApproved = approve.creditAnalysis(installment)

                  print(f'In order to pay a house of US$ {housePrice:.2f} in {yearsToPay} years, the monthly payments will be of US$ {installment:.2f}')

                  cutInstallment = buyerSalary*0.3

                  if isApproved:
                        print(f'''Since the monthly payments won't be more than 30% of your wage, which is US$ {cutInstallment:.2f}, your loan has been APPROVED.\nCongratulations!!!''')
                  else:
                        print(f'''We're sorry! Since the monthly payments will be more than 30% of your wage, which is US$ {cutInstallment:.2f}, your loan has been DENIED!!!''')
            elif practiceNum == 37:
                  numToConvert = int(input('Type an integer number to be converted:'))
                  conversionOptions = ''
                  detacher = '=-=' * 10

                  converter = Exercise37(numToConvert)
                  #by keeping this dictionary, our code will be cleaner, but it will decrese performance since all the listed functions will be ran.
                  """
                  converterFunctions = {
                        '1': converter.convertToBinary(),
                        '2': converter.convertToOctal(),
                        '3': converter.convertToHexa()
                  }
                  """
                  for key, value in converter.conversionDict.items():
                        conversionOptions += f'[{key}] to convert to {value}\n'

                  while True:
                        conversionBase = int(input(f'Pick one of the conversion bases listed bellow:\n{detacher}\n{conversionOptions}{detacher}\n'))

                        if conversionBase in (1, 2, 3):
                              chosenConversionBase = str(converter.conversionDict[str(conversionBase)])
                              print(f'You have chosen the {chosenConversionBase} base')
                              msg = f'{str(numToConvert)} converted to the {chosenConversionBase} base is '

                              #convertedNum = converterFunctions[str(conversionBase)]
                              #print(msg + '0' if convertedNum == '0' else msg + convertedNum.lstrip('0'))

                              #this block makes the code less cleaner but it would be better off in terms of performance, since it will run only the selected function
                              if conversionBase == 1:
                                    binary = converter.convertToBinary()
                                    print(msg + '0' if binary == '0' else msg + binary.lstrip('0'))
                                    break
                              elif conversionBase == 2:
                                    octal = converter.convertToOctal()
                                    print(msg + '0' if octal == '0' else msg + octal.lstrip('0'))
                                    break
                              elif conversionBase == 3:
                                    hexa = converter.convertToHexa()
                                    print(msg + '0' if hexa == '0' else msg + hexa.lstrip('0'))
                                    break
                        else:
                              print('Sorry.\nThe option you have picked is invalid.\nMake sure you choose a valid option')
            elif practiceNum == 39:

                  birthDate = input('Please, inform your birth date [dd/mm/yyyy]:')
                  enlist = Exercicio39(birthDate)

                  age = enlist.getAge()
                  enlistYear = enlist.getEnlistYear()
                  yToday = datetime.today().date().year

                  msg = f'Who has born in {birthDate[-4:]} is now {str(age)} years old'
                  if age < 18:
                        msg += f'\nDont worry. You are not obligated to enlist yet. Your mandatory enlistment will be only in {enlistYear}'
                  elif age == 18:
                        msg += f'\nYou have to enlist to the military this year'
                  else:
                        msg += f'\nYou should have enlisted yourself {yToday - enlistYear} years ago!'
                        msg += f'\nYour enlistment year was in {enlistYear}'
                  print(msg)

            elif practiceNum == 42:
                  l1 = float(input('Inform the 1st line:'))
                  l2 = float(input('Inform the 2nd line:'))
                  l3 = float(input('Inform the 3rd line:'))

                  if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
                        print('It is POSSIBLE to draw a triangle with the given lines!')
                        if l1 == l2 == l3:
                              print('The drawn triangle is EQUILATERAL.')
                        elif l1 in (l2, l3) or l2 in (l1, l3):
                              print('The drawn triangle is ISOSCELES.')
                        else:
                              print('The drawn triangle is SCALENE.')
                  else:
                        print('It is NOT POSSIBLE to draw a triangle with the given lines!')
            elif practiceNum == 44:
                  purchasePrice = float(input('Purchase price: '))

                  pymtMethsDict = {
                        '1': 'payment in cash or bank check',
                        '2': 'cash payment by card',
                        '3': '2x by card',
                        '4': '3x or more by card'
                  }

                  msg = 'Choose a payment method:\n'
                  for key, value in pymtMethsDict.items():
                        msg += f'[{key}] {value}\n'
                  pymtMeth = int(input(msg))
                  msg = ''

                  if pymtMeth == 1:
                        finalPrice = purchasePrice - (purchasePrice * 0.1)
                        msg = f'Your purchase will be in ${finalPrice} by cash or bank check considering 10% discount'
                  elif pymtMeth == 2:
                        finalPrice = purchasePrice - (purchasePrice * 0.05)
                        msg = f'Your purchase will be in ${finalPrice} by cash or bank check considering 5% discount'
                  elif pymtMeth == 3:
                        installment = purchasePrice / 2
                        finalPrice = purchasePrice
                        msg = f'Your purchase will be in two installments of ${installment} each'
                        msg += f'\nThe amount paid will be ${finalPrice} at the end'
                  elif pymtMeth == 4:
                        numOfInstallments = int(input('How many installments would you like to split the purchase off?'))
                        finalPrice = purchasePrice * 1.2
                        installment = finalPrice / numOfInstallments
                        msg = f'Your purchase will be in {numOfInstallments} installments of ${installment} each'
                        msg += f'\nThe amount paid will be ${finalPrice} at the end'
                  print(msg)



      except ZeroDivisionError:
            print('ERROR: there was a calculation error. The price of the house may not be zero')
      except ArithmeticError:
            print('ERROR: There was some arithmetical error. Please, check the value you typed!')
      except (ValueError, TypeError):
            print('ERROR: The data type you typed is invalid.')
      except KeyboardInterrupt:
            print('\nYou exited the application!')
      except Exception as e:
            print(e.__cause__)



