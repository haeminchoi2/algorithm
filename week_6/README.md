# 1. <a href="https://www.acmicpc.net/problem/1912">연속합</a>
- 다이나믹 프로그래밍
- 이전에 풀어봤던 다이나믹 프로그래밍에서 배열을 하나 만들어서, 기록해가며 비교했던 기억이 남
- 12 + 21이 정답인데, 쭉 더하다가 `시작하는 숫자`를 어떻게 바꾸는지가 중요..
  - Key! 이전까지 합 + 현재 숫자 vs 현재 숫자
- done.

# 6. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/72410">신규 아이디 추천</a>
- 유형 알수없음. 구현문제 인듯
- 2단계, 3단계에서 `filter`쓰려다, 정규식 사용함
- `re.findall(pattern, str)`
- `re.sub(pattern, replace, str)`
- done.

# 7. <a href="https://school.programmers.co.kr/learn/courses/30/lessons/67256">키패드 누르기</a>
- 유형은 모르겠음. 그냥 구현인듯
- 왼쪽, 가운데, 오른쪽 키패드를 `list`로 초기화 하고
- 각 조건마다 구현해 줌.
- done.

# 8. <a href="https://www.acmicpc.net/problem/10844">쉬운 계단수</a>
- DP
- 계단수가 되는 경우의 수를 쭉 구해보았음.
- 1의 자릿수부터 경우의 수를 구해
  - 10, 100 ... 경우의 수를 구해보고
  - 패턴을 찾는다.
  - 이전 자릿수의 `i-1` `i+1`경우의 수를 더한다.

# 9. <a href="https://www.acmicpc.net/problem/1932">정수 삼각형</a>
- DP
  1. 모든 경우의 수 더한 값을 dp리스트에 담아서 `max`함수 사용하려 함
     - 양 끝에 있는 숫자가 아닐 경우 모든 경우의 수를 더한 값이 맞지 않아서 fail.
  2. 양 끝에 있는 숫자가 아닐 경우, 더한 값이 2개가 나오는데 이 중 큰것으로 구함.
     - 이렇게 해야 배열의 자릿수가 맞아서, 원하는 경우의 수를 구할 수 있음.
     - done.