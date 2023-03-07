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