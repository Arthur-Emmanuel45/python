#!/bin/bash
#defing a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
#To access apple
print(myFruitList[0])

#To access banana
print(myFruitList[1])

#To access cherry
print(myFruitList[2])

#Changing values in list
#To change cherry to orange
myFruitList[2] = "orange"

#Defining a tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)

#Accessing a tuple by position
#To access apple
print(myFinalAnswerTuple[0])

#To access banana
print(myFinalAnswerTuple[1])

#To access cherry
print(myFinalAnswerTuple[2])

#Defining a dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#To access Akua's favorite fruit
print(myFavoriteFruitDictionary["Akua"])

#To access Saanvi's favorite fruit
print(myFavoriteFruitDictionary["Saanvi"])

#To access Paulo's favorite fruit
print(myFavoriteFruitDictionary["Paulo"])
