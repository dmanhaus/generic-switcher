from importlib import import_module

from .switcher import SwitcherBaseClass

def switch(switch_name, *args, **kwargs):
  try:
    if '.' in switch_name:
      module_name, class_name = switch_name.rsplit('.', 1)
    else:
      module_name = switch_name
      class_name = switch_name.capitalize()

    switch_module = import_module('.' + module_name, package='switcher')

    switch_class = getattr(switch_module, class_name)

    instance = switch_class(*args, **kwargs)

  except (AttributeError, AssertionError, ModuleNotFoundError):
    raise ImportError('{} is not part of the switcher collection'.format(switch_name))
  else:
    if not issubclass(switch_class, SwitcherBaseClass):
      raise ImportError('There is no {}'.format(switch_class))

  return instance