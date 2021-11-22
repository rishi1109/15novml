#Question2
print(5**9)
print(3**2)
print(7//3)
print(7/3)
print(6==6)
a=20
a+=30
a%=3
print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3) and (7>4) or (18==3)) and (9>3))
print(True is False)
print('False' in 'False')
print(((True==False) or (False>True)) and (False<=True))
#Question3
s1="Nice to have it"
s2=" here"
print(s1+s2)
#Question4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])
#Question6
numbers=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
for x in numbers:
    if x==237:
        print(x)
        break;
    elif x%2==0:
        print(x)

#Question7
color_list_1= set(["White","Black","Red"])
color_list_2= set(["Red","Green"])
print(set(color_list_1 - color_list_2))
#Question11
print("Enter a string:")
s=input().split(,)
print(s)
s.sort()
print(s)

#Question12
d={'Student':['Rahul','Kishore','Vidhya','Rakhi'], 'Marks':[57,87,67,79]}
d1=d['Marks']
large=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==large):
        j=1
d2=d['Student']
print(d2[j])


#Question13
s=input("Enter a string:")
l=0
d=0
for i in s:
    if i.isalpha():
        l=l+1
    elif c.isalpha():
        d=d+1
    else:
        pass
print("Letters", l)
print("Digits", d)

#Question5
a.insert(0,s1)
a.insert(7,s2)
print(a)




        
