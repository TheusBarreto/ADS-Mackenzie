import math 
EP = float (input(''))
CV = float (input(''))
EPC = EP/CV
EPV = math.ceil(EPC) 
CVP = EPC+EPC*0.23
PVC = math.ceil (CVP) 
print(CVP)
print(EPV)