from scipy.optimize import minimize


print("Informe a quantidade de vendas anteriores e seus respectivos desconto")
print(" ")


desconto1 = int(input("Informe o primeiro desconto  "))
publico1 = int(input("Informe a quantidade de vendas realizadas para este desconto  "))

desconto2 = int(input("Informe o segundo desconto  "))
publico2 = int(input("Informe a quantidade de vendas realizadas para este desconto  "))



M = ((desconto2 - desconto1)/(publico2 - publico1))


def R(x):
    return -((M*(publico2-x) + desconto2)*x)


maxpublico = minimize(R,1)

Dmaxreceita = desconto2 - M*(int(maxpublico.x)-publico2)



print(" ")
print("desconto sugerido:")
print(float(Dmaxreceita))
print(" ")
print("Quantidade de vendas esperada:")
print(int(maxpublico.x))
print(" ")
print("Receita esperada:")
print(int(Dmaxreceita*maxpublico.x))


