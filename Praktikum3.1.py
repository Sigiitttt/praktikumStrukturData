def stack():
  return []
def push(s,data):
  s.append(data)
def pop(s):
  h = s.pop()
  return h
def isEmpty(s):
  return s == []
def size(s):
  return len(s)
def peek(s):
  return s[-1]

def dec2bin(num):
  biner = ""  
  proc = ""  
  count = 1  
  st = stack() 
  while num != 0:
    push(st,num%2) 
    proc += f"{count}. Push stack with {num&2} --> {st}\n" 
    num //= 2 
    count += 1
  while not isEmpty(st):  
    biner += str(pop(st)) 
    proc += f"{count}. Pop stack --> {st}\n" 
    count += 1  
  return biner,proc

num = 20  # angka uji
binary,proc = dec2bin(num)  
print(proc)
print(f"Biner {num} = {binary}")