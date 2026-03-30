-- 코드를 입력하세요
-- 회원 이름, 리뷰 텍스트, 리뷰 작성일
-- 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
SELECT m.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, "%Y-%m-%d")
FROM REST_REVIEW r

JOIN MEMBER_PROFILE m
    ON m.MEMBER_ID = r.MEMBER_ID

WHERE r.MEMBER_ID = (SELECT MEMBER_ID
                    FROM REST_REVIEW
                    GROUP BY MEMBER_ID
                    ORDER BY COUNT(*) DESC
                    LIMIT 1)

ORDER BY r.REVIEW_DATE , r.REVIEW_TEXT
-- 리뷰 작성일을 기준으로 오름차순, 리뷰 텍스트를 기준으로 오름차순 정렬