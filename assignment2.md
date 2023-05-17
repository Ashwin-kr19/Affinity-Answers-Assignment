# Assignment 2
## SQL

1. SQL query To find the number of types of tigers in the taxonomy table and the "ncbi_id" of the Sumatran Tiger:
  ```sql
SELECT COUNT(DISTINCT tax_string) AS Number_of_Tiger_Types
FROM taxonomy
WHERE tax_string LIKE '%Tiger%';

SELECT ncbi_id
FROM taxonomy
WHERE tax_string = 'Panthera tigris sondaica' -- Sumatran Tiger
LIMIT 1;
```
---
2. SQL query To find all the columns that can be used to connect the tables in the given database:

```sql
SELECT
  CONSTRAINT_NAME,
  TABLE_NAME,
  COLUMN_NAME,
  REFERENCED_TABLE_NAME,
  REFERENCED_COLUMN_NAME
FROM
  INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
  CONSTRAINT_SCHEMA = 'Rfam' -- Replace 'Rfam' with the actual database name if different
  AND REFERENCED_TABLE_NAME IS NOT NULL;
```
---
3. SQL query for Which type of rice has the longest DNA sequence:
  ```sql
SELECT
  tx.type AS rice_type,
  MAX(rs.seq_length) AS longest_sequence_length
FROM
  rfamseq rs
JOIN
  taxonomy tx ON rs.ncbi_id = tx.ncbi_id
WHERE
  tx.type LIKE '%rice%'
GROUP BY
  rice_type;
```
---
4. SQL query that will return the 9th page when there are 15 results per page:
````sql
SELECT
  f.family_accession AS family_accession,
  f.family_name AS family_name,
  MAX(rs.seq_length) AS max_length
FROM
  family f
JOIN
  rfamseq rs ON f.rfam_acc = rs.rfam_acc
GROUP BY
  f.family_accession,
  f.family_name
HAVING
  max_length > 1000000
ORDER BY
  max_length DESC
LIMIT 15 OFFSET 120;


