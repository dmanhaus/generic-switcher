from ..switcher import SwitcherBaseClass

import sys
import inspect
import pkgutil
from pathlib import Path
from importlib import import_module

for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
    imported_module = import_module('.' + name, package='switcher.switches')

    class_name = list(filter(lambda x: x != 'SwitcherBaseClass' and not x.startswith('__'),
                             dir(imported_module)))

    switch_class = getattr(imported_module, class_name[0])

    if issubclass(switch_class, SwitcherBaseClass):
        setattr(sys.modules[__name__], name, switch_class)