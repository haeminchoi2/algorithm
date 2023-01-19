# 1. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/86491">최소 직사각형</a>
- 가로와 세로는 바꿀수 있기 때문에, 의미가 없다.
- 명함 가로/세로 중 `가장 큰 값`은 무조건 `넓이`
- 명함 가로/세로 중 `작은 값` 중에 가장 큰 값이 `높이`
- done.

# 2. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42840">모의고사</a>
- 정답 개수를 세는 `cnt`변수 초기화
- 패턴에 맞게 사람1, 사람2, 사람3 초기화
- 정답 반복문 돌면서, 정답이면 `cnt += 1`
- 정답이 될 리스트에 순서대로 `append`
- 채점시 실패한 테스트가 있음ㅠㅠ

# 3. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42839">소수찾기</a>
- `itertools`의 `permutations`이용
  - **순서가 중요한 조합 == `순열`**을 생각해내야 함
    - 다른 개념으로 **순서X 와 중복없이 == `조합`**
- `순열`은 중복을 갖고 있을수 있으므로, `set()`을 통해 중복 제거 후 개수 계산
- done

# 4. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42842">카펫</a>
- 