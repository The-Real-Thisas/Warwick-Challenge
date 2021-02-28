# API KEY: PYLY7H-VVY3HJVPQX

import pyforms
import pyforms.basewidget
import pyforms.controls
import wolframalpha
import requests


def apicall(nn):
  query = str(nn)
  app_id = "PYLY7H-VVY3HJVPQX"
  url = 'http://api.wolframalpha.com/v1/result?i=%s&appid=%s' %(query, app_id)
  req = requests.get(url)
    # Set debug flag to 1 to enable.
  debug = 1

  if debug == 1:
      print("----------------------")
      print("DEBUG INFORMATION")
      print("DEBUG (URL) : ", url)
      print("DEBUG: ", 'Requesting content')
      print("DEBUG (Status code) : ", req.status_code)
      print("----------------------")

  client = wolframalpha.Client(app_id)
  res = client.query(query)

  try:
    answer = next(res.results).text
  except:
    print("Unable to process query.")

  print("----------------------")
  print("Answer:")
  print(answer)
  print("----------------------")
  return answer


questionss = []

class Main(pyforms.basewidget.BaseWidget):
  global question
  



  def __init__(self):
    super(Main, self).__init__("Wolfram Alpha Calculator")

    self.question = pyforms.controls.ControlLabel(" ")
    self.question.value = '' #contain value for calculating purposes

    self.answer = pyforms.controls.ControlLabel("")
    self.answer.value = "" #showing purposes


    self.button1 = pyforms.controls.ControlButton("SOLVE")
    self.button1.value = self.solve
    self.button2 = pyforms.controls.ControlButton("-")
    self.button2.value = self.subtract

    self.button3 = pyforms.controls.ControlButton("+")
    self.button3.value = self.add

    self.button4 = pyforms.controls.ControlButton("x")
    self.button4.value = self.multiply

  
    self.button5 = pyforms.controls.ControlButton( "a^2")
    self.button5.value = self.power

    self.button6 = pyforms.controls.ControlButton("sin")
    self.button6.value = self.sin

    self.button7 = pyforms.controls.ControlButton("cos")
    self.button7.value = self.cos

    self.button8 = pyforms.controls.ControlButton("tan")
    self.button8.value = self.tan
    
    self.button9 = pyforms.controls.ControlButton("(")
    self.button9.value = self.openn
    
    self.button10 = pyforms.controls.ControlButton(")")
    self.button10.value = self.close

    self.button11 = pyforms.controls.ControlButton("/")
    self.button11.value = self.divide

    
    self.button12 = pyforms.controls.ControlButton("Solve Complex Equation")
    self.button12.value = self.changegui
    #self.button13 = pyforms.controls.ControlButton("Solve")

    self.button13 = pyforms.controls.ControlButton("delete")
    self.button13.value = self.delete

    self.button14 = pyforms.controls.ControlButton("C")
    self.button14.value = self.cc

    self.button21 = pyforms.controls.ControlButton("1")
    self.button21.value = self.one

    self.button22 = pyforms.controls.ControlButton("2")
    self.button22.value = self.two

    self.button23 = pyforms.controls.ControlButton("3")
    self.button23.value = self.three

    self.button24 = pyforms.controls.ControlButton("4")
    self.button24.value = self.four

    self.button25 = pyforms.controls.ControlButton("5")
    self.button25.value = self.five
    
    self.button26 = pyforms.controls.ControlButton("6")
    self.button26.value = self.six
    
    self.button27 = pyforms.controls.ControlButton("7")
    self.button27.value = self.seven

    self.button28 = pyforms.controls.ControlButton("8")
    self.button28.value = self.eight

    
    self.button29 = pyforms.controls.ControlButton("9")
    self.button29.value = self.nine

    self.button30 = pyforms.controls.ControlButton("0")
    self.button30.value = self.zero

    self.second = pyforms.controls.ControlText("If too complex, Enter a question here: ")

  
    self._formset = [
            (''),
            ('questions'),
            ('answer'),
             
            
            ('button21', 'button22','button23','button24','button25', 'button26','button27','button28','button29', 'button30'),
            ('button2', 'button3','button4','button5'),
            ('button6', 'button7','button8'),
            ('button9', 'button10', 'button11'),
            ('button13', 'button14'),
             ('second'),
            ('button12'),
            ('button1')
            
          
        ]

  def solve(self):
    self.answer.hide()
    self.answer.value = apicall(self.question.value)
    self.answer.hide()
    self.answer.show()

  def subtract(self):
    self.question.value = self.question.value + "-"
    self.answer.value = self.answer.value + " - "
    self.answer.hide()
    self.answer.show()

  def add(self):
    self.question.value = self.question.value + "+"
    self.answer.value = self.answer.value + " + "
    self.answer.hide()
    self.answer.show()

  def multiply(self):
    self.question.value = self.question.value + "*"
    self.answer.value = self.answer.value + " x "
    self.answer.hide()
    self.answer.show()

  def divide(self):
    self.question.value = self.question.value + "/"
    self.answer.value = self.answer.value + " / "
    self.answer.hide()
    self.answer.show()

  def power(self):
    self.question.value = self.question.value + "^(2)"
    self.answer.value = self.answer.value + "^2"
    self.answer.hide()
    self.answer.show()

  def sin(self):
    self.question.value = self.question.value + "sin("
    self.answer.value = self.answer.value + "sin("
    self.answer.hide()
    self.answer.show()

  def cos(self):
    self.question.value = self.question.value + "cos("
    self.answer.value = self.answer.value + "cos("
    self.answer.hide()
    self.answer.show()

  def tan(self):
    self.question.value = self.question.value + "tan("
    self.answer.value = self.answer.value + "tan("
    self.answer.hide()
    self.answer.show()

  def openn(self):
    self.question.value = self.question.value + "("
    self.answer.value = self.answer.value + "("
    self.answer.hide()
    self.answer.show()
 
  def close(self):
    self.question.value = self.question.value + ")"
    self.answer.value = self.answer.value + ")"
    self.answer.hide()
    self.answer.show()

  def delete(self):
    questionnn = self.question.value
    answerrr = self.answer.value
      
    self.answer.value = ""
    self.question.value = ''

    for index in range(len(questionnn)-1):
      self.question.value = self.question.value + questionnn[index]
        
    for index2 in range(len(answerrr) -1):
      self.answer.value = self.answer.value + answerrr[index2]
      
    #self.question.value = question1
      #return question
    self.answer.hide()
    self.answer.show()
    
    
  def changegui(self):
    self.answer.hide()
    self.answer.value = apicall(self.second.value)
    self.answer.hide()
    self.answer.show()


  def cc(self):
    self.question.value = " "
    self.answer.value = " "
    self.answer.hide()
    self.question.hide()
    self.answer.show()


  def one(self):
    self.question.value = self.question.value + "1"
    self.answer.value = self.answer.value + "1"
    self.answer.hide()
    self.answer.show()

  def two(self):
    self.question.value = self.question.value + "2"
    self.answer.value = self.answer.value + "2"
    self.answer.hide()
    self.answer.show()

  def three(self):
    self.question.value = self.question.value + "3"
    self.answer.value = self.answer.value + "3"
    self.answer.hide()
    self.answer.show()

  def four(self):
    self.question.value = self.question.value + "4"
    self.answer.value = self.answer.value + "4"
    self.answer.hide()
    self.answer.show()

  def five(self):
    self.question.value = self.question.value + "5"
    self.answer.value = self.answer.value + "5"
    self.answer.hide()
    self.answer.show()

  def six(self):
    self.question.value = self.question.value + "6"
    self.answer.value = self.answer.value + "6"
    self.answer.hide()
    self.answer.show()

  def seven(self):
    self.question.value = self.question.value + "7"
    self.answer.value = self.answer.value + "7"
    self.answer.hide()
    self.answer.show()

  def eight(self):
    self.question.value = self.question.value + "8"
    self.answer.value = self.answer.value + "8"
    self.answer.hide()
    self.answer.show()

  def nine(self):
    self.question.value = self.question.value + "9"
    self.answer.value = self.answer.value + "9"
    self.answer.hide()
    self.answer.show()

  def zero(self):
    self.question.value = self.question.value + "0"
    self.answer.value = self.answer.value + "0"
    self.answer.hide()
    self.answer.show()

pyforms.start_app(Main, geometry=(200, 100, 300, 400)) #left,top,bottom,right   

## 