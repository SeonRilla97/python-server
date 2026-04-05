'''
pip install faker
'''

from faker import Faker

fake = Faker('ko_KR')

print ('가짜 프로필 생성기')

name = fake.name()
address = fake.address()

print(name)
print(address)

for i in range(5):
    print(fake.name())