# "python" используя срезы - создать две отдельные переменные, первая будет хранить только первый символ,
# вторая переменная - остаток строки. После этого, следует перевести первую переменную в верхний регистр,
# а вторую - в нижний и склеить обратно, так, чтобы получилось "Python"


text = "python"
firstpart = text[0]
secondpart = text[1:]

firstpart = firstpart.upper()
result = firstpart + secondpart

print(result)