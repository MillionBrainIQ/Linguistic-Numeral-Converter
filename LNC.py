polyglot = [
  ["Zero", "One", "Two", "Three", "Four", "Five" , "Six", 
   "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
   "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
   "Seventeen", "Eighteen", "Nineteen", "Twenty"],
  ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", 
   "Siete", "Ocho", "Nueve", "Diez", "Once", "Doce", 
   "Trece", "Catorce", "Quince", "Dieciséis", "Diecisiete", 
   "Dieciocho", "Diecinueve", "Veinte"],
  ["Zero", "Une", "Deux", "Trois", "Quatre", "Cinq", "Six", 
   "Sept", "Huit", "Neuf", "Dix", "Onze", "Douze", "Treize", 
   "Quatorze", "Quinze", "Seize", "Dix-sept", "Dix-huit", 
   "Dix-neuf", "Vingt"],
  ["शून्य", "एक", "दो", "तीन", "चार", "पाँच", "छह", "सात", "आठ", 
   "नौ", "दस", "ग्यारह", "बारह", "तेरह", "चौदह", "पंद्रह", "सोलह", 
   "सत्रह", "अठारह", "उन्नीस", "बीस"], 
  ["영", "하나", "둘", "셋", "넷", "다섯", "여섯", "일곺", "여덟", 
   "아홒", "열", "열하나", "열둘", "열셋", "열넷", "열다섯", 
   "열여섯", "열일곺", "열여덟", "열아홒", "스물"],
  ["Null", "Eins", "Zwei", "Drei", "Vier", "Fünf", "Sechs", 
   "Sieben","Acht", "Neun", "Zehn", "Elf", "Zwölf", "Dreizehn", 
   "Vierzehn", "Fünfzehn", "Sechzen", "Siebzehn", 
   "Achtzehn", "Neunzehn", "Zwanzig"],
  ["Nolla", "Yksi", "Kaksi", "Kolme", "Neljä", "Viisi", 
   "Kuusi", "Seitsemän",  "Kahdeksan", "Yhdeksän", 
   "Kymmenen", "Yksitoista", "Yksitoista", "Kolmetoista", 
   "Nelijätoista", "Viisitoista", "Kuusitoista", 
   "Seitsemäntoista", "Kahdeksantoista", "Yhdeksäntoista", 
   "Kaksikymmentä"],
  ["Nulla", "I", "II", "III", "IV", "V", "VI", "VII", 
   "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", 
   "XVI", "XVII", "XVIII", "XIX", "XX"],
  ["Zero", "Uno", "Due", "Tre", "Quattro", "Cinque", "Sei", 
   "Sette", "Otte", "Nove", "Dieci", "Undici", "Dodici", 
   "Tredici", "Quattordici", "Quindici", "Sedici", 
   "Diciassette", "Diciotto", "Diciannove", "Venti"],
  ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", 
   "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", 
   "Catorze", "Quinze", "Dezesseis", "Dezessete", 
   "Dezoito", "Dezenove", "Vinte"],
  ["Μιδέν", "Ενας", "Δίο", "Τρία", "Τέσσερα", "Πέντε", 
   "Eξι", "Επτά", "Οκτώ", "Εννέα", "Δέκα", "Εντεκα", 
   "Δώδεκα", "Δεκατρία", "Δεκατέσσερα", "Δεκαπέντε", 
   "Δεκαέξι", "Δεκαεπτά", "Δεκαοκτώ", "Δεκαεννέα", "Είκοσι"],
  ["Нуль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", 
   "Семь", "Восемь", "Девять", "Десять", "Одиннадцать", 
   "Двенадцать", "Тринадцать", "Четырнадцать", 
   "Пятнадцать", "Шестнадцать", "Семнадцать", 
   "Восемнадцать", "Девятнадцать", "Двадцать"]]

number_input = 0 
language_reattempt = 0
number_reattempt = 0

print("Welcome to the Linguistic Numeral Converter.")
print()
print()

number_input = int(input("Input a number from 0 to 20: "))
print()

while number_input > 20 or number_input < 0:
  print("Invalid number. Please try again.")
  print()
  number_input = int(input("Input a number from 0 to 20: "))

print("0. English")
print("1. Spanish")
print("2. French")
print("3. Hindi")
print("4. Korean")
print("5. German")
print("6. Finnish")
print("7. Roman Numerals")
print("8. Italian")
print("9. Portugese")
print("10. Greek")
print("11. Russian")
print()
print()

language_input = int(input("Select a language by typing in its corresponding number: "))
while language_input > 11 or language_input < 0:
  print("Invalid number. Please try again.")
  language_input = int(input("Select a language by typing in its corresponding number: "))

print(polyglot[language_input][number_input])