def frequency(s):
             # s = input("Enter a string:")
              words = s.split()
              d = {}

              for i in words:
                  if i in d:
                      d[i] += 1
                  else:
                      d[i] = 1
              return dict(sorted(d.items()))
s = "abc bcd def abc abc def"
ans = frequency(s)
print(ans)
                          
            
              
