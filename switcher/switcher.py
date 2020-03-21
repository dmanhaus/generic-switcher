from abc import ABCMeta, abstractmethod

class SwitcherBaseClass(metaclass=ABCMeta):
  def __init__(self, name=None):
    if name:
      self.name = name

  @abstractmethod
  def switch(self):
    pass
