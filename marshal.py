# Cryptography with Python created by Ismail ahmed
# linkedin.com/in/engismail2020/


import marshal

Ismail = """import os 

print(' Your Bank Account Number Is : 13549 ')"""

Ismail = compile(Ismail, "<Ismail>", "exec")

data = marshal.dumps(Ismail)

print("-"*150)
print(repr(data))
print("-"*150)

exec(marshal.loads(data))
