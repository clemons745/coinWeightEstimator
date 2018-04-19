#! /usr/bin/python3

#####
#
# Name: coinEstimator.py
#
# Description: Input weight of coins in either grams or pounds,
# and return how many wrappers they will need, how much money they have,
# how many coins they have.
#
# Version: 0.1dev
#
# Date: 4/18/2018
#
# Author: Tony Clemons (clemons745@gmail.com)
#
#####

# Ask the user to enter the weight of each type of coin


def getWeight():
    # This function asks the user their weight of each coin
    # Returns a dict of the weight of each coin

    # Create the Dictionary
    coinWeight = {}

    # Ask if they want to enter the weight in grams or pounds
    print('''Would you like to enter the weight in grams, or pounds?
1 Grams
2 Pounds

Selection: ''', end='')
    while True:
        try:
            unitSelection = int(input())
        except ValueError:
            print('Please enter a valid selection: ', end='')
            continue
        if unitSelection < 1 or unitSelection > 2:
            print('Please enter a valid selection: ', end='')
            continue
        elif unitSelection == 1 or unitSelection == 2:
            break
        else:
            raise Exception('This should not have happened')

    try:
        print('\nEnter the weight of each coin type.')
        print('Quarters: ', end='')
        coinWeight['quarters'] = float(input())
        print('Dimes: ', end='')
        coinWeight['dimes'] = float(input())
        print('Nickels: ', end='')
        coinWeight['nickels'] = float(input())
        print('Pennies: ', end='')
        coinWeight['pennies'] = float(input())
    except ValueError:
        raise Exception('You must enter a number.')

    # If the user entered the weight in pounds, convert it to grams
    if unitSelection == 2:
        coinWeight = poundsToGrams(coinWeight)
    return coinWeight


# If they enter the value in pounds, convert it to grams for calculations


def poundsToGrams(coinWeight):
    # This function converts the dictionary of weight to grams

    for i in coinWeight.keys():
        coinWeight[i] *= 453.59237
    return coinWeight


# Calculate how many of each coin they have


def getCoinInventory(coinWeight):
    coinInventory = {'quarters': 0,
                     'dimes': 0,
                     'nickels': 0,
                     'pennies': 0}

    coinInventory['quarters'] = coinWeight['quarters'] / 5.670
    coinInventory['dimes'] = coinWeight['dimes'] / 2.268
    coinInventory['nickels'] = coinWeight['nickels'] / 5.000
    coinInventory['pennies'] = coinWeight['pennies'] / 2.500
    return coinInventory


# Calculate the value of the money they have


def getCoinValue(coinInventory):
    coinValue = {'quarters': 0.0,
                 'dimes': 0.0,
                 'nickels': 0.0,
                 'pennies': 0.0}

    coinValue['quarters'] = coinInventory['quarters'] * 0.25
    coinValue['dimes'] = coinInventory['dimes'] * 0.10
    coinValue['nickels'] = coinInventory['nickels'] * 0.05
    coinValue['pennies'] = coinInventory['pennies'] * 0.01
    return coinValue


# Calculate how many wrappers they will need for each coin type


def getWrapperInventory(coinInventory):
    coinWrappersNeeded = {'quarters': 0,
                          'dimes': 0,
                          'nickels': 0,
                          'pennies': 0}

    if coinInventory['quarters'] % 40 == 0:
        coinWrappersNeeded['quarters'] = coinInventory['quarters'] / 40
    elif coinInventory['quarters'] % 40 > 0:
        coinWrappersNeeded['quarters'] = int(coinInventory['quarters']/40)+1
    else:
        raise Exception('Error when calculating wrappers needed for quarters')

    if coinInventory['dimes'] % 50 == 0:
        coinWrappersNeeded['dimes'] = coinInventory['dimes'] / 50
    elif coinInventory['dimes'] % 50 > 0:
        coinWrappersNeeded['dimes'] = int(coinInventory['dimes'] / 50) + 1
    else:
        raise Exception('Error when calculating wrappers needed for dimes')

    if coinInventory['nickels'] % 40 == 0:
        coinWrappersNeeded['nickels'] = coinInventory['nickels'] / 40
    elif coinInventory['nickels'] % 40 > 0:
        coinWrappersNeeded['nickels'] = int(coinInventory['nickels'] / 40) + 1
    else:
        raise Exception('Error when calculating wrappers needed for nickels')

    if coinInventory['pennies'] % 50 == 0:
        coinWrappersNeeded['pennies'] = coinInventory['pennies'] / 50
    elif coinInventory['pennies'] % 50 > 0:
        coinWrappersNeeded['pennies'] = int(coinInventory['pennies'] / 50) + 1
    else:
        raise Exception('Error when calculating wrappers needed for pennies')

    return coinWrappersNeeded


def printCoinInventory(coinInventory):
    print()
    print('Quarters: %s' % coinInventory['quarters'])
    print('Dimes: %s' % coinInventory['dimes'])
    print('Nickels: %s' % coinInventory['nickels'])
    print('Pennies: %s' % coinInventory['pennies'])


def printCoinValue(coinValue):
    total = 0.0

    for i in coinValue.keys():
        total += coinValue[i]

    print()
    print('Quarters: %s' % coinValue['quarters'])
    print('Dimes: %s' % coinValue['dimes'])
    print('Nickels: %s' % coinValue['nickels'])
    print('Pennies: %s' % coinValue['pennies'])
    print('Total: %s' % total)


def printWrappersNeeded(wrappersNeeded):
    print()
    print('Quarters: %s' % wrappersNeeded['quarters'])
    print('Dimes: %s' % wrappersNeeded['dimes'])
    print('Nickels: %s' % wrappersNeeded['nickels'])
    print('Pennies: %s' % wrappersNeeded['pennies'])


def main():
    import sys

    coinWeight = getWeight()
    coinInventory = getCoinInventory(coinWeight)
    wrappersNeeded = getWrapperInventory(coinInventory)
    coinValue = getCoinValue(coinInventory)

    while True:

        print('''\nWhat would you like to view?
1 Number of Coins
2 Value of Coins
3 Wrappers Needed
4 Quit
Selection: ''', end='')

        while True:
                try:
                    selection = int(input())
                except ValueError:
                    print('Please enter a valid selection: ', end='')
                    continue
                if selection < 1 or selection > 4:
                    print('Please enter a valid selection: ', end='')
                    continue
                elif selection >= 1 and selection <= 4:
                    break
                else:
                    raise Exception('Error while checking valid selection')

        if selection == 1:
            printCoinInventory(coinInventory)
        elif selection == 2:
            printCoinValue(coinValue)
        elif selection == 3:
            printWrappersNeeded(wrappersNeeded)
        elif selection == 4:
            sys.exit()
        else:
            raise Exception('Error occured while processing selection')


if __name__ == '__main__':
    main()
