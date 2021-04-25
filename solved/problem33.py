product =1
for num in range(10,100):
    if num%10 ==0:
        continue
    for den in range(10,100):
        if den % 10 == 0:
            continue
        if num/den < 1.0:
            real_result = num/den
            if str(num)[1] == str(den)[0]:
                fake_num = int(str(num)[0])
                fake_den = int(str(den)[1])
                fake_result = fake_num/fake_den
                if fake_result==real_result:
                    product = product*real_result


print(1/product)
