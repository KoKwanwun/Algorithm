-- floor(PRICE / 10000) * 10000로 첫번째 열을 생성한 후, floor(PRICE / 10000) * 10000로 그룹으로 묶어주고 count로 개수 구함
-- floor : 내림
-- order by : 1이면 1열 기준으로 정렬
SELECT floor(PRICE / 10000) * 10000 as PRICE_GROUP, count(*) as PRODUCTS
FROM PRODUCT
GROUP BY floor(PRICE / 10000) * 10000
ORDER BY 1