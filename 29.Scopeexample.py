# Global scope 
X=99

def func(Y):
  # Local scope 
  Z=X+Y
  return Z
func(1)

