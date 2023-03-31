# 1. <a href="https://leetcode.com/problems/two-sum/">Two Sum</a>
- 구현
- nums 배열 돌면서
- 다시 nums배열을 반복하며
- 두 수의 합이 같으면
- index를 바로 반환해준다.
- done.
- 소요시간 : 30분

# 2. <a href="https://leetcode.com/problems/add-two-numbers/">Add Two Numbers</a>
- 구현 근데 링크드리스트를 곁들인..
- 빈 문자열 만들고
- 역순으로 들어갈 수 있게 구현
- 덧셈 해주고나서
- 다시 리스트형태로 펼치기
- 링크드리스트로 구현하지 않으면 안됌..
  - 링크드 리스트 구현하기 위해 검색했습니다.
  - 공부가 필요한 부분
- 소요시간 : 90분

# 3. <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">Longest_Substring_Without_Repeating_Characters</a>
- ??
- 인덱스 0부터 시작하여
- 1글자, 2글자, 3글자... len(s) 만큼 글자수만큼
- 잘라보고
- 끝까지 잘라보면서 제일 큰 부분문자열을 찾아본다
- fail
  - abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
  - 무한반복은 생각도 못함........
  - 위의 배열이 반복되니까 스택이나 큐로 계속 넣어보면서 비교하기??
----
- Queue를 이용한 풀이 방법(참고했음)
- 큐를 만들어주고, 이미 나왔던 문자인지 확인하기 위한 딕셔너리도 만들어준다.
- 문자열을 차례대로 반복문 돌면서
- 큐에 넣어 substring을 만들고, 같은 문자가 나오면 그 이전까지 계속 지워줘서 다시 substring 문자를 만든다.
- done.

# 4. <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/">Median of Two Sorted Arrays</a>
- Hard난이도의 문제
- 단순하게 구현할 수 있지만, O(log(m+n))이어야 한다.
- 단순하게 풀어보았다.
- 두 배열을 합치고
- `sort()`를 이용 정렬한 뒤
- 조건에 맞게 미들값을 구했다
- `sort()`가 O(N*logN)이지만 통과했다..
- done.
- 소요시간 : 10분

# 5. <a href="https://leetcode.com/problems/longest-palindromic-substring/">Longest Palindromic Substring</a>
- 
