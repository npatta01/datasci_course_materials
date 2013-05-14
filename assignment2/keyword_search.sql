SELECT A.docid ,B.docid , SUM(A.count*B.count) as similarity
from new_frequencys AS A  
JOIN  new_frequencys AS B
  ON A.term =B.term AND B.docid <A.docid
where A.docid ="q" 
GROUP BY A.docid,B.docid
ORDER BY Similarity DESC