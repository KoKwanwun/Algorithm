-- 재구매한 회원 ID와 재구매한 상품 ID를 출력
-- 회원 ID를 기준으로 오름차순 정렬, 상품 ID를 기준으로 내림차순 정렬
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY 1, 2
HAVING COUNT(USER_ID) >= 2
ORDER BY 1, 2 DESC