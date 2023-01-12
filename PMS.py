# Pharmacy Management System
import sys
# User Sign Up
def sign_up():
  global stored_username
  global stored_password
  stored_username = input("Enter a username: ")
  stored_password = input("Enter a password: ")
  print("Sign up successful! You can now log in using these credentials.")

# User Log In
def log_in():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  # Check if username and password are correct
  if username == stored_username and password == stored_password:
    print("Log in successful! Welcome to the pharmacy management system.")
  else:
    print("Error: Incorrect username or password. Please try again.")

# Admin Dashboard
def admin_dashboard():
  # Linear Search
  def linear_search(medicine_list, target):
    for i in range(len(medicine_list)):
      if medicine_list[i] == target:
        return i
    return -1

  # Bubble Sort
  def bubble_sort(medicine_list):
    for i in range(len(medicine_list) - 1):
      for j in range(len(medicine_list) - 1 - i):
        if medicine_list[j] > medicine_list[j + 1]:
          medicine_list[j], medicine_list[j + 1] = medicine_list[j + 1], medicine_list[j]
    return medicine_list

  # Enqueue
  def enqueue(medicine_list, medicine):
    medicine_list.append(medicine)
    return medicine_list

  # Main function
  def main():
    # Linear search example
    medicine_list = ["Aspirin", "Ibuprofen", "Acetaminophen", "Naproxen"]
    target = "Ibuprofen"
    result = linear_search(medicine_list, target)
    if result == -1:
      print("Medicine not found.")
    else:
      print("Medicine found at index", result)

    # Bubble sort example
    medicine_list = ["Aspirin", "Ibuprofen", "Acetaminophen", "Naproxen"]
    result = bubble_sort(medicine_list)
    print("Sorted medicine list:", result)

    # Enqueue example
    medicine_list = ["Aspirin", "Ibuprofen", "Acetaminophen"]
    medicine = "Naproxen"
    result = enqueue(medicine_list, medicine)
    print("Updated medicine list:", result)

  main()

# Medicine List
medicine_list = []

# Stack and Queue
medicine_stack = []
medicine_queue = []

# Add Medicine
def add_medicine():
  global medicine_count
  name = input("Enter medicine name: ")
  price = int(input("Enter medicine price: "))
  medicine = {"name": name, "price": price}
  medicine_stack.append(medicine) # Add medicine to stack
  medicine_queue.append(medicine) # Add medicine to queue


# View Medicine (Stack)
def view_medicine_stack():
  if len(medicine_stack) == 0:
    print("No medicines found.")
  else:
    for i in range(len(medicine_stack)-1, -1, -1):
      print(medicine_stack[i])

# View Medicine (Queue)
def view_medicine_queue():
  if len(medicine_queue) == 0:
    print("No medicines found.")
  else:
    for medicine in medicine_queue:
      print(medicine)


# Edit Medicine
def edit_medicine():
  medicine_name = input("Enter the name of the medicine: ")
  found = False
  for medicine in medicine_list:
    if medicine["name"] == medicine_name:
      found = True
      new_name = input("Enter the new name of the medicine: ")
      new_price = input("Enter the new price of the medicine: ")
      medicine["name"] = new_name
      medicine["price"] = new_price
      print("Medicine edited successfully!")
  if not found:
    print("Error: Medicine not found.")

# Delete Medicine
def delete_medicine():
  medicine_name = input("Enter the name of the medicine: ")
  found = False
  for i in range(len(medicine_list)):
    if medicine_list[i]["name"] == medicine_name:
      found = True
      del medicine_list[i]
      print("Medicine deleted successfully!")
      break
  if not found:
    print("Error: Medicine not found.")


# Confirm Medicine
def confirm_medicine():
  medicine_name = input("Enter the name of the medicine: ")
  found = False
  for medicine in medicine_list:
    if medicine["name"] == medicine_name:
      found = True
      print("Medicine found:")
      print("Name:", medicine["name"])
      print("Price:", medicine["price"])
  if not found:
    print("Error: Medicine not found.")

# Search Medicine
def search_medicine():
  medicine_name = input("Enter the name of the medicine: ")
  found = False
  for medicine in medicine_list:
    if medicine["name"] == medicine_name:
      found = True
      print("Medicine found:")
      print("Name:", medicine["name"])
      print("Price:", medicine["price"])
  if not found:
    print("Error: Medicine not found.")

# Sort Medicine
def sort_medicine():
  sorted_medicine_list = sorted(medicine_list, key=lambda k: k["name"])
  for medicine in sorted_medicine_list:
    print("Name:", medicine["name"])
    print("Price:", medicine["price"])

# Traverse Medicine
def traverse_medicine():
  for medicine in medicine_list:
    print("Name:", medicine["name"])
    print("Price:", medicine["price"])

# Generate Bill
def generate_bill():
  total_cost = 0
  for medicine in medicine_list:
    total_cost += (medicine["price"])
  print("Total cost:", total_cost)

# Exit
def exit():
  print("Thank you for using the pharmacy management system. Good bye!")
  sys.exit()

# Main Function
def main():
  while True:
    print("Welcome to the Pharmacy Management System")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Admin Dashboard")
    print("4. Add Medicine")
    print("5. Edit Medicine")
    print("6. Delete Medicine")
    print("7. View Medicine (Stack)")
    print("8. View Medicine (Queue)")
    print("9. Confirm Medicine")
    print("10. Search Medicine")
    print("11. Sort Medicine")
    print("12. Traverse Medicine")
    print("13. Generate Bill")
    print("14. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      sign_up()
    elif choice == "2":
      log_in()
    elif choice == "3":
      admin_dashboard()
    elif choice == "4":
      add_medicine()
    elif choice == "5":
      edit_medicine()
    elif choice == "6":
      delete_medicine()
    elif choice == "7":
      view_medicine_stack()
    elif choice == "8":
      view_medicine_queue()
    elif choice == "9":
      confirm_medicine()
    elif choice == "10":
      search_medicine()
    elif choice == "11":
      sort_medicine()
    elif choice == "12":
      traverse_medicine()
    elif choice == "13":
      generate_bill()
    elif choice == "14":
      exit()
    else:
      print("Error: Invalid choice. Please try again.")

main()