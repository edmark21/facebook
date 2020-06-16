import os,sys

u = raw_input("username: ")
fn = raw_input("first name: ")
ln = raw_input("last name: ")
bm = raw_input("birth month: ")
bd = raw_input("birth date: ")
by = raw_input("birth year: ")
pn = raw_input("Phone #: ")
a = raw_input("age: ")
c = raw_input("custom fav: ")
n = raw_input("nickname: ")
stdoutOrigin=sys.stdout
sys.stdout = open("password.txt", "w")
print(fn + bd)
print(fn + bm + bd)
print(fn + bm + bd + by)
print(u + bm)
print(u + bm + bd)
print(ln + bd)
print(ln + bm + bd)
print(ln + bm + bd + by)
print(fn + a)
print(ln + a)
print(n + bd)
print(n + bm + bd)
print(n + bm + bd + by)
print(n + a)
print(c + a)
print(c + bd)
print(c + bm)
print(c + bm + bd)
print(c + bm + bd + by)
sys.stdout.close()
sys.stdout=stdoutOrigin










