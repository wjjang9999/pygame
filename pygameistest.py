class God():
    def __init__(self,name,age,country,height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f"저는 {self.name} 이고, 나이는 {self.age} 세이고, 국적은 {self.country} 이고, 몸무게는 {self.height} 입니다.")


a = God('정윤성','14','한국','38kg')
b = God('장우진','13','한국','32kg')
c = God('지명원','14','한국','37.9kg')
d = God('전상진','13','한국','28kg')
e = God('김정은','39','조선민주주의인민공화국','666kg')

a.introduce()
b.introduce()
c.introduce()
d.introduce()
e.introduce()