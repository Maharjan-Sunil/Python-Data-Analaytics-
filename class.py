# # class Logic:
# #     def sum(self,n):
# #         sumOfNumber = n + n
# #         if sumOfNumber % 2  == 0 :
# #             print("congratulation")
# #         elif int(sumOfNumber) > 10
# #             print("sorry invalid number")
# #         else:
# #             print(sumOfNumber)

# # obj = Logic()
# # print(obj.sum(3))

# # # def printNumber(number):
# # # 	x=1;
# # # 	while x != number :
# # # 		print (x);
# # # 		x = x+1;

# # # printNumber(11); 

# # # def displayCrushName(names):
# # # 	newName= names.split(',');
# # # 	crusher = [crush[::-1] for crush in newName]
# # # 	oldCrusher = ' '.join(crusher);
# # # 	print ("These are old & I'm trying to create some new one : " + oldCrusher);

# # # names = 'atibaK, ujnA, ayhskidaS';

# # # displayCrushName(names);

# # # sportsPerson = ['Ronaldo', 'Messi', 'Coutino']
# # # ballondronWinner = sportsPerson.pop(2)
# # # print (ballondronWinner)

# # # class MyClass:
# # #   def printName(self,name):
# # #   	print("My name is "+ str(name))

# # # p1 = MyClass()
# # # p1.printName("Manish")


# for x in range(1,10):
#     print(x)


class Rational():
    def __init__(self,numerator,denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def __repr__(self):
        return (f'herer data is {self.numerator}/{self.denumerator}')

    def _return_max_common_divisor(self):
        smaller_value = min(self.numerator, self.denumerator)
        smaller_value_divisor = { i for i in range(1,smaller_value + 1 ) if smaller_value % 2 == 0 }
        max_value = max(self.numerator,self.denumerator)
        common_divisor = {i for i in smaller_value_divisor if max_value % i == 0}
        return max(common_divisor)
    
    def return_fraction_number(self):
        gcd = self._return_max_common_divisor()
        self.numerator = self.numerator / gcd
        self.denumerator = self.denumerator /gcd
        return self

fraction  = Rational(32,16)
print(fraction.return_fraction_number())