print('안전한 나눗셈 계산기')

while True:
    try:
        # 정상 로직
        num_str = input('숫자를 입력하세요 (종료 q)')
        if num_str == 'q':
            break
        num = int(num_str)
        result = 10/ num
        print(f'계산 결과: {result}')
    except ValueError:
        # 숫자가 아닐 때 실행
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
    except ZeroDivisionError:
        # 0으로 나눌 때 실행
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        # 그 외 모든 오류
        print(e)

    finally:
        # 항상 실행
        print("계산 시도 완료")