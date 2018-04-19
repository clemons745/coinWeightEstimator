#! /usr/bin/python3

# Test getCoinInventory

from coinEstimator import *

coinWeight = {'quarters': 1451.52,
              'dimes': 335.664,
              'nickels': 4485,
              'pennies': 57.5}

coinInventory = {'quarters': 256,
                 'dimes': 148,
                 'nickels': 897,
                 'pennies': 23}

assert getCoinInventory(coinWeight) == coinInventory

# Test getCoinValue

coinValue = {'quarters': 64,
              'dimes': 14.80,
              'nickels': 44.85,
              'pennies': 0.23}

assert getCoinValue(coinInventory) == coinValue

# Test getWrapperInventory

wrappersNeeded = {'quarters': 7,
                  'dimes': 3,
                  'nickels': 23,
                  'pennies': 1}

assert getWrapperInventory(coinInventory) == wrappersNeeded