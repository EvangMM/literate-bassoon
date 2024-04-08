WITH tab AS (
    SELECT  *
    FROM    {{ ref('employees') }}
)
SELECT  *
FROM    tab
WHERE   tab."DEPARTMENT_ID" = '60'
