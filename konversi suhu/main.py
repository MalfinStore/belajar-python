#Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.

def kelvin_to_celcius(kelvin): # konversi suhu kelvin  ke celcius
    celcius = kelvin - 273.15   
    return celcius

result_celcius = kelvin_to_celcius(300)
print("suhu ruangan ini adalah", result_celcius, "derajat celcius")

def celcius_to_kelvin(celcius): # konversi suhu celcius ke kelvin
    kelvin = celcius + 273.15
    return  kelvin

result_kelvin = celcius_to_kelvin(25)
print("suhu ruangan ini adalah", result_kelvin, "derajat kelvin")
# Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. 
# Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin.
#  Panggil function yang pertama jika diperlukan.

def celcius_to_fahrenheit(celcius): # konversi suhu celcius ke fahrenheit
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

result_celcius_to_fahrenheit = celcius_to_fahrenheit(28)
print("suhu ruangan ini adalah", result_celcius_to_fahrenheit, "derajat fahrenheit")

def kelvin_to_fahrenheit(kelvin): # konversi suhu kelvin ke fahrenheit
    fahrenheit = (kelvin * 9/5) -459.67
    return fahrenheit

result_kelvin_to_fahrenheit = kelvin_to_fahrenheit(300) 
print("suhu ruangan ini adalah", result_kelvin_to_fahrenheit, "derajat fahrenheit")

# Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit.
# Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin.

def fahrenheit_to_celcius(fahrenheit): # konversi suhu fahrenheit ke celcius
    celcius = (fahrenheit -32) * 5/9
    return  celcius

result_farenheit_to_celcius = fahrenheit_to_celcius(80) # konversi suhu fahrenheit ke celcius
print("suhu ruangan ini adalah", result_farenheit_to_celcius, "derajat celcius")

def fahrenheit_to_kelvin(fahrenheit): # konversi suhu fahrenheit ke kelvin
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

result_fahrenheit_to_kelvin = fahrenheit_to_kelvin(85)
print( "suhu ruangan ini adalah", result_fahrenheit_to_kelvin , "derajat kelvin")

