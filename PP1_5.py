'''
    Practice Questions: Typecasting
    Author: Johnny Zhao
    Date Created: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''

def q1():
  numq1 = input("Input an integer: ") #asking the user to input an integer
  numq1 = int(numq1) #turning their answers into a integer datatype
  print(numq1 + 3) #outputting the result plus three


def q2():
  numq2 = input("Input a number: ") #asking the user to input a number
  numq2 = numq2 + "4" #adding "4" to the end of their answer
  numq2 = float(numq2) #turning their answer into a float datatype
  print(numq2 + 2) #outputting their result plus two

def q3():
  numq3 = input("Input a radius: ") #asking the user to input a radius
  numq3 = float(numq3) #turning their answer into a float datatype 
  print(numq3 * numq3 * 3.14) #using the formula to calculate area of circle then outputting the area

def q4():
  numq4 = input("Input a number: ") #asking the user to input a number
  numq4 = float(numq4) #turning their answer into a float
  numq4 = numq4 * 12 #mutiplying their answer by 12
  numq4 = int(numq4) #turning their answer into a integer datatype
  print(numq4)

def q5():
  numq5 = input("Input an integer: ")
  numq5 = int(numq5)
  print(f"Your number + 5 is {numq5 + 5}")


#Comment this code out when running tests
#Do not comment this out when running your program normally

#q1()
#q2()
#q3()
#q4()
#q5()
