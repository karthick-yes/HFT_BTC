def Quantum(size, target): 
    bookmark = size * 2/5 
    if bookmark == target: 
          return True 
    if bookmark < target:
         return Quantum(size - bookmark, target - bookmark)
    if bookmark > target: 
          return Quantum(bookmark, target) 
    return False
Quantum(167,36)
