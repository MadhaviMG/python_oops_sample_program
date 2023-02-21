from House.activities import Members, Parent1, Parent2, kid1, kid2

user1 = Parent1('Male', '43')
user2 = Parent2('Female', '40')
user3 = kid1('Female', '12')
user4 = kid2('Male', '8')

def additional_work(member_object):
    member_object.work()
    print("can also help in house hold works")

for person in [user1, user2, user3, user4]:
    person.work()

user1.common_activities()
additional_work(user3)
user3.work()

