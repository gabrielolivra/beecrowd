SELECT 
    d.name, 
    SUM(
        CASE 
            WHEN w.name = 'nocturnal' THEN ROUND((A.hours * 150) + ( (A.hours * 150) * 0.15),1)
            WHEN w.name = 'afternoon' THEN ROUND((A.hours * 150) + ( (A.hours * 150) * 0.02),1)
            WHEN w.name = 'day' THEN ROUND((A.hours * 150) + ( (A.hours * 150) * 0.01),1)
            ELSE 0  
        END
    ) AS salary
FROM 
    doctors d
    INNER JOIN attendances a ON a.id_doctor = d.id
    INNER JOIN work_shifts w ON w.id = a.id_work_shift
GROUP BY 
    d.name
ORDER BY
    salary DESC;