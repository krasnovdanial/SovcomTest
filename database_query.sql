--a. Десять лиц с наибольшим количеством обязательств:

SELECT d.name, d.inn, COUNT(m.id) AS obligations_count
FROM debtors d
JOIN monetary_obligations m ON m.debtor_id = d.id
GROUP BY d.id
ORDER BY obligations_count DESC
LIMIT 10;


--b. Десять лиц с наибольшей общей суммой задолженностей:

SELECT d.name, d.inn, SUM(m.debt_sum) AS total_debt_sum
FROM debtors d
JOIN monetary_obligations m ON m.debtor_id = d.id
GROUP BY d.id
ORDER BY total_debt_sum DESC
LIMIT 10;


--c. Все физические лица с процентом выплаченной суммы по обязательствам:

SELECT
  d.name,
  d.inn,
  ((SUM(m.total_sum) - SUM(m.debt_sum)) / SUM(m.total_sum) * 100) AS paid_percentage
FROM debtors d
JOIN monetary_obligations m ON m.debtor_id = d.id
GROUP BY d.id
ORDER BY paid_percentage;