from university import *

class Data:
    ROOMS = [["R1",20], ["R2",35], ["R3",30], ["R4",15], ["R5",55], ["R6",20], ["R7",15], ["R8",10], ["R9",35]]
    MEETING_TIMES = [["08:40 - 10:15"],
                     ["10:35 - 12:10"],
                     ["12:20 - 13:55"],
                     ["14:05 - 15:40"]]
    INSTRUCTORS = [["Flitwick"],
                   ["Sinistra"],
                   ["Lupin"],
                   ["Sprout"],
                   ["Binns"],
                   ["Snape"],
                   ["McGonagall"],
                   ["Vector"]]

    def __init__(self):
        self._rooms = []
        self._meetingTimes = []
        self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Audience(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(LessonTime(self.MEETING_TIMES[i][0]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Teacher(self.INSTRUCTORS[i][0]))

        subject1 = Subject("Astronomy",[self._instructors[0], self._instructors[1]], 40)
        subject2 = Subject("Charms", [self._instructors[0], self._instructors[2]], 20)
        subject3 = Subject("Defense Against the Dark Arts", [self._instructors[7], self._instructors[1]], 30)
        subject4 = Subject("Herbology", [self._instructors[2], self._instructors[3]], 55)
        subject5 = Subject("History of Magic", [self._instructors[3]], 22)
        subject6 = Subject("Potions", [self._instructors[0], self._instructors[2]], 30)
        subject7 = Subject("Transfiguration", [self._instructors[1], self._instructors[3]], 35)
        subject8 = Subject("Arithmancy", [self._instructors[6], self._instructors[5]], 40)
        subject9 = Subject("Divination", [self._instructors[4], self._instructors[7]], 20)
        self._subjects = [subject1, subject2, subject3, subject4, subject5, subject6, subject7]

        spec1 = Speciality("MI", [subject1, subject3, subject9])
        spec2 = Speciality("TTP", [subject2, subject4, subject5])
        spec3 = Speciality("TK", [subject6, subject7, subject8])
        self._specs = [spec1, spec2, spec3]

        self._numberOfClasses = 0
        for i in range(0, len(self._specs)):
            self._numberOfClasses += len(self._specs[i]._subjects)