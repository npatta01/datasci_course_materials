Select docid,sum(count)
from frequency
Group by docid
Having sum(count)>300