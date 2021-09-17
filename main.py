import os

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def input_float(msg):
  while True:
    val = input(msg)
    fval = 0.0
    try:
      fval = float(val)
      return fval
    except:
      print("Invalid input")

def input_int(msg):
  while True:
    val = input(msg)
    ival = 0.0
    try:
      ival = int(val)
      return ival
    except:
      print("Invalid input")

def print_header(msg):
  print()
  print("---------------------------------")
  print(msg)
  print("---------------------------------")
  print()

def print_table(rows):
  max_sizes = []
 
  for columns in rows:
    column_n = 0
    for column in columns:
      if len(max_sizes) > column_n:
        if max_sizes[column_n] < len(str(column)):
          max_sizes[column_n] = len(str(column))
        else:
          pass
      else:
        max_sizes.append(len(str(column)))
      column_n += 1
  
  for columns in rows:
    c = ""
    rt = ""
    column_n = 0
    for column in columns:
      col_c = ""
      for i in range(max_sizes[column_n]):
        col_c += " "
      
      col_c = str(column) + col_c[len(str(column)):]
      #c += " | " + col_c + " |"
      c += col_c + "  "
      rt += "   "
      for i in range(len(col_c)):
        rt += "-"
      rt += "  "
    print(c)
    #print(rt)

def ask_question(msg, default):
  msg += " (Yes("
  if default == "y":
    msg += "Y"
  else:
    msg += "y"
  msg += ") / No("
  if default == "n":
    msg += "N"
  else:
    msg += "n"
  msg += ")): "
  req = input(msg)
  if default == "n" and (req == "Y" or req == "y"):
    return True
  elif default == "n":
    return False
  elif default == "y" and (req == "N" or req == "n"):
    return False
  elif default == "y":
    return True
  else:
    return False
    
def ask_goback_question():
  return ask_question("Do you want to go back to main menu", "n")

# [[code, name, discount, quantity, price]]
products = []

prod_codek = 0
prod_namek = 1
prod_discountk = 2
prod_quantityk = 3
prod_pricek = 4

def add_product(code, name, discount, quantity, price):
  products.append([])
  products[len(products) - 1].append(code)
  products[len(products) - 1].append(name)
  products[len(products) - 1].append(discount)
  products[len(products) - 1].append(quantity)
  products[len(products) - 1].append(price)

def handle_add_action():
  print_header("ADD PRODUCT")

  prod_code = input("Product Code: ")
  prod_name = input("Product Name: ")
  prod_discount = input_float("Product Discount: ")
  prod_quantity = input_int("Product Quantity: ")
  prod_price = input_float("Product Price: ")
  add_product(prod_code, prod_name, prod_discount, prod_quantity, prod_price)

def ask_update_question(field_name):
  return ask_question("Do you want to update the " + field_name, "n")

def handle_update_action():
  print_header("UPDATE PRODUCT")
  
  prod_i = input_int("Enter the product index to update: ") - 1
  while len(products) <= prod_i:
    print("Product index does not exists!")
    if ask_goback_question():
      return
    prod_i = input_int("Enter the product index to update: ") - 1
  
  if ask_update_question("Product Code"):
    prod_code = input("New Product Code: ")
    products[prod_i][prod_codek] = prod_code
    
  if ask_update_question("Product Name"):
    prod_name = input("New Product Name: ")
    products[prod_i][prod_namek] = prod_name
    
  if ask_update_question("Product Discount"):
    prod_discount = input_float("New Product Discount: ")
    products[prod_i][prod_discountk] = prod_discount
    
  if ask_update_question("Product Quantity"):
    prod_quantity = input_int("New Product Quantity: ")
    products[prod_i][prod_quantityk] = prod_quantity
    
  if ask_update_question("Product Price"):
    prod_price = input_float("New Product Price: ")
    products[prod_i][prod_pricek] = prod_price

def handle_delete_action():
  print_header("DELETE PRODUCT")
  
  prod_i = input_int("Enter the product index to delete: ") - 1
  while len(products) <= prod_i:
    if ask_goback_question():
      return
    print("Product index does not exists!")
    prod_i = input_int("Enter the product index to delete: ") - 1
  
  products.pop(prod_i)

def print_products():
  xprods = products[:]
  i = 1
  for prod in xprods:
    prod = prod[:]
    prod.insert(0, i)
    prod[prod_pricek+1] = str(prod[prod_pricek+1]) + " LKR"
    prod[prod_discountk+1] = str(prod[prod_discountk+1]) + "%"
    xprods[i-1] = prod
    i += 1
  print("Current products --------------------------------------------------------")
  print()
  print_table(list(xprods))
  print()
  print("-------------------------------------------------------------------------")
  print()

def handle_bill_print():
  print_header("BILL")
  bill_products = products[:]
  bill_products.insert(0, ["#", "name", "%", "qty", "price"])
  bill_products.insert(1, ["", "", "", "", ""])
  gross_total = sum([float(i[prod_pricek]) * int(i[prod_quantityk]) for i in products])
  product_discounted = sum([float(i[prod_pricek]) * int(i[prod_quantityk]) / 100 * float(i[prod_discountk]) for i in products])
  bill_discount = 15
  bill_discounted = 0
  if gross_total > 15000 and gross_total < 21000:
    bill_discount = input_float("Enter discount percentage: ")
    bill_discounted = gross_total / 100 * bill_discount
  elif gross_total > 55000:
    bill_discounted = gross_total / 100 * 20
  net_total = gross_total - product_discounted - bill_discounted
 
  print()
  print("Welcome to fashion house")
  print("-----------------------------------------")
  print_table(bill_products)
  print("-----------------------------------------")
  metrices = [["Gross total", str(gross_total) + " LKR"],
              ["Discount on products", str(product_discounted) + " LKR"],
              ["Discount on bill", str(bill_discounted) + " LKR"],
              ["Net total", str(net_total) + " LKR"]]
  print_table(metrices)
  print("-----------------------------------------")
  print("               Thank you                 ")
  

def ask_for_action():
  actions = [[1, "Add Product"], [2, "Update Product"], [3, "Delete Product"], [4, "Print Bill"]]
  print_table(actions)
  print()
  return input_int("Select action: ")

username = input("Username: ")
password = input("Password: ")

while username != "admin" or password != "123":
  print("Invalid login!")
  username = input("Username: ")
  password = input("Password: ")

clear_console()

# 1 -> Add item
# 2 -> Update item
# 3 -> Delete item
# 4 -> Print bill

action = 1
#handle_add_action()
while True:
  clear_console()
  print_header("MAIN MENU")
  
  print_products()
  
  action = ask_for_action()
  
  if action == 1:
    clear_console()
    if ask_goback_question():
      continue
    clear_console()
    handle_add_action()
  elif action == 2:
    clear_console()
    if ask_goback_question():
      continue
    clear_console()
    handle_update_action()
  elif action == 3:
    clear_console()
    if ask_goback_question():
      continue
    clear_console()
    handle_delete_action()
  elif action == 4:
    clear_console()
    handle_bill_print()
    break
  else:
    print("Invalid menu item") 
  
