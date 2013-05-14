SELECT a.row_num, b.col_num, SUM(a.value * b.value)
  FROM a, b
 WHERE a.col_num = b.row_num
 GROUP BY a.row_num, b.col_num;
 
 
 A=[[0 0 0 55 78];[19 0 21 3 81];[0 48 50 1 0];[0 0 33 0 67];[95 0 0 0 31]];
 B=[[0 73 0 0 42];[0 0 82 0 0];[83 13 0 57 0];[48 85 18 24 0];[98 7 0 0 3]];
 C=A*B;