animals = ['cat','dog','monkey']
for animal in  animals:
	print(animal)
for idx, animal in enumerate(animals):
	print('#%d: %s' % (idx+1,animal))

d={'cat': 'cute', 'dog': 'furry'}
print(d['cat'])
print('cat' in d)
d['fish']='wet'
print(d['fish'])
print(d.get('monkey', 'N/A'))
print(d.get('fish','N/A'))
del d['fish']
print(d.get('fish','N/A'))

d={'person':2, 'cat':4,'spider':8}
for animal in d:
        legs=d[animal]
        print('A %s has %d legs' % (animal, legs))
for animal, legs in d.items():
        print('A %s has %d legs' % (animal, legs))

for i in range(10) :
        print(i)
for i in range(3,10) :
        print(i)
for i in range(0, 10, 2) :
        print(i)

i=0
while i <10 :
        i+=1
        print(i)

def sign(x):
        if x>0:
                return 'positive'
        elif x<0 :
                return 'negative'
        else :
                return 'zero'

for x in [-1,0,1] :
        print(sign(x))

class Student(object):
        def __init__(self, name) :
                self.name = name
        def set_age(self, age) :
                self.age = age
        def set_major(self, major) :
                self.major = major

anna = Student('anna')
anna.set_age(21)
anna.set_major('physics')

class MasterStudent(Student):
        def set_lab(self, lab):
                sefl.lab=lab
