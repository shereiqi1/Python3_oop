class InstanceCounter(object):
    count = 0
    
 def __init__(self, val):
     self.val = val
     InstanceCounter.count +=1
     
 def set_val(self, newval):
     self.val = newval
     
 def get_val(self):
     return self.val
    
 def get_count(self):
     return InstanceCounter.count
    
a = InstanceCounter(9)
b = InstanceCounter(18)
c = InstanceCounter(27)

for obj in (a, b, c):
    print ('val of obj: %s' %(obj.get_val())) # Initialized value ( 9, 18,27)
    print ('count: %s' %(obj.get_count())) # always 3
