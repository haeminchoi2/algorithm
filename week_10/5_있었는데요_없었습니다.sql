-- https://school.programmers.co.kr/learn/courses/30/lessons/59043


SELECT i.ANIMAL_ID, i.NAME
FROM ANIMAL_OUTS as o
JOIN ANIMAL_INS as i
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.DATETIME > o.DATETIME
ORDER BY i.DATETIME
;