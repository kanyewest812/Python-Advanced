class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        return f"My name is {self._name}. I'm {self._age}."


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def info(self):
        return f"I'm {self._name}. My major is {self.major}."


p = Person("Amina", 21)
s = Student("Liza", 18, "Cybersecurity")

print(p.info())
print(s.info())
