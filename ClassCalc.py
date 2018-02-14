# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
class CFrac:
    WholePart = 0
    UpNum = 0
    LowNum = 0
    __InputStr = ""
    __Frac = [0,0,0]
    
    def __init__(self, p_InputStr):
        self.__InputStr = p_InputStr
        self.__ParseNumbers()
        
    def __ParseNumbers(self):
        StrWholePart = "0"
        if self.__InputStr[0] != '(':
            StrWholePart = self.__InputStr[:self.__InputStr.find('(')]
            self.__InputStr = self.__InputStr[self.__InputStr.find('('):]
        self.__InputStr = self.__InputStr.strip('(').strip(')')
        __Frac = self.__InputStr.split('/')  
        
        self.WholePart = int(StrWholePart)
        self.UpNum = int(__Frac[0])
        self.LowNum = int(__Frac[1])
        
    def __add__(self, Arg2):
        self.UpNum = self.UpNum * Arg2.LowNum + Arg2.UpNum*self.LowNum
        self.LowNum = self.LowNum * Arg2.LowNum
        self.WholePart = self.WholePart + Arg2.WholePart
        
        if self.UpNum > self.LowNum:
            self.WholePart = self.WholePart + self.UpNum//self.LowNum
            self.UpNum = self.UpNum % self.LowNum
        return self

    def __sub__(self, Arg2):
        self.UpNum = self.WholePart*self.LowNum* Arg2.LowNum + self.UpNum * Arg2.LowNum - Arg2.UpNum*self.LowNum - Arg2.WholePart*Arg2.LowNum*self.LowNum
        self.LowNum = self.LowNum * Arg2.LowNum
        self.WholePart = 0
        
        if self.UpNum > self.LowNum:
            self.WholePart = self.WholePart + self.UpNum//self.LowNum
            self.UpNum = self.UpNum % self.LowNum   
        return self
        
    
    def __mul__(self, Arg2):
        self.UpNum = (self.WholePart*self.LowNum + self.UpNum) * (Arg2.UpNum + Arg2.WholePart*Arg2.LowNum)
        self.LowNum = self.LowNum * Arg2.LowNum
        self.WholePart = 0
        
        if self.UpNum > self.LowNum:
            self.WholePart = self.WholePart + self.UpNum//self.LowNum
            self.UpNum = self.UpNum % self.LowNum    
        return self
       
    
    def __mod__(self, Arg2):
        self.UpNum = (self.WholePart*self.LowNum + self.UpNum) * Arg2.LowNum    
        self.LowNum = self.LowNum * (Arg2.UpNum + Arg2.WholePart*Arg2.LowNum)
        self.WholePart = 0
        
        if self.UpNum > self.LowNum:
            self.WholePart = self.WholePart + self.UpNum//self.LowNum
            self.UpNum = self.UpNum % self.LowNum
        return self
    
    def print(self):
        if self.WholePart != 0:
            print(str(self.WholePart) + "(" + str(self.UpNum) + "/" + str(self.LowNum) + ")")
        else:
            print("(" + str(self.UpNum) + "/" + str(self.LowNum) + ")")   

#InputStr = input()
InputStr = "1(1/2) + (3/4)"

Args = ["",""]    


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

Arg1 = Args[0].strip()
Arg2 = Args[1].strip()

Frac1 = CFrac(Arg1)
Frac2 = CFrac(Arg2)


if InputStr.find('+') >= 0:
    Result = Frac1 + Frac2
else:
   if InputStr.find('-') >= 0:
     Result = Frac1 - Frac2
   else:
      if InputStr.find('*') >= 0:
          Result = Frac1 * Frac2
      else:          
          Result = Frac1 % Frac2

Result.print()

