SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(e.matr) AS "Numero de Empregados",
    ROUND(COALESCE(AVG(
        (SELECT COALESCE(SUM(v.valor), 0)
         FROM emp_venc ev 
         JOIN vencimento v ON v.cod_venc = ev.cod_venc
         WHERE ev.matr = e.matr) -
        (SELECT COALESCE(SUM(d.valor), 0)
         FROM emp_desc ed
         JOIN desconto d ON d.cod_desc = ed.cod_desc
         WHERE ed.matr = e.matr)
    ), 0), 2) AS "Media Salarial",
    ROUND(COALESCE(MAX(
        (SELECT COALESCE(SUM(v.valor), 0)
         FROM emp_venc ev 
         JOIN vencimento v ON v.cod_venc = ev.cod_venc
         WHERE ev.matr = e.matr) -
        (SELECT COALESCE(SUM(d.valor), 0)
         FROM emp_desc ed
         JOIN desconto d ON d.cod_desc = ed.cod_desc
         WHERE ed.matr = e.matr)
    ), 0), 2) AS "Maior Salario",
    ROUND(COALESCE(MIN(
        (SELECT COALESCE(SUM(v.valor), 0)
         FROM emp_venc ev 
         JOIN vencimento v ON v.cod_venc = ev.cod_venc
         WHERE ev.matr = e.matr) -
        (SELECT COALESCE(SUM(d.valor), 0)
         FROM emp_desc ed
         JOIN desconto d ON d.cod_desc = ed.cod_desc
         WHERE ed.matr = e.matr)
    ), 0), 2) AS "Menor Salario"
FROM 
    departamento dep
LEFT JOIN 
    empregado e ON dep.cod_dep = e.lotacao
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;

--

SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(e.matr) AS "Numero de Empregados",
    ROUND(COALESCE(AVG(
        COALESCE(
            (SELECT SUM(v.valor) FROM emp_venc ev JOIN vencimento v ON v.cod_venc = ev.cod_venc WHERE ev.matr = e.matr), 0) 
        - COALESCE(
            (SELECT SUM(d.valor) FROM emp_desc ed JOIN desconto d ON d.cod_desc = ed.cod_desc WHERE ed.matr = e.matr), 0)
    ), 0), 2) AS "Media Salarial",
    ROUND(COALESCE(MAX(
        COALESCE(
            (SELECT SUM(v.valor) FROM emp_venc ev JOIN vencimento v ON v.cod_venc = ev.cod_venc WHERE ev.matr = e.matr), 0)
        - COALESCE(
            (SELECT SUM(d.valor) FROM emp_desc ed JOIN desconto d ON d.cod_desc = ed.cod_desc WHERE ed.matr = e.matr), 0)
    ), 0), 2) AS "Maior Salario",
    ROUND(COALESCE(MIN(
        COALESCE(
            (SELECT SUM(v.valor) FROM emp_venc ev JOIN vencimento v ON v.cod_venc = ev.cod_venc WHERE ev.matr = e.matr), 0)
        - COALESCE(
            (SELECT SUM(d.valor) FROM emp_desc ed JOIN desconto d ON d.cod_desc = ed.cod_desc WHERE ed.matr = e.matr), 0)
    ), 0), 2) AS "Menor Salario"
FROM 
    departamento dep
LEFT JOIN 
    empregado e ON dep.cod_dep = e.lotacao
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;

---

SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(e.matr) AS "Numero de Empregados",
    ROUND(
        COALESCE(
            AVG(
                COALESCE(
                    (SELECT SUM(v.valor) FROM emp_venc ev JOIN vencimento v ON v.cod_venc = ev.cod_venc WHERE ev.matr = e.matr), 0
                ) - COALESCE(
                    (SELECT SUM(d.valor) FROM emp_desc ed JOIN desconto d ON d.cod_desc = ed.cod_desc WHERE ed.matr = e.matr), 0
                )
            ), 0
        ), 2
    ) AS "Media Salarial",
    ROUND(
        COALESCE(
            MAX(
                COALESCE(
                    (SELECT SUM(v.valor) FROM emp_venc ev JOIN vencimento v ON v.cod_venc = ev.cod_venc WHERE ev.matr = e.matr), 0
                ) - COALESCE(
                    (SELECT SUM(d.valor) FROM emp_desc ed JOIN desconto d ON d.cod_desc = ed.cod_desc WHERE ed.matr = e.matr), 0
                )
            ), 0
        ), 2
    ) AS "Maior Salario",
    ROUND(
        COALESCE(
            MIN(
                COALESCE(
                    (SELECT SUM(v.valor) FROM emp_venc ev JOIN vencimento v ON v.cod_venc = ev.cod_venc WHERE ev.matr = e.matr), 0
                ) - COALESCE(
                    (SELECT SUM(d.valor) FROM emp_desc ed JOIN desconto d ON d.cod_desc = ed.cod_desc WHERE ed.matr = e.matr), 0
                )
            ), 0
        ), 2
    ) AS "Menor Salario"
