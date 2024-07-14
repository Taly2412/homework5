immutable_var = 1, 2, "Taly", True
print(immutable_var)
#immutable_var[0] = 5   #кортеж - это неизменяемый тип данных, поэтому при попытке выполнить программа выдает ошибку
#print(immutable_var)
mutable_list = ["июнь", "июль", "август"]
mutable_list[2] = "сентябрь"
print(mutable_list)