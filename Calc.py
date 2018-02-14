# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
# Parse Arg String into 3 nums: whole, dividend, divider
def ParseNumbers(InStr):
    WholeNum = "0"
    if InStr[0] != '(':
        WholeNum = InStr[:InStr.find('(')]
        InStr = InStr[InStr.find('('):]
    InStr = InStr.strip('(').strip(')')
    Frac = InStr.split('/')    
    return int(WholeNum), int(Frac[0]), int(Frac[1])

# Arg1 + Arg2
def AddNums(Arg1, Arg2):
    UpNum = Arg1[1] * Arg2[2] + Arg2[1]*Arg1[2]
    LowNum = Arg1[2] * Arg2[2]
    WholeNum = Arg1[0] + Arg2[0]
    
    if UpNum > LowNum:
        WholeNum = WholeNum + UpNum//LowNum
        UpNum = UpNum % LowNum
        
    return WholeNum, UpNum, LowNum

#Arg1 - Arg2
def SubNums(Arg1, Arg2):
    UpNum = Arg1[0]*Arg1[2]* Arg2[2] + Arg1[1] * Arg2[2] - Arg2[1]*Arg1[2] - Arg2[0]*Arg2[2]*Arg1[2]
    LowNum = Arg1[2] * Arg2[2]
    WholeNum = 0
    
    if UpNum > LowNum:
        WholeNum = WholeNum + UpNum//LowNum
        UpNum = UpNum % LowNum
        
    return WholeNum, UpNum, LowNum

#Arg1 * Arg2
def MulNums(Arg1, Arg2):
    UpNum = (Arg1[0]*Arg1[2] + Arg1[1]) * (Arg2[1] + Arg2[0]*Arg2[2])
    LowNum = Arg1[2] * Arg2[2]
    WholeNum = 0
    
    if UpNum > LowNum:
        WholeNum = WholeNum + UpNum//LowNum
        UpNum = UpNum % LowNum
        
    return WholeNum, UpNum, LowNum

#Arg1 / Arg2
def DivNums(Arg1, Arg2):
    UpNum = (Arg1[0]*Arg1[2] + Arg1[1]) * Arg2[2]    
    LowNum = Arg1[2] * (Arg2[1] + Arg2[0]*Arg2[2])
    WholeNum = 0
    
    if UpNum > LowNum:
        WholeNum = WholeNum + UpNum//LowNum
        UpNum = UpNum % LowNum
        
    return WholeNum, UpNum, LowNum

#InputStr = input()
InputStr = "1(1/2) % (3/4)" 	# test input string

Args = ["",""]    

# Split string into 2 Args
if InputStr.find('+') >= 0:
    Args = InputStr.split('+')
else:
   if InputStr.find('-') >= 0:
       Args = InputStr.split('-')
   else:
       if InputStr.find('*') >= 0:
           Args = InputStr.split('*')
       else:           
           Args = InputStr.split('%')

# Remove spaces
Arg1 = Args[0].strip()
Arg2 = Args[1].strip()

# Split 2 Args into 6 numbers
Arg1 = ParseNumbers(Arg1)
Arg2 = ParseNumbers(Arg2)

Result = [0,0,0]

# Calculate result
if InputStr.find('+') >= 0:
    Result = AddNums(Arg1, Arg2)
else:
   if InputStr.find('-') >= 0:
      Result = SubNums(Arg1, Arg2)
   else:
      if InputStr.find('*') >= 0:
          Result = MulNums(Arg1, Arg2)
      else:          
          Result = DivNums(Arg1, Arg2)

# Print result
if Result[0] != 0:
    print(str(Result[0]) + "(" + str(Result[1]) + "/" + str(Result[2]) + ")")
else:
    print("(" + str(Result[1]) + "/" + str(Result[2]) + ")")

