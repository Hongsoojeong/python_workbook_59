#연습 59번
number_count=0
upper_count=0
plate=input("번호판을 입력해주세요: ")
upper=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number=["0","1","2","3","4","5","6","7","8","9"]
for i in plate:
    if i in upper:
        upper_count+=1
    elif i in number:
        number_count+=1


if upper_count==3 and number_count==3:
    print("이전 스타일의 번호판입니다.")
elif upper_count==3 and number_count==4:
    print("최근 스타일의 번호판입니다.")
else:
    print("잘못된 형태의 번호판입니다.")