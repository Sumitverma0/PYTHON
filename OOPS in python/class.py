class Emoployee:
    company ='hp'
    def get_salary(self):
        print(self)
        return 34000

e=Emoployee()
print(e.get_salary())

e2=Emoployee()
print(e2.get_salary())
print(e)