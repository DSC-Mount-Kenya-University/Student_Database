from Database import StatsStudents,Student,ExamStats,Exams,InnitializeStudents,InnitializeExams
from tools import Lists,Files,randomise,Strings


class Scalar:
    def get_best_perfomance(student_object):
        self_exams = StatsStudents.get_stats(student_object)
        print(self_exams)
        exam_list = self_exams.get('exam_list')
        score_list = self_exams['scores']
        score_list1 = []
        for item in score_list:
            score_list1.append(int(item))
        maximum = max(score_list1)
        index_of_max = score_list1.index(maximum)
        max_dic ={"exam":exam_list[index_of_max],"score":maximum}
        print("You did well on the", max_dic['exam'],"exam", "You maxed out in all your exams with", max_dic['score'])
        return max_dic

    def get_worst_perfomance(student_object):
        self_exams = StatsStudents.get_stats(student_object)
        exam_list = self_exams['exam_list']
        score_list = self_exams['scores']
        score_list1 = []
        for item in score_list:
            score_list1.append(int(item))
        minimum = min(score_list1)
        index_of_min = score_list1.index(minimum)
        min_dic = {"exam": exam_list[index_of_min], "score": minimum}
        print("Suggested Improve on",min_dic['exam'],"You had the lowest score :",min_dic['score'])
        return min_dic
    def get_best_student():
        pass
    def get_worst_student():
        pass
    def get_average_perfomance(student_object):
        pass

class Innitialize(ExamStats, StatsStudents):
    def system():
        pass
    pass