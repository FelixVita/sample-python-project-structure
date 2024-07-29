"""
This is the main runner script.
It provides specific functionality to a larger library you are packaging.
This file is sometimes alternatively named as `main.py`.
"""

from packagename.internal_module_a.a import add, sub

print(add(10, 20))  # 30
print(sub(20, 10))  # 10
