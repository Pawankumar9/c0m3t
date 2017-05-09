# Python 3.5.2 is required!
import sys
import tensorflow as tsfl

# Program Banner
print('Artificial Intelligence Hacker')
print('Powered by TensorFlow')

# Print Message
mesg = tsfl.constant('Hello, Artificial Intelligence Hacker!')
sesn = tsfl.Session()
print(sesn.run(mesg))
