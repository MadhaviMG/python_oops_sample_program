class Members:
    def __init__(self, gender, age):
        self.member_gender = gender
        self.member_age = age

    def common_activities(self):
        print("This person daily does common activities along with specific works")

    def work(self):
        print("Everyone does their specific work and common work")

class Parent1(Members):
    def work(self):
        print("Parent1 does mainly office work, dropping and picking up kids")
        
class Parent2(Members):
    def work(self):
        print("Parent2 mainly does all household activities, food preparation and teaching kids")

class kid1(Members):
    def work(self):
        print("kid1 goes to school and studies after coming home")

class kid2(Members):
    def work(self):
        print("kid2 goes to school and does studies and play after coming back")

