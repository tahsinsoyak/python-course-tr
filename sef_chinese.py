from sef import Chef
# sef klasını import ettik kalıtım-miras için


# kalıtım-miras için parantez içine yazdık
class ChineseChef(Chef):
    
    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_special_dish(self):
        print("The chef makes orange chicken")