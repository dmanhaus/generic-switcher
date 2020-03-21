from abc import ABCMeta, abstractmethod

class SwitcherBaseClass(metaclass=ABCMeta):
  def __init__(self, name=None):
    if name:
      self.name = name

  @abstractmethod
  def base_switch(self, argument):
    # Get the method from 'self'. Default to a lambda

    method = getattr(self, argument, lambda: "Invalid request")

    # Call the method as we return it

    return method()