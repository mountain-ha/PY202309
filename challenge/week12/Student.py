class Student():
    def __init__(self, name, korean, math, eng): #생성자
        self.name = name
        self.korean = korean
        self.math = math
        self.eng = eng

    def  get_average(self): #성적 평균을 구하는 함수
        return (self.korean+self.math+self.eng)/3