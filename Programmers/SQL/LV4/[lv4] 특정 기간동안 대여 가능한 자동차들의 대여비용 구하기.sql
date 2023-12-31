--  자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차
-- 대여 금액을 기준으로 내림차순, 자동차 종류를 기준으로 오름차순, 자동차 ID를 기준으로 내림차순
SELECT DISTINCT C.CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
JOIN CAR_RENTAL_COMPANY_CAR C ON C.CAR_TYPE = P.CAR_TYPE
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON H.CAR_ID = C.CAR_ID
WHERE P.CAR_TYPE IN ('세단', 'SUV') AND P.DURATION_TYPE = '30일 이상' 
AND C.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE <= "2022-11-30" AND END_DATE >= "2022-11-01"
)
AND ROUND(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) >= 500000 AND ROUND(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) < 2000000
ORDER BY FEE DESC, C.CAR_TYPE, C.CAR_ID DESC