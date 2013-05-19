import MapReduce
import sys

"""
Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # id: join key
    # value: document contents
    id = record[1]
    mr.emit_intermediate(id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    if list_of_values.count<2:
        return
    orderlem= list_of_values[0];
    
    for i in range(1,len(list_of_values)):
        joined_result=orderlem
        joined_result.extend(list_of_values[i]);
        mr.emit((joined_result))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
