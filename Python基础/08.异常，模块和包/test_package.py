"""
import 和 from 语句中
.是用来区分层级的
"""

# import my_package.model1
# import my_package.model2
#
# # compute/time.py show/time.py
# # import compute.time
# # import show.time
# my_package.model1.say_hello()
# my_package.model2.say_hello()
#
# from my_package import model1
# model1.say_hello()
#
# from my_package.model1 import say_hello
# say_hello()

from my_package import *
model1.say_hello()
 