import random
ilk_grup = ["Mr.","Kylian","ps5","Why","Eti","DA DA DA DA","Adolf","Q7","Skibidi","Arctic"]
ikinci_grup = ["Whopper", "Beast", "Offside","So","d","Cin","MAX","Error","Red","Kraga"]
son_grup = ["404","McDonalds","McCrappe","Werner","Serious","Trump","VERSTAPPEN","Stalin","Bottler","505"]
def name():
    ilk_eleman = ilk_grup[random.randint(0,9)]
    ikinci_eleman = ikinci_grup[random.randint(0,9)]
    son_eleman = son_grup[random.randint(0,9)]
    print(f"{ilk_eleman} {ikinci_eleman} {son_eleman}")
repeat = int(input("Kaç Tekrar İstersiniz? "))
for i in range(repeat):
    name()