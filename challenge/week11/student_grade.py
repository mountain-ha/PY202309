    
class Student():
    def __init__(self, name, korean, math, eng): #생성자
        self.name = name
        self.korean = korean
        self.math = math
        self.eng = eng

    def  get_average(self): #성적 평균을 구하는 함수
        return (self.korean+self.math+self.eng)/3
    
def load_data(file_name): #파일 열기
    fp = open(file_name, "r", encoding="utf8")
    lines = fp.readlines()
    fp.close()

    student_list = []
    for line in lines[1:]:
        tokens = line.replace("\n", "").split(",")
        student1 = Student(tokens[0], float(tokens[1]), float(tokens[2]), float(tokens[3])) #객체 만들기
        student_list.append(student1) #만든 객체를 리스트에 저장

    return student_list


# TODO 2: 각 학생별 평균 점수 계산
# getAverage()를 사용하여 평균 계산
student_list = load_data("student.csv") #위의 함수 작동
for student_ins in student_list:
    print(f"{student_ins.name}의 평균점수 {student_ins.get_average()}") #평균점수 출력


