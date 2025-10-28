t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if n%(x+1)==0:
        print("Gaurav wins")
    else:
        print("Anubhav wins")
