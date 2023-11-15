    
class  Student(): #학생 이름과 성적 클래스 생성
    name = ""
    korean = 0
    math = 0
    eng = 0
    def  get_average(self): #성적 평균을 구하는 함수
        return (self.korean+self.math+self.eng)/3
    
def load_data(file_name):
    fp = open(file_name, "r", encoding="utf8")
    lines = fp.readlines()

    student_list = []
    for line in lines[1:]:
        tokens = line.replace("\n","").split(",")
        std_ins = Student()
        std_ins.name = tokens[0]
        std_ins.korean = float(tokens[1])
        std_ins.math = float(tokens[2])
        std_ins.eng = float(tokens[3])
        student_list.append(std_ins)
    return student_list


# TODO 2: 각 학생별 평균 점수 계산
# getAverage()를 사용하여 평균 계산
student_list = load_data("student.csv")
for student_ins in student_list:
    print(f"{student_ins.name}의 평균점수 {student_ins.get_average()}")


