'''
Mean, Median, Mode, and Standard Deviation.

MEAN    : Sum all values, and divide the sum by the number of values
MEDIAN  : Value in the middle after you sort of the value 
          (if there are two numbers in the middle, divide the sum of those numbers by 2)
MODE    : Value thay appears most number of the times
Standard Deviation  : is a number that describes how spread out the values are
Variance    : is another number that indicates how spread out the values are
              (The variance is the average number of the squared differences)
'''
from scipy import stats
import numpy

numbers = [98,22,45,67,83,45,12,98,54,45,67,78]
mean = numpy.mean(numbers)
median = numpy.median(numbers)
mode = stats.mode(numbers)
variance = numpy.var(numbers)
sd = numpy.std(numbers)

print("Numbers : [98,22,45,67,83,45,12,98,54,45,67,78]")
print("Mean value from the numbers :",mean)
print("Median value from the numbers :",median)
print(mode)
print("Variance value from the numbers :",variance)
print("Standard Deviation value from the numbers :",sd)


