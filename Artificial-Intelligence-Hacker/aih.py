# Python 3.5.2 or 3.5.3 or 3.6.1 is required!
import sys
import tensorflow as tsfl

# Program Banner
print('Artificial Intelligence Hacker Nu')
print('Cycrada')
print('Powered by TensorFlow')

# Print Message
print('Hello, Cycrada!')
mesg = tsfl.constant('Hello, c0m3t!')
sesn = tsfl.Session()
print(sesn.run(mesg))
