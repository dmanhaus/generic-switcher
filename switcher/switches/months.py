from ..switcher import SwitcherBaseClass

class Month(SwitcherBaseClass):
  def __init__(self, name=None):
    SwitcherBaseClass.__init__(self, name)

  # This function is the function that the Switcher class exposes
  def numbers_to_months(self, argument):
      return self.switch('_month_' + str(argument))

  # These functions are the underlying functions that get called based on the argument passed in the first function
  def _month_1(self):
    return "January"
  
  def _month_2(self):
    return "February"

  def _month_3(self):
    return "March"

  def _month_4(self):
    return "April"

  def _month_5(self):
    return "May"

  def _month_6(self):
    return "June"

  def _month_7(self):
    return "July"

  def _month_8(self):
    return "August"

  def _month_9(self):
    return "September"

  def _month_10(self):
    return "October"

  def _month_11(self):
    return "November"

  def _month_12(self):
    return "December"