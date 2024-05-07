#!/bin/bash
#Create a mixed-type-list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#printing list using for loop
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
