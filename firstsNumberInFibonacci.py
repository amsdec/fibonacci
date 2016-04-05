#!/usr/bin/python
#coding=UTF-8

numbersInTheSerie = int(input("Cantidad de números: "))
if numbersInTheSerie < 1:
  print "Debe de ser un número entero mayor a 0"
  exit()
def fibonacci(number):
  if number <= 1:
    return 0
  if number == 2:
    return 1
  return fibonacci(number-1) + fibonacci(number-2)

number = 1
while number <= numbersInTheSerie:
  print fibonacci(number)
  number = number+1

