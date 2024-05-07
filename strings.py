#!/bin/bash
#string data type
myString="This is a string."
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

#concatenating a string
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#working with input strings
name = input("What is your name? ")
print(name)

#Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}".format(name, color, animal))
