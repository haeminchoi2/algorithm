# 1. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12906">같은 숫자는 싫어</a>
- 스택
- 임의의 배열에 첫 숫자를 넣어 놓는다.
- 차례로 반복문 돌면서 array의 `-1`인덱스 값과 확인하여
- 일치하지 않으면 array에 `appned`
- done.

# 2. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/59040">중복제거</a>
- SQL
- `GROUP BY`해주고
- 고양이 먼저 조회하라는 조건이 있어서
- `ORDER BY`로 문자열순으로 정렬
- done.

# 4. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/72410">신규 아이디 추천</a>
- 구현문제
- `re.findall(pattern, str)`
- `re.sub(pattern, replace, str)`
- done.

# 5. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/59043">있었는데요 없었습니다</a>
- SQL
- `INNER JOIN`으로 묶어주고
- `DATETIME` 대소비교를 통해 날짜 정렬
- done.

# 7. <a href="https://www.acmicpc.net/problem/1920">수찾기</a>
- 이진탐색
- `bisect` 모듈 이용
- `bisect_left` 사용 이진탐색을 이용해 왼쪽의 `index`를 구해준다.
  - 사용해본 결과 배열안에 없으면 `index`를 초과해 버린다.
- `index`가 배열의 길이보다 작고, 현재 비교하는 숫자와 배열 인덱스에 위치해있는 숫자가 같으면 1을 출력해준다.
  - 비교해볼 숫자가 음수일 때 조건을 만족할 수 있으므로 배열이 있는지 확인해준다
- done.