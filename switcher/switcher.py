from abc import ABCMeta

class SwitcherBaseClass(metaclass=ABCMeta):
  def __init__(self, name=None):
    if name:
      self.name = name

  def switch(self, argument):
    method_name = str(argument)
    # Get the method from 'self'. Default to a lambda

    method = getattr(self, method_name, lambda: "Invalid request")

    # Call the method as we return it

    return method()
