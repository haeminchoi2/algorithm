# 1. 두 정수 사이의 합 ([https://school.programmers.co.kr/learn/courses/30/lessons/12912)](https://school.programmers.co.kr/learn/courses/30/lessons/12912)

  - a, b 대소관계를 생각할 것.
  - done

# 2. 문자열을 정수로 바꾸기([https://school.programmers.co.kr/learn/courses/30/lessons/12925](https://school.programmers.co.kr/learn/courses/30/lessons/12925))

  - 단순하게 `int()`함수 사용하면 될 것 같아서, 시도 후 정답처리
  - done

# 3. 정수 내림차순으로 배치하기([https://school.programmers.co.kr/learn/courses/30/lessons/12933](https://school.programmers.co.kr/learn/courses/30/lessons/12933))

  1) 정수 n을 문자열로 변환
  2) 변환된 문자열 리스트로 쪼개고
  3) 반환된 리스트를 역순으로 정렬
  4) 다시 하나의 문자열로 변환
  - `sort()`, `sorted()` 메서드 및 내장함수 사용
  - done

# 4. 나머지가 1이 되는 수 찾기 - 월간 코드 챌린지 시즌3([https://school.programmers.co.kr/learn/courses/30/lessons/87389](https://school.programmers.co.kr/learn/courses/30/lessons/87389))

  1) 반복문 중에 처음으로 나머지가 1이 되는 x를 return
  - done

# 5. 음양 더하기 - 월간 코드 챌린지 시즌2([https://school.programmers.co.kr/learn/courses/30/lessons/76501](https://school.programmers.co.kr/learn/courses/30/lessons/76501))

  - `enumerate()`를 통해 absolutes와 signs의 길이가 같다는 것을 이용
  - done

# 6. 예산 - Summer/Winter Coding(~2018)([https://school.programmers.co.kr/learn/courses/30/lessons/12982](https://school.programmers.co.kr/learn/courses/30/lessons/12982))

  - 오름차순으로 정렬후 반복문돌면서 예산에서 빼줌
  - done

# 7. K번째수 - 정렬([https://school.programmers.co.kr/learn/courses/30/lessons/42748](https://school.programmers.co.kr/learn/courses/30/lessons/42748))

  - 문제 설명대로 진행...
  - done

# 8.  같은 숫자는 싫어 - 스택/큐([https://school.programmers.co.kr/learn/courses/30/lessons/12906](https://school.programmers.co.kr/learn/courses/30/lessons/12906))

  1) 정답이 될 초기 리스트에 arr 0번째 요소를 넣어줌
  2) arr 1번 인덱스부터 반복문 돌면서, 정답이 될 리스트 마지막과 일치하지 않을 때만 `.append()` 사용
  - done

# 9.  실패율 - 2019 KAKAO BLIND RECRUITMENT([https://school.programmers.co.kr/learn/courses/30/lessons/42889](https://school.programmers.co.kr/learn/courses/30/lessons/42889))

  1) 2차원리스트 만들고, 요소는 [스테이지 번호, 실패율]
  2) 실패율 내림차순으로 정렬
  3) 다시 스테이지 번호만 answer로 정의
  4) 테스트 1, 6, 7, 9, 13, 23, 24, 25 : 런타임 에러 | 테스트 22 : 시간초과
  5) ㅠㅠㅠ

# 10.  소수 만들기 - Summer/Winter Coding(~2018)([https://school.programmers.co.kr/learn/courses/30/lessons/12977](https://school.programmers.co.kr/learn/courses/30/lessons/12977))

  - 경우의 수 구현을 잘 못하겠어서, `itertools.combinations` 사용
  - 소수 판별 함수 `is_prime_number()`정의 후 경우의 수마다 확인하여 `answer += 1`
  - done