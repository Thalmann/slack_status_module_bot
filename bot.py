from modules.module import Module
from active_modules import *


modules = [module() for module in Module.__subclasses__()]
try:
    while True:
        for module in modules:
            if module.should_run():
                module.run()
except Exception as error:
    print('Failed due to: ', error)
