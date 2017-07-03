"""
ENCODING SCHEME: LIST ON SEPARATE LINES IN THIS FORMAT
list of states separated by , and cannot use , in names
start state
accept state
reject state
now list all possible transition funtions in this form separated by ,
state, what you read,what you write, Direction, state you go to"""

"- represents the blank space"
#this example tm checks for pallindromes
tmqs1 = """q0,qaccept,qr,qendr,qreject,ql,qr2,qend2
q0
qaccept
qreject
q0,a,-,R,qr
q0,-,-,R,qaccept
q0,b,-,R,qr2
qr,a,a,R,qr
qr,b,b,R,qr
qr,-,-,L,qendr
qendr,b,-,R,qreject
qendr,a,-,L,ql
ql,a,a,L,ql
ql,b,b,L,ql
ql,-,-,R,q0
qr2,a,a,R,qr2
qr2,b,b,R,qr2
qr2,-,-,L,qend2
qend2,a,-,R,qreject
qend2,b,-,L,ql
qendr,-,-,R,qreject
qend2,-,-,R,qreject"""

def TMI(tm ,string1):
  lines = tm.splitlines()
  states = lines[0].split(",")
  #print(states)
  start = lines[1]
  accept = lines[2]
  reject = lines[3]
  functions =[]
  #print(start,accept,reject)
  for i in range(4,len(lines)):
    functions.append(lines[i].split(","))

  #print(functions)
  tape = list(string1)
  currentState = start
  #print(tape)
  pos = 0
  if(tape==[]):
    tape=['-']
  while(currentState != accept and currentState != reject):
    for func in functions :
      if(func[0] == currentState and func[1] == tape[pos]):
        #print(func)
        tape[pos] = func[2]
        currentState = func[4]
        if(func[3]=="L" and pos>0):
          pos = pos - 1

        elif (func[3] =="R"):
          if(pos<len(tape)-1):
            pos = pos +1
          else:
            pos = pos + 1
            tape.append("-")
        else:
          break
        #print(tape)
        break

  if (currentState == accept):
    return True
  else:
    return False

def test():
  assert(False == TMI(tmqs1,"abbbaabba"))
  assert(False == TMI(tmqs1,"abbbaaaaaaabba"))
  assert(False == TMI(tmqs1,"ab"))
  assert(True == TMI(tmqs1,"abbabbbbbbbbabba"))
  assert(False == TMI(tmqs1,"abbbaabbab"))
  assert(True == TMI(tmqs1,""))
  assert(False == TMI(tmqs1,"abbbabbba"))
  assert(False == TMI(tmqs1,"a"))
  assert(False == TMI(tmqs1,"ababbbaba"))
  assert(True == TMI(tmqs1,"abba"))
  print("tests passed!")
