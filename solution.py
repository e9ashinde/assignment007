#Q1
def ispalindrome(x):
    if type(x) is int:
        x=str(x)
        return x==x[::-1]
    return x==x[::-1]
print(ispalindrome(2332))

#Q2
def insert_lst(lst,num,pos):
  lst.insert(num,pos)
  return lst
print(insert_lst([1,2,3,5,6,7,8],3,4))

#Q3
def two_lst(a,b):
  a.insert(3,4)
  print("Inserted the element 4 at 3rd position:",a)
  b.append(4)
  print("Adding element 4 in list:",b)
  a.extend(b)
  print("Extended the list a with b:",a)
print([11,12,2,34,4],[5,6,7,8,9])


#Q4
def count_lst(a,b):
   lst=[i for i in range(a,b)]
   d={i:lst.count(i) for i in lst if lst.count(i)<2}
   return d
print(count_lst(72,166))

#Q5
def rem_dup_lst(l):
  return list(set(l))
print(rem_dup_lst([1,2,3,4,5,2,3,4,5,6,7,8,7,9]))


#Q6
def prime_numbers(n):
  l=[1]
  for i in range(1,n+1):
    c=0
    for j in range(2,i+1):
      if i%j==0:
        c+=1
    if c==1:
      l.append(i)
  return l
print(prime_numbers(31))
print(prime_numbers(32))

#Q7
def rem_last(lst):
  return lst.pop()
print(rem_last([1,2,3,4,5,2,1,3,4]))

#Q8
def check(lst):
  return 2 in lst
print(check([1,3,4,5,6]))

#Q9
def find_max(lst):
  lst.sort()
  return lst[-1]
print(find_max([1,2,3,1,1,6,2,3]))

#Q10
from collections import Counter
def merge_dict(d1,d2):
  d1=Counter(d1)
  d2=Counter(d2)
  return dict(d1+d2)
print(merge_dict({"A":1,'B':3},{'C':4,'D':8}))

#Q11
def rem_occ(lst,n):
  if lst.count(n)>1:
    for i in range(lst.count(n)):
      lst.remove(n)
  return lst
print(rem_occ([1,2,3,4,3,3],3))

#Q12
def max_item(d):
  return max(d,key=d.get)
print(max_item({"Pencil":10,"Books":260,"Bottle":99}))

#Q13
def swap_dict(d):
  keys=d.values()
  vals=d.keys()
  return {i:j for (i,j) in zip(keys,vals)}
print(swap_dict({"A":1,"B":8,"C":4}))

#Q14
def rem_dict(d,x):
  return {i:j for (i,j) in d.items() if j!=x}
print(rem_dict({"a":1,"b":2,"c":1},1))

#Q15
def new_tup(t1,t2):
  return tuple(t1+t2)
print(new_tup((1,2,3,4,5,6),("DSA","Django","Python")))

#Q16
def avg_height(tup):
  return sum(tup)/len(tup)
print(avg_height((170,150,144,155,167)))

#Q17
def tup_numbers(tup,n):
  for i in range(len(tup)):
    if tup[i]==n:
      return i
print(tup_numbers((1,2,3,2,3,4,5,6,7,2),3))

#Q18
def capita(sentence):
  words=sentence.split()
  result=' '.join(i.capitalize() for i in words)
  return result
print(capita("This is the assignment solution"))

#Q19
def rev_order(string):
  string=string.split()
  string=string[::-1]
  return ' '.join(i for i in string)
print(rev_order('Python is a high level programming language'))

#Q20
def longest_word(string):
  string=string.split()
  return max(string,key=len)
print(longest_word('String is the collection of all characters'))
