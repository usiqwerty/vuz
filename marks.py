#!/usr/bin/env python3
marks=list()
cc=0
ss=0

print ("Marks perspective calculator by usiqwerty")
while True:
    i=int(input())
    marks.append(i)
    if i !=9:
        cc+=1
        ss+=i
    else:

        break
print ("Starting...")
was=float(ss)/float(cc)
print ("Current average:", was, " with ", cc, " marks")
def test(c, s):
    test5ing=0
    test45ing=0
    test455ing=0
    dc=c
    ds=s
    while test5ing < 4.5:
        s+=5
        c+=1
        test5ing=float(s)/float(c)
    print ("fives: ",c-dc, " times more")
    c=dc
    s=ds
    for i in range(10):
        s+=9
        c+=2
        test45ing=float(s)/float(c)
        if test45ing>=4.5:
            print ("four-fives: ", c-dc, " times more")
    if test45ing<4.5:
        print ("four-five combination is not possible")
    c=dc
    s=ds
    while test455ing < 4.5:
        s+=14
        c+=3
        test455ing=float(s)/float(c)
    print ("four-five-fives: ", c-dc, " times more")

if was<4.5:
    test(cc, ss)
else:
    print("Already five")
print("==== Emergency calculations ====")
test(cc+1, ss+2)
print ("==== Degrade calculation ====")
test4ing=float(ss)/float(cc)
s=ss
c=cc
while test4ing>=4.5:
    s+=4
    c+=1
    test4ing=float(s)/float(c)
print ("fours: ", c-cc, " times more")
s=ss
c=cc
test3ing=float(ss)/float(cc)
while test3ing>=4.5:
    s+=3
    c+=1
    test3ing=float(s)/float(c)
print ("threes: ", c-cc, " times more")
s=ss
c=cc
test2ing=float(ss)/float(cc)
while test2ing>=4.5:
    s+=2
    c+=1
    test2ing=float(s)/float(c)
print ("twos: ", c-cc, " times more")
s=ss
c=cc
for i in range(10):
        s+=9
        c+=2
        test45ing=float(s)/float(c)
        if test45ing>=4.5:
            print ("four-fives: ", c-cc, " times more")
            break
if test45ing<4.5:
    print ("four-five combination is not possible")
