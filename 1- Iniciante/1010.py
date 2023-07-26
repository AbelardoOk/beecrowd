l1 = input().split(" ")
l2 = input().split(" ")
cd1, qtd1, vl1 = l1
cd2, qtd2, vl2 = l2

total = (int(qtd1) * float(vl1)) + (int(qtd2) * float(vl2))
print("VALOR A PAGAR: R$ {:.2f}".format(total))