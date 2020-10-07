def solution(record):

    for i in record:
        answer = []

        #입장
        if record[i][0:5] == "Enter":
            print(record[i].rfind(' '))
            a = record[record[i].rfind(' ')+1 : ]

            answer.insert(0, a + "님이 들어왔습니다.")
        
        #퇴장
        elif record[i][0:5] == "Leave":
            print(record[i].rfind(' '))
            a = record[record[i].rfind(' ')+1 : ]

            answer.insert(0, a + "님이 나갔습니다.")