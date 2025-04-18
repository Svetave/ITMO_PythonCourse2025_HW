# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
age = int(age)
print (f"1. The type of the variable age is {type(age)}. The variable foo contains characters, so it can not be converted to int.")

# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)
print (f"2. The type of the variable age is {type(age)}.")

# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
print (f"3. The type of the variable flag is {type(flag)}.")

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one, str_two = bool(str_one), bool(str_two)
print (f"4. The type of the variable str_one is {type(str_one)}. The type of the variable str_two is {type(str_two)}")

# Преобразуйте значение 0 и 1 в Boolean
zero, one = bool(0), bool(1)
print (f"5. The type of the variable zero is {type(zero)}. The type of the variable one is {type(one)}")
# Преобразуйте False в строку
false_val = str(False)
print (f"6. The type of the variable false_val is {type(false_val)}.")