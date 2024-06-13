"""
1. BMI-Rechner -  
es ist eine Funktion zur Berechnung des BMI zu erstellen. Der BMI errechnet sich nach der 
Formel  
�
�𝑀𝐼 =𝐾ö𝑟𝑝𝑒𝑟𝑔𝑒𝑤𝑖𝑐ℎ𝑡 𝑖𝑛 𝑘𝑔 / (𝐾ö𝑟𝑝𝑒𝑟𝑔𝑟öß𝑒 𝑖𝑛 𝑚 ∗𝐾ö𝑟𝑝𝑒𝑟𝑔𝑟öß𝑒 𝑖𝑛 𝑚) 
Die Funktion ist mit verschiedenen Werten zu testen. 
2. Umfang und Fläche eines Rechtecks -  
zur Berechnung des Umfangs und der Fläche eines Rechtecks sind zwei Funktionen zu 
definieren. Die Funktionen sind mit verschiedenen Werten zu testen. 
"""

#1
def bmicalc(weight, height):
    bmi = weight / (height * height)
    return bmi


print(round(bmicalc(80, 1.76), 2))
print(round(bmicalc(65, 1.65), 2))
print(round(bmicalc(90, 2.08), 2))

#2
def rechteckfl(x, y):
    flaeche = x * y
    return flaeche

def rechteckumf(x, y):
    umfang = ((2 * x) + (2 * y))
    return umfang


seitea = 2.45
seiteb = 3.65
print(f"Fläche: {rechteckfl(seitea, seiteb)} cm² Umfang: {rechteckumf(seitea, seiteb)} cm")
seitea = 5
seiteb = 5
print(f"Fläche: {rechteckfl(seitea, seiteb)} cm² Umfang: {rechteckumf(seitea, seiteb)} cm")
seitea = 40
seiteb = 10.65
print(f"Fläche: {rechteckfl(seitea, seiteb)} cm² Umfang: {rechteckumf(seitea, seiteb)} cm")