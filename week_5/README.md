# 1. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/43165">타겟 넘버</a>
- DFS 구현
  - `numbers`의 길이가 0이 될때까지, `재귀`적으로 더하거나 뺀다.
  - `numbers`의 길이가 0일때 sum과 target이 같다면 1을 반환
  - 반환된 1을 합산해주면 정답
  - done.

# 2. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/1844">게임 맵 최단거리</a>
- DFS 풀이 시도
  - 방문한 좌표를 0으로 바꿔 다시 방문 하지 못하도록 했음
  - 한칸 전진할 때 마다, `cnt`변수를 `+1`하고 `재귀`
  - 목표한 좌표에 도달하면 `answer`를 `cnt`로 반환
  - 어떤 이유인지 모르겠으나, 채점 결과 많은 실패율..
  - fail
  
- BFS 풀이 시도
  1) 방문 좌표 `visited` 변수에 담아두기
     - 전진하며 방문한 좌표를 `visited` 변수에 담아두어, 목표에 도달하면 `len(visited)`를 반환하려 했음
     - 방문한 좌표를 `visited`안에서 찾으려 할 때, 이미 방문하였지만 다시 되돌아 가는 경우가 생겼음.
     - fail

  2) 다음 방문할 좌표에 현재 방문한 좌표의 count?를 더해줌
    - 다음 방문할 좌표에 계속 `+1`을 통해 몇칸 이동했는지 알 수 있음.
    - `while`반복문 안에서 목표에 도달했을 경우 목표 좌표의 값을 반환
    - `while`반복문이 끝날동안 함수가 종료되지 않았다면, 목표에 도달할 수 없다고 판단, `-1`을 반환
    - done.

# 3. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/43238">입국심사</a>
- 제한사항에서 `1,000,000,000분`이하 인 것을 보고, 시간을 줄여야 하겠다고 생각해야 한다.
- 이분탐색 사용
  - `mid`시간동안, 몇 명이 심사받을 수 있는지 `people`에 담고
  - `n명`과 비교하여 다시 이분탐색,
  - 심사 받을 수 있는 `people`과 `n`이 같다면 정답이다.
  - done.