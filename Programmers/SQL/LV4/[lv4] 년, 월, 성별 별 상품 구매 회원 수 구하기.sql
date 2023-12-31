-- 년, 월, 성별 별로 상품을 구매한 회원수를 집계
-- 년, 월, 성별을 기준으로 오름차순
-- 성별 정보가 없는 경우 결과에서 제외
-- 중복 제거를 위해 DISTINCT를 사용해줘야 함
SELECT YEAR(O.SALES_DATE) AS YEAR, MONTH(O.SALES_DATE) AS MONTH, U.GENDER, COUNT(DISTINCT U.USER_ID) AS USERS
FROM ONLINE_SALE O
JOIN USER_INFO U USING (USER_ID)
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, U.GENDER
ORDER BY YEAR, MONTH, U.GENDER