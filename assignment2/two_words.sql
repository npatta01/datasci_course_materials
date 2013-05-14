Select docid
From Frequency
Where term="transactions"
AND docid IN 
( Select docid From Frequency where term="world")
