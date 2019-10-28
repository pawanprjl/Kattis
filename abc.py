num = list(map(int, input().split()))
pat = input()

a, b, c = sorted(num)
if(pat[0]=='A' and pat[1] == 'B' and pat[2] == 'C'):
    print(a,b,c)
elif (pat[0]=='A' and pat[1] == 'C' and pat[2] == 'B'):
    print(a,c,b)
elif(pat[0]=='B' and pat[1] == 'A' and pat[2] == 'C'):
    print(b,a,c)
elif(pat[0]=='B' and pat[1] == 'C' and pat[2] == 'A'):
    print(b,c,a)
elif(pat[0]=='C' and pat[1] == 'A' and pat[2] == 'B'):
    print(c,a,b)
else:
    print(c,b,a)
