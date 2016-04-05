#!/usr/bin/python
#coding=UTF-8

number = int(input("Número: "))
if number < 0:
  print "Número inválido, no puede ser negativo"
  exit()
if number == 0:
  print number
  exit()
fibonacci = [0,1]
nextFibonacciNumber = fibonacci[-1] + fibonacci[-2]
while nextFibonacciNumber <= number:
  fibonacci.append(nextFibonacciNumber)
  nextFibonacciNumber = fibonacci[-1] + fibonacci[-2]
print fibonacci
