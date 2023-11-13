    
class  Student():
    [name, korean, math, english] = [" ", 0, 0, 0]
    def  get_average(self,name):
        get_sum = self.korean + self. math + self.english
        average = get_sum / len(self,scores)
        return average

fp = open("student.csv", "r", encoding="utf8")
lines = fp.readlines()
fp.close()

# TODO 1: 학생 정보를 딕셔너리에 저장
students = {}
for line in lines[1:]:
    student_data = Student()
    student_data.name
    student_data.korean
    student_data.math
    student_data.english


# TODO 2: 각 학생별 평균 점수 계산
# getAverage()를 사용하여 평균 계산
print("----학생들의 평균 점수----")
for name, scores in students.items():
    average_score = getAverage(scores)
    print(f"{name}의 평균 점수는 {average}입니다")