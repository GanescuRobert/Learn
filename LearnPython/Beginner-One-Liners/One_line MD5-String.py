# Natural
text = 'hello world'

import hashlib

m = hashlib.md5()
m.update(text.encode('utf-8'))
print(m.hexdigest())

# One_Liner 1
import hashlib;text = 'hello world'; m = hashlib.md5();m.update(text.encode('utf-8'));print(m.hexdigest())

# One_Liner 2
import hashlib; m = hashlib.md5('hello world'.encode('utf-8'));print(m.hexdigest())

# One_Liner 3
import hashlib as h; print(h.md5('hello world'.encode('utf-8')).hexdigest())

# One_Liner 4
import hashlib as h; print(h.md5(b'hello world').hexdigest())
