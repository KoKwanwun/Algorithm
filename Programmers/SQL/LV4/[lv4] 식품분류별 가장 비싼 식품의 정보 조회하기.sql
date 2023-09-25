-- FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
-- 결과는 식품 가격을 기준으로 내림차순 정렬
-- MAX는 행이 달라져서 서브쿼리 활용해야 함
SELECT A.CATEGORY, A.MAX_PRICE, PRODUCT_NAME
FROM (
    SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
) A
JOIN FOOD_PRODUCT B ON A.CATEGORY = B.CATEGORY AND A.MAX_PRICE = B.PRICE
ORDER BY MAX_PRICE DESC