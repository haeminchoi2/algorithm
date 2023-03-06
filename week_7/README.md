# 2. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/64061">크레인 인형 뽑기</a>
- 유형은 구현인 듯
- `stack`이 생각나서 유사하게 풀이 함.
- 경우에 따라서, `stack list`에 `append` 또는 `pop`을 해줌.
- done.

# 3. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/64061">로또의 최고 순위와 최저 순위</a>
- 구현문제
- 로또 순위를 `dict`로 초기화
- `lottos`안에 일치하는 숫자가 있는지 `cnt`변수에 담고
- 0의 갯수대로 로또번호를 최대로 넣을 수 있다.
- 차례대로 `answer`에 `append`해준다.
- done.

# 4. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/64061">로또의 최고 순위와 최저 순위</a>
- 구현문제 인줄 알았으나, 다른 사람 풀이를 보니 **`Stack`으로도 풀이 가능**
1. 행렬을 만듦
2. 쿼리에 따라서, 순서대로 숫자들과 숫자들의 꼭지점들을 담아주었음.
3. 숫자들중에서 최소값을 구해주고
4. 구해낸 꼭지점들을 이용해서 다시 숫자행렬을 고쳐줌
- done.

# 5. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/77486">다단계 칫솔 판매</a>
- 구현문제
1. `딕셔너리 자료형`으로 관계를 만들어줌.
2. 수익을 낸 사람들을 `for`문 돌면서
3. 한명이 수익을 냈을 때, `while`문으로 분배를 안할때 까지 각자의 수익에 더해준다
4. **`math.ceil` 과 `math.floor`** 사용하지 않으면 에러가 발생했었음.
- done.

# 6. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42577">전화번호목록</a>
- 해쉬 유형
1. `dict`자료형을 이용해 해쉬맵을 만들어준다.
2. 전화번호부에서 차례로 반복문, 전화번호 숫자를 차례로 돌면서 임의의 접두어를 만들어 간다.
3. 분기문으로 딕셔너리 key값에서 찾으면 정답
- done.
  
# 7. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42627">디스크 컨트롤러</a>
- 힙 유형
1. 정렬하고, `heapify`후 구현하려 했으나, 힙 자료구조로 만들때 원하는 대로 만들어지지 않음.
   - fail
2. 총 시간과 현재시간, 이전 작업의 시작시간을 초기화하고
3. 이전 작업의 시작시간과 현재시간 동안 작업을 기다릴 수 있으면 힙 배열에 추가.
   - 이 때, 소요시간이 작은 순으로 push가 되어야 한다.
   - heapq 정렬이 첫번째 원소를 기준으로 최소힙을 구현해준다.
4. 조건대로 구현해주고, 힙 배열에 원소가 없을 때는 기다릴수 있는 작업이 없으므로 현재시간 +1을 해준다.
5. done.

# 8. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/43162">네트워크</a>
- 완전탐색 유형
1. `BFS`이용, 주어진 `computers`를 돌면서 이어진 노드를 탐색
2. 이미 존재하는 네트워크아니라면, 리스트에 추가
3. 정답 리스트의 `len()`가 답안!
4. done.

# 9. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42746">가장 큰 수</a>
- 정렬 유형
- 이게 왜 정렬인지 잘 와닿지 않는다...
1. `itertools`의 `permutations`이용해서 `max`값만 추출
2. 모두 시간초과로 실패

1. `numbers`를 문자열로 바꾸고
2. 문자열 리스트를 정렬해준다
3. 정렬시 최대값이 1000이므로 자리값을 맞춰주기 위해 `문자열*3`해준다
   1. 문자열 정렬시 `ASCII`코드를 기준으로 대소비교를 한다...
4. done.


