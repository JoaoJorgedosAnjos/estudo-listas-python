t = ['a', 'b', 'c', 'd', 'e', 'f'];
print(t);
t = t[1:3];
print(t);
t.append('d');
print(t)

t1 =['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)