 STEP 1 — CREATE BASE ANALYSIS QUERY

SELECT username,
       status,
       attempts
FROM logins;
_____

STEP 2 — FAILED LOGIN FILTER

SELECT username,
       attempts
FROM logins
WHERE status = 'FAILED';
_____

STEP 3 — USER LOGIN COUNT (BEHAVIOR VIEW)

SELECT username,
       COUNT(*) AS total_logins
FROM logins
GROUP BY username;
_____

STEP 4 — FAILED LOGIN COUNT PER USER

SELECT username,
       COUNT(*) AS failed_logins
FROM logins
WHERE status = 'FAILED'
GROUP BY username;
_____

STEP 5 — RISK CLASSIFICATION

SELECT username,
       COUNT(*) AS failed_logins,
       CASE
           WHEN COUNT(*) >= 5 THEN 'CRITICAL'
           WHEN COUNT(*) >= 2 THEN 'WARNING'
           ELSE 'LOW'
       END AS risk_level
FROM logins
WHERE status = 'FAILED'
GROUP BY username;
_____

STEP 6 — CRITICAL USERS ONLY

SELECT username,
       COUNT(*) AS failed_logins,
       CASE
           WHEN COUNT(*) >= 5 THEN 'CRITICAL'
           WHEN COUNT(*) >= 2 THEN 'WARNING'
           ELSE 'LOW'
       END AS risk_level
FROM logins
WHERE status = 'FAILED'
GROUP BY username
HAVING COUNT(*) >= 5;

⸻

STEP 7 — FINAL INVESTIGATION QUERY 

SELECT username,
       COUNT(*) AS failed_logins,
       CASE
           WHEN COUNT(*) >= 5 THEN 'CRITICAL'
           WHEN COUNT(*) >= 2 THEN 'WARNING'
           ELSE 'LOW'
       END AS risk_level
FROM logins
WHERE status = 'FAILED'
GROUP BY username
ORDER BY failed_logins DESC;
