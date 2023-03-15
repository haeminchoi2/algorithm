-- https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d')
FROM BOOK as b, AUTHOR as a
WHERE b.author_id = a.author_id AND category = "경제"
ORDER BY PUBLISHED_DATE
;