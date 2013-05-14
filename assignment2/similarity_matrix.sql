%Final for two douments
SELECT A.docid ,B.docid , SUM(A.count*B.count) as similarity
from Frequency AS A  JOIN  Frequency AS B
ON A.term =B.term
where A.docid IN ("10080_txt_crude") AND B.docid IN ("17035_txt_earn")
GROUP BY A.docid,B.docid



%for each document pair
SELECT A.docid ,B.docid ,A.term,b.term,A.count*B.count as count
from Frequency AS A  JOIN  Frequency AS B
ON A.term =B.term
where A.docid IN ("10080_txt_crude") AND B.docid IN ("17035_txt_earn")


