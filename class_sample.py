from datetime import datetime

class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    result = "{name} menu available from {start} to {end}".format(name=self.name,start=self.start_time,end=self.end_time)
    return result

  def calculate_bill(self,purchased_items):
    total_cost = 0
    for item in purchased_items:
      total_cost += self.items[item]
    return total_cost   

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    result = "This Franchise is located at {}".format(self.address)
    return result

  def available_menu(self,time):
    in_time = datetime.strptime(time, "%I:%M %p")
    out_time = datetime.strftime(in_time, "%H:%M")
    true_time = int(out_time[:2])
    if true_time >= 10 and true_time < 11:
      return self.menus[4]
    elif true_time >= 11 and true_time < 15:
      return self.menus[0],self.menus[3],self.menus[4]
    elif true_time >= 15 and true_time < 16:
      return self.menus[0],self.menus[1],self.menus[3],self.menus[4]
    elif true_time >= 16 and true_time < 17:
      return self.menus[2],self.menus[3],self.menus[4]
    elif true_time >= 17 and true_time < 18:
      return self.menus[1],self.menus[2],self.menus[3],self.menus[4]
    elif true_time >= 18 and true_time < 21:
      return self.menus[2],self.menus[3],self.menus[4]
    elif true_time >= 21 and true_time < 23:
      return self.menus[2]

class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
  

item_1 = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

item_2 = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

item_3 = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

item_4 = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

item_5 = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

brunch = Menu("Brunch",item_1,"11:00 am","4:00 pm")
early_bird = Menu("Early Bird",item_2,"3:00 pm","6:00 pm")
dinner = Menu("Dinner", item_3,"5:00 pm","11:00 pm")
kids = Menu("Kids",item_4,"11:00 am","9:00 pm")
arepas_menu = Menu("Take a Arepa", item_5,"10am","8pm")

#orders = ["salumeria plate","mushroom ravioli (vegan)"]
#print(brunch.calculate_bill(orders))
#print(early_bird.calculate_bill(orders))
menus = [brunch, early_bird,dinner,kids,arepas_menu]
flagship_store = Franchise("1232 West End Road",menus)
new_installment = Franchise("12 East Mulberry Street",menus)
arepas_place = Franchise("189 Fitzgerald Avenu",menus)
#print(flagship_store)
#print(flagship_store.available_menu("9:00 pm"))
franchises = [flagship_store,new_installment,arepas_place]
business = Business("Basta Fazoolin with my Heart",franchises)
business_2 = Business("Take a Arepa",franchises)

print(arepas_place.available_menu("8:00 pm"))
