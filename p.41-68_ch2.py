# p.41
print(5)


# p.41
print(-10)
print(3.14)
print(1000)


# p.42
print(5 + 3)
print(2 * 8)
print(6 / 3)
print(3 * (3 + 1))


# p.43
# 1분 퀴즈
# 1. 다음 중 숫자 자료형 -10을 출력하기 위한 방법으로 알맞은 것은?
# print(-10)


# p.44
print('풍선')
print("나비")
print("abcdefg")
print("10")
print("파이썬" * 3)


# p.45
# print('작은따옴표")
# print("큰따옴표')


# p.45
# Note 문자열에서 작음따옴표와 큰따옴표의 차이는 무엇인가요?
print("I don't want to go to school") # 정상 출력
# print('I don't want to go to school') # 오류 발생


# p.45
# 2. 다음 중 문자열 자료형을 표시하는 방법으로 알맞은 것은?
print("마우스")


# p.46
print(5 > 10)
print(5 < 10)


# p.47
print(True)
print(False)


# p.47
print(not True)
print(not False)


# p.47
print(not (5 > 10))


# p.48
# 다음 중 불 자료형에 대한 설명으로 잘못된 것은?
# 4번. 불자료형 앞에 not을 붙이면 None이 된다.


# p.49
print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요.")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")
print("연탄이는 수컷인가요?")
print("네.")


# p.50, p.52, p.53, p.54
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"
is_male = True

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요.")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")

print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "예요")
# print(name + "는 " + age + "살이고, " + hobby + "을 아주 좋아해요")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요")


# p.54
name = "해피"
animal = "고양이"
age = 4
hobby = "낮잠"

print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "예요")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요")


# p.55
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print(name, "는", age, "살이고,", hobby, "을 아주 좋아해요")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요")


# p.56
# print(int("3") + "입니다.")


# p.56
print(int(3.5))


# p.56
# print(int("삼"))


# p.57
print(float("3.5"))
print(float(3))


# p.57
# print(float("오"))


# p.57
print(str(3) + "입니다.")
print(str(3.5) + "입니다.")


# p.58
# Note type()
print(type(3)) # 정수(int)
print(type("3")) # 문자열(str)
print(type(3.5)) # 실수(float)
print(type(str(3))) # 정수(int)를 문자열(str)로 형변환


# p.59
del name # 전에 name에 변수를 정의했던 게 남아있어서 원하는 결과가 나오지 않았다.
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
name = "연탄이"
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")


# p.59
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요")
hobby = "수영"
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요")


# p.60
# 1분 퀴즈
# 4. 다음 중 변수에 대한 설명으로 잘못된 것은?
# 3번. 변수의 값은 한번 정의하면 바꿀 수 없다.


# p.62
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

# print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요")
hobby = "수영"
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요")


# p.62
name = "연탄이" # 이름
animal = "개" # 종류
age = 4
hobby = "산책" # 취미


"""
# print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요") # 종류, 이름
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요") # 나이, 취미
"""


# p.63
# 6. 다음 코드의 실행결과로 올바른 것은?
print("파이썬은")
# print("처음에는")
print("쉬워요")

# 3번.
# 답: 파이썬은
#     쉬워요


# p.64
# 실습문제: 역 이름 출력하기

station = "사당"
# station = "신도림"
# station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")


# p.67
# 셀프체크
# 문제: 변수를 사용해 택배의 배송 상태를 안내하는 프로그램을 작성하세요.
# 조건: ~

status = "상품 준비"
# status = "배송 중"
# status = "배송 완료"

print("주문 상태 : " + status)