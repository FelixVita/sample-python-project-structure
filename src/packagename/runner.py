"""
This is the main runner script.
It provides specific functionality to a larger library you are packaging.
This file is sometimes alternatively named as `main.py`.

Also note that this features a slight improvement upon the traditional `if __name__ == '__main__'` entrypoint,
inspired by Jean-Paul Calderone's blogpost on https://as.ynchrono.us/how-to-define-a-main-entry-point-into-a-python-program.html
"""

if __name__ == '__main__':
    import packagename.runner
    raise SystemExit(packagename.runner.main())

from packagename.submodule_a.a import add, sub

def defineSomeFunctions():
    pass

class Whatever:
    pass

def main():
    print(add(10, 20))  # 30
    print(sub(20, 10))  # 10
