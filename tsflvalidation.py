# Python 3.5.2 or 3.5.3 or 3.6.1 is required!
import tensorflow as tsfl
mesg = tsfl.constant('Hello, TensorFlow!')
print(mesg)
sesn = tsfl.Session()
print(sesn)
print(sesn.run(mesg))
