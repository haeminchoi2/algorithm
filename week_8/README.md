# 1. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42888">오픈채팅방</a>
- 구현문제인듯
- 닉네임 변경이 최종적으로 완료된 배열을 만들고
- 다시 record를 반복문 돌면서 조건에 맞게 순서대로 answer리스트에 넣어준다.
- done.

# 2. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42888">단어 변환</a>
- BFS/DFS 유형이다

### 내 풀이
1. 단어들을 하나씩 돌면서
2. 알파벳의 인덱스 위치가 begin과 일치하지 않고, target과 일치하면
3. begin을 word로 바꿈
4. 알파벳 1개만 바꿀수 있는 조건을 지키지 못함
5. fail

### 참고후 풀이
1. `"dog"`와 `"log"` 둘 중 하나만 방문해도 4회가 나오므로 탐색문제이다.
2. BFS 이용
3. 큐에 시작단어와 `begin`과 다른 알파벳 갯수를 넣어준다.
4. 조건대로 알파벳 위치와 알파벳이 다른지 체크하고, 다른 알파벳 갯수를 세준다.
5. 갯수가 1개라면 큐에 넣어주고, 방문처리
6. 다 돌고 나면 answer를 반환해준다.

# 5. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/59405">상위 n개 레코드</a>
- SQL
- 이름을 조회해야 하므로 `SELECT NAME`
- 날짜를 기준으로 정렬 `ORDER BY`
- `LIMIT`를 통해 위에서 갯수로 잘라온다.
- done.

# 6. <a href="https://www.acmicpc.net/problem/11279">최대 힙</a>
- 힙 유형
- 최대 힙 구하기
1. `heapq`모듈을 이용해 풀이
2. 최대 힙은 `최소 힙에서 음수값을 이용하면 된다.`
3. 조건에 따라 구현하면 끝
4. done.

# 7. <a href="https://www.acmicpc.net/problem/1927">최소 힙</a>
- 힙 유형
1. `heapq`모듈을 이용해 풀이
2. 조건에 따라 구현하면 끝
3. 입력값 받을때 `input()`사용했더니 시간초과....
4. `sys.stdin.readline()`사용하여 통과
5. done.

# 8. <a href="https://www.acmicpc.net/problem/11286">절대값 힙</a>
- 힙 유형
1. `heapq`모듈을 이용해 풀이
2. 조건에 따라 구현하면 끝
3. `heappush`를 할 때, 막무가내로 `list`자료형으로 넣어봤더니 통과...!!
  - 첫번째 원소를 기준으로 먼저 정렬하고, 첫번째 원소가 같으면 두번째 원소를 기준으로 정렬해준다.
4. done.

# 9. <a href="https://www.acmicpc.net/problem/11066">파일합치기</a>
- 동적프로그래밍 유형
1. 첫번째 풀이
  - dp에 인덱스 값에 있는 숫자까지 최소 합을 구해서
  - 다 더하려고 했으나
  - 원하는 값이 나오지 않음
  - fail.

# 10. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/59408">중복제거</a>
- SQL
1. `FROM`절에 그룹바이한 서브쿼리 사용해서 중복 없애고, `COUNT(*)`로 조회
  - `Every derived table must have its own alias.`에러 발생
  - 서브쿼리 사용시 `alias`지정 안해줘서 생긴 에러
  - 서브쿼리 뒤에 `as A`라고 지정해주고 조회
  - 카운트가 97개가 되서 실패. 아마 `NULL`값이 조회되는 것 같아서
  - `WHERE`절 추가
  - done.

2. `DISTINCT`사용
  - `DISTINCT column`을 사용하면 `column`의 중복을 제거하고 조회해준다.
  - `WHERE`절을 사용하지 않아도 `NULL`값이 제외된다??
    - 단순히 `SELECT DISTINCT column`을 사용하면 `NULL`값 포함하여 조회된다.
    - `COUNT`함수로 감싸주면 `NULL`은 제외하고 조회해준다.
