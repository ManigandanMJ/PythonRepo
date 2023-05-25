import logging
logging.basicConfig(filename = "c:\\logs\\marks_percent_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

num = int(input("Enter number students : "))
log.info("Received number of students to added")
stu_marks = {}
# Getting number of students list with marks in dictionary
for i in range(num):
    log.info("Entered loops to get the student details")
    #spliting the marks in *marks and calculating sum
    stu_name, *marks = input().split()
    marks_list = list(map(float, marks))
    marks_len = len(marks_list)
    stu_marks[stu_name] = marks_list
    log.info("Students data received")
# Receiving student name to find the average
stu_input = input("Enter student name : ")
if stu_input in stu_marks.keys():
    #Defining function for getting percentage value
    def average_marks():
        log.info("Average of marks is calculated")
        total = sum(stu_marks[stu_input])
        percent = total / marks_len
        print(stu_input, "%.2f" % percent)
        return stu_input, "%.2f" % percent
    log.info("Percentage value is returned")
else:
    log.warning("Entered wrong student name")
    print("Input name is not on data received")

