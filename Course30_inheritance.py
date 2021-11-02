from sef import Chef
from sef_chinese import ChineseChef

# genel bir şef yarattık
myChef = Chef()
myChef.make_chicken()

# artık yeni şefimiz standart şefin yemeklerinide yapıyor
myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
# overwrite yapmassak aynı yemeği yapar 
myChineseChef.make_special_dish()