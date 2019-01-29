from modules.module import Module


modules = Module.__subclasses__()
try:
    while True:
        for module in modules:
            if module.should_run():
                module.run()
except Exception as error:
    print('Failed due to: ', error)
