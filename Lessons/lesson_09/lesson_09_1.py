# пример с походом - идем в поход,
# если сегодня выходной и хорошая погода
is_weekend = True
is_good_weather = True

going_haiking = is_weekend or is_good_weather

if going_haiking:
    print("*** Мы идем в поход")
else:
    print("*** Мы не идем в поход")

print("*** код после блока if-else")