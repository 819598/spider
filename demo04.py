# import re
# a = "700.80元"
# print(a)
# b = re.match('([0-9]*\.[0-9]*)',a)
# print(b.group())

import time

start = time.time()
for i in range(10000):
    print(i)
end = time.time()
spend = end - start
print(spend)