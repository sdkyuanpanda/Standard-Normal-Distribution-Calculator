#!/usr/bin/python3.7
###########################################################################################################
# This program is part of Standard Normal Distribution Calculator
#
# Standard Normal Distribution Calculator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Standard Normal Distribution Calculator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Standard Normal Distribution Calculator.  If not, see <https://www.gnu.org/licenses/>.
#
# Author:
#         Samuel Yuan
#         sdkyuan@gmail.com
#         09/21/2020
# 
###########################################################################################################

from scipy.integrate import quad
import numpy as np

#This is a cumulative distribution function which generates values for the Standard Deviation Table.
def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2*np.pi)
    return(constant * np.exp((-x**2) / 2.0))

def print_Help():
    print("This is a program that helps find a z-score or a percentile using the standard normal distribution table")
    print("The acceptable commands that can be used are: help, z-score, percentile, and quit. Acceptable commands are all in lowercase.")
    print("To find the z-score I used the function: (Value-Mean)/Standard Deviation.")
    print("To find the percentile I used a function to generate values of percentiles which are the same as the Standard Normal Distribution table.")
    print("Helpful articles: https://towardsdatascience.com/how-to-use-and-create-a-z-table-standard-normal-table-240e21f36e53 ")
    print("Thank you for using this program!")

def main():
    print("This is a program that helps find a z-score or a percentile using the standard normal distribution table.")
    print("Enter help for more details")
    print("Enter z-score to find the z-score")
    print("Enter percentile to find the percentile")

    while True:
        mode = input("Enter help, z-score, percentile, or quit:")
        realmode = str(mode)

        if realmode == "z-score":
            print("finding z-score...")
            print("Enter the  Value, then the mean, then the standard deviation")
            value = input("Enter Value:")
            mean = input("Enter Mean:")
            standardDeviation = input("Enter Standard Deviation:")
            try:
                realValue = float(value)
                realMean = float(mean)
                realStd = float(standardDeviation)
                partONE = realValue - realMean
                zScore = partONE / realStd
                print("The z-score of your data set is:", zScore)
            except:
                print("Invalid Input, please try again")

        elif realmode == "percentile":
            print("finding percentile...")
            print("Enter the Value, then the mean, then the standard deviation")
            valueforSnd = input("Enter Value:")
            meanforSnd = input("Enter Mean:")
            standardDevforSnd = input("Enter Standard Deviation:")
            try:
                realValuesnd = float(valueforSnd)
                realMeansnd = float(meanforSnd)
                realStdsnd = float(standardDevforSnd)
                partONEsnd = realValuesnd - realMeansnd
                sndplug = partONEsnd / realStdsnd
                userPercentile, _ = quad(normalProbabilityDensity, np.NINF, sndplug)
                print("The percentile of your data set is:", userPercentile)
                print("Would you like some additional info about your data set?")
                addInfo = input("Yes for more and no to cancel:")

                if addInfo == "Yes":
                    print("The value you put was:", realValuesnd)
                    print("The mean of your data set was:", realMeansnd)
                    print("The Standard Deviation of your data set was:", realStdsnd)
                    print("The z-score of your data set was:", sndplug)
                    print("The percentile of your data set is:", userPercentile)
                elif addInfo == "yes":
                    print("The value you put was:", realValuesnd)
                    print("The mean of your data set was:", realMeansnd)
                    print("The Standard Deviation of your data set was:", realStdsnd)
                    print("The z-score of your data set was:", sndplug)
                    print("The percentile of your data set is:", userPercentile)
                elif addInfo == "No":
                    print("No additional information given")
                elif addInfo == "no":
                    print("No additional information given")
                else:
                    print("Invalid Input, no additional information given")

            except ValueError:
                print("Invalid Input, please try again")

        elif realmode == "help":
            print_Help()
        elif realmode == "quit":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid Input, please try again")


if __name__ ==  "__main__":
   main()
