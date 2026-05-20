import math
tup1= (4,9,2026)
tup2= (3,5,2026)
yr_diff= (tup1[2] - tup2[2])*365
mnth_diff= (tup1[1] - tup2[1])*30
date_diff= (tup1[0] - tup2[0])
diff = yr_diff + mnth_diff + date_diff
print("Difference between dates is ", diff, " days")
