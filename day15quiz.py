#      Quize
"""" Create a python program capable of greeting you with Good 
 Morning, Good Afternoon and Good Evening. Your program 
 should use time module to get the current hour. Here is a 
sample program and documentation link for you:  """
import time 
a=time.strftime("%H")
print(a)
# 

import time
houre=int(time.strftime("%H"))

if (houre >=5 and houre <20):
     print("Good Moring Sir")
elif(houre >=12 and houre<20):
     print("Good Afternoon Sir")
elif(houre>=17 and houre<17):
     print("Good Eveing Sir")
else:
     print("Good Night Sir")