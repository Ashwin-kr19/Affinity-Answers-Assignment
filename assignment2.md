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
