-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
-- 진료예약일시를 기준으로 오름차순 정렬
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A
JOIN PATIENT P ON P.PT_NO = A.PT_NO
JOIN DOCTOR D ON D.DR_ID = A.MDDR_ID
WHERE A.MCDP_CD = 'CS' AND A.APNT_CNCL_YN = 'N' AND DATE_FORMAT(APNT_YMD, "%Y-%m-%d") = "2022-04-13"
ORDER BY APNT_YMD