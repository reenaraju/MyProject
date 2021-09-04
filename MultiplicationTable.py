import pyttsx3

n = input("Enter the number:")
dic = {
    "1" : "ones",
    "2" : "twos",
    "3" : "threes",
    "4" : "fours",
    "5" : "fives",
    "6" : "six",
    "7" : "sevens",
    "8" : "eights",
    "9" : "nines",
    "10" : "tens",
}
txt = ""
for i in range(1,11):
    mul = i*int(n)
    txt+= n + " " + dic[str(i)] + " are " + str(mul) + "\n"
#print(txt)

engine = pyttsx3.init()
txt1="Multiplication table of " + str(n)
engine.say(txt1)
engine.say(txt)
engine.runAndWait()