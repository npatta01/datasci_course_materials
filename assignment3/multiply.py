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
    ind_0=record[1]
    ind_1=record[2]
    value=record[3]
    t=record[0];

    B_size=20
    if t=="a":
        j=ind_1
    else:
        j=ind_0

    for k in xrange(0,B_size):
        
        if t =="a":
            mr.emit_intermediate((ind_0,k), (t,j,value))
        else:
            mr.emit_intermediate((k,ind_1), (t,j,value))

def reducer(key, list_of_values):
    A_size=20
    # key: word
    # value: list of occurrence counts
    A_tmp=[0]*A_size;
    B_tmp=[0]*A_size;
    for i in xrange(0,len(list_of_values)):
        current=list_of_values[i]
        t=current[0]
        j=current[1]
        value=current[2]
        if(t=="a"):
            A_tmp[j]=value
        else:
            B_tmp[j]=value
    
    sum=0
    for i in xrange(0,len(A_tmp)):
        sum=sum+ A_tmp[i] *B_tmp[i];
    if sum!=0 :
        mr.emit((key[0],key[1],sum))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