FROM 
    departamento dep
LEFT JOIN 
    empregado e ON dep.cod_dep = e.lotacao
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;

---

/**
 * Escreva a sua solução aqui
 * Code your solution here
 * Escriba su solución aquí
 */
SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(e.matr) AS "Quantidade Empregados",
    ROUND(COALESCE(AVG(
        (SELECT COALESCE(SUM(v.valor), 0)
         FROM emp_venc ev 
         JOIN vencimento v ON v.cod_venc = ev.cod_venc
         WHERE ev.matr = e.matr) -
        (SELECT COALESCE(SUM(d.valor), 0)
         FROM emp_desc ed
         JOIN desconto d ON d.cod_desc = ed.cod_desc
         WHERE ed.matr = e.matr)
    ), 0), 2) AS "Media Salarial",
    ROUND(COALESCE(MAX(
        (SELECT COALESCE(SUM(v.valor), 0)
         FROM emp_venc ev 
         JOIN vencimento v ON v.cod_venc = ev.cod_venc
         WHERE ev.matr = e.matr) -
        (SELECT COALESCE(SUM(d.valor), 0)
         FROM emp_desc ed
         JOIN desconto d ON d.cod_desc = ed.cod_desc
         WHERE ed.matr = e.matr)
    ), 0), 2) AS "Maior Salario",
    ROUND(COALESCE(MIN(
        (SELECT COALESCE(SUM(v.valor), 0)
         FROM emp_venc ev 
         JOIN vencimento v ON v.cod_venc = ev.cod_venc
         WHERE ev.matr = e.matr) -
        (SELECT COALESCE(SUM(d.valor), 0)
         FROM emp_desc ed
         JOIN desconto d ON d.cod_desc = ed.cod_desc
         WHERE ed.matr = e.matr)
    ), 0), 2) AS "Menor Salario"
FROM 
    departamento dep
    LEFT JOIN divisao div ON div.cod_dep = dep.cod_dep
    LEFT JOIN empregado e ON e.lotacao_div = div.cod_divisao
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;

---

SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(e.matr) AS "Numero de Empregados",
    ROUND(COALESCE(AVG(
        COALESCE((SELECT SUM(v.valor)
                  FROM emp_venc ev
                  JOIN vencimento v ON v.cod_venc = ev.cod_venc
                  WHERE ev.matr = e.matr), 0) -
        COALESCE((SELECT SUM(d.valor)
                  FROM emp_desc ed
                  JOIN desconto d ON d.cod_desc = ed.cod_desc
                  WHERE ed.matr = e.matr), 0)
    ), 0), 2) AS "Media Salarial",
    ROUND(COALESCE(MAX(
        COALESCE((SELECT SUM(v.valor)
                  FROM emp_venc ev
                  JOIN vencimento v ON v.cod_venc = ev.cod_venc
                  WHERE ev.matr = e.matr), 0) -
        COALESCE((SELECT SUM(d.valor)
                  FROM emp_desc ed
                  JOIN desconto d ON d.cod_desc = ed.cod_desc
                  WHERE ed.matr = e.matr), 0)
    ), 0), 2) AS "Maior Salario",
    ROUND(COALESCE(MIN(
        COALESCE((SELECT SUM(v.valor)
                  FROM emp_venc ev
                  JOIN vencimento v ON v.cod_venc = ev.cod_venc
                  WHERE ev.matr = e.matr), 0) -
        COALESCE((SELECT SUM(d.valor)
                  FROM emp_desc ed
                  JOIN desconto d ON d.cod_desc = ed.cod_desc
                  WHERE ed.matr = e.matr), 0)
    ), 0), 2) AS "Menor Salario"
FROM 
    departamento dep
    LEFT JOIN divisao div ON div.cod_dep = dep.cod_dep
    LEFT JOIN empregado e ON e.lotacao_div = div.cod_divisao
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;

---

SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(e.matr) AS "Numero de Empregados",
    ROUND(COALESCE(AVG(
        COALESCE((SELECT SUM(v.valor)
                  FROM emp_venc ev
                  JOIN vencimento v ON v.cod_venc = ev.cod_venc
                  WHERE ev.matr = e.matr), 0) -
        COALESCE((SELECT SUM(d.valor)
                  FROM emp_desc ed
                  JOIN desconto d ON d.cod_desc = ed.cod_desc
                  WHERE ed.matr = e.matr AND d.valor IS NOT NULL), 0)
    ), 0), 2) AS "Media Salarial",
    ROUND(COALESCE(MAX(
        COALESCE((SELECT SUM(v.valor)
                  FROM emp_venc ev
                  JOIN vencimento v ON v.cod_venc = ev.cod_venc
                  WHERE ev.matr = e.matr), 0) -
        COALESCE((SELECT SUM(d.valor)
                  FROM emp_desc ed
                  JOIN desconto d ON d.cod_desc = ed.cod_desc
                  WHERE ed.matr = e.matr AND d.valor IS NOT NULL), 0)
    ), 0), 2) AS "Maior Salario",
    ROUND(COALESCE(MIN(
        COALESCE((SELECT SUM(v.valor)
                  FROM emp_venc ev
                  JOIN vencimento v ON v.cod_venc = ev.cod_venc
                  WHERE ev.matr = e.matr), 0) -
        COALESCE((SELECT SUM(d.valor)
                  FROM emp_desc ed
                  JOIN desconto d ON d.cod_desc = ed.cod_desc
                  WHERE ed.matr = e.matr AND d.valor IS NOT NULL), 0)
    ), 0), 2) AS "Menor Salario"
FROM 
    departamento dep
    LEFT JOIN empregado e ON e.lotacao_dep = dep.cod_dep
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;

---

SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(e.matr) AS "Numero de Empregados",
    ROUND(COALESCE(AVG(COALESCE(venc.total_venc, 0) - COALESCE(desc.total_desc, 0)), 0), 2) AS "Media Salarial",
    ROUND(COALESCE(MAX(COALESCE(venc.total_venc, 0) - COALESCE(desc.total_desc, 0)), 0), 2) AS "Maior Salario",
    ROUND(COALESCE(MIN(COALESCE(venc.total_venc, 0) - COALESCE(desc.total_desc, 0)), 0), 2) AS "Menor Salario"
FROM 
    departamento dep
    LEFT JOIN empregado e ON e.lotacao_dep = dep.cod_dep
    LEFT JOIN (
        SELECT ev.matr, SUM(v.valor) AS total_venc
        FROM emp_venc ev
        JOIN vencimento v ON v.cod_venc = ev.cod_venc
        GROUP BY ev.matr
    ) AS venc ON venc.matr = e.matr
    LEFT JOIN (
        SELECT ed.matr, SUM(d.valor) AS total_desc
        FROM emp_desc ed
        JOIN desconto d ON d.cod_desc = ed.cod_desc
        WHERE d.valor IS NOT NULL
        GROUP BY ed.matr
    ) AS desc ON desc.matr = e.matr
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;

---

WITH Salarios AS (
    SELECT 
        e.matr,
        e.lotacao_dep AS cod_dep,
        COALESCE(SUM(v.valor), 0) - COALESCE(SUM(d.valor), 0) AS salario_liquido
    FROM 
        empregado e
    LEFT JOIN emp_venc ev ON e.matr = ev.matr
    LEFT JOIN vencimento v ON ev.cod_venc = v.cod_venc
    LEFT JOIN emp_desc ed ON e.matr = ed.matr
    LEFT JOIN desconto d ON ed.cod_desc = d.cod_desc AND d.valor IS NOT NULL
    GROUP BY e.matr, e.lotacao_dep
)
SELECT 
    dep.nome AS "Nome Departamento",
    COUNT(s.matr) AS "Numero de Empregados",
    ROUND(COALESCE(AVG(s.salario_liquido), 0), 2) AS "Media Salarial",
    ROUND(COALESCE(MAX(s.salario_liquido), 0), 2) AS "Maior Salario",
    ROUND(COALESCE(MIN(s.salario_liquido), 0), 2) AS "Menor Salario"
FROM 
    departamento dep
LEFT JOIN Salarios s ON s.cod_dep = dep.cod_dep
GROUP BY 
    dep.nome
ORDER BY 
    "Media Salarial" DESC;
