coins = [1,2,5,10,20,50,100,200]
counts = [200,100,40,20,4,2,1]
unique_ways = 0
start=200
for i in range(start+1):
    left1 = start-i
    possible_twos = left1//2
    for j in range(possible_twos+1):
        left2 = left1 - j*2
        possible_fives = left2//5
        for k in range(possible_fives+1):
            left3 = left2 - k*5
            possible_tens = left3//10
            for l in range(possible_tens+1):
                left4 = left3 - l*10
                possible_twenties = left4//20
                for m in range(possible_twenties+1):
                    left5 = left4-m*20
                    possible_fifties = left5//50
                    for n in range(possible_fifties+1):
                        left6 = left5-n*50
                        possible_hundreds = left6//100
                        for g in range(possible_hundreds+1):
                            left7 = left6-g*100
                            possible_twohundreds = left7//200
                            for h in range(possible_twohundreds+1):
                                left8 = left7-200*h
                                if left8==0:
                                    # print(i,1,j,2,k,5,l,10,m,20,n,50,g,100,h,200)
                                    unique_ways+=1
print(unique_ways)



