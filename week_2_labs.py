#User Inputs type of operation they want to do

while True:
  print("Select operation:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exponentiation")

  user_input = input('Please enter the type of operation (1,2,3,4,5,): ')

  #Make sure user input is a valid operation

  if not user_input.isdigit():
        print("Invalid input. Please enter a valid operation number.")
        continue

  user_input = int(user_input)

  if user_input not in (1, 2, 3, 4, 5):
        print("Invalid input. Please enter a valid operation number.")
        continue

  #User inputs number for the operation
  variable_1_input = input("Enter the first number: ")
  variable_2_input = input("Enter the second number: ")

  try:
   variable_1 = float(variable_1_input)
   variable_2 = float(variable_2_input)
  except ValueError:
        print("Invalid input. Please enter valid numeric values for variables.")
        continue

  #Calculation Process
  if user_input == 1:
        result = variable_1 + variable_2
  elif user_input == 2:
        result = variable_1 - variable_2
  elif user_input == 3:
        result = variable_1 * variable_2
  elif user_input == 4:
        if variable_2 == 0:
            print("Error: Division by zero")
            continue
        result = variable_1 / variable_2
  elif user_input == 5:
        result = variable_1 ** variable_2

  #Print Results
  print(f"Result: {result}")

  break

