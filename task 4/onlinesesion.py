

def basic_operations(a, b):
  results = {}

  try:
    a = float(a)
    b = float(b)
  except ValueError:
    print("Invalid input. Please enter valid numbers.")
    return None

  try:
    results["addition"] = a + b
    results["subtraction"] = a - b
    results["multiplication"] = a * b
    results["division"] = a / b
  except ZeroDivisionError:
    print("Division by zero is not allowed.")
    return None

  return results

def power_operation(base, power):
  try:
    base = float(base)
    power = float(power)
  except ValueError:
    print("Invalid input. Please enter valid numbers.")
    return None

  try:
    result = base ** power
  except OverflowError:
    print("Result is too large to be represented.")
    return None

  return result

def apply_operations(operation_list):
  results = list(map(lambda operation: operation[0](*operation[1:]), operation_list))
  return results


a = input("Enter your first number: ")
b = input("Enter your second number: ")
results = basic_operations(a, b)

if results:
  print(f"Addition: {results['addition']}")
  print(f"Subtraction: {results['subtraction']}")
  print(f"Multiplication: {results['multiplication']}")
  print(f"Division: {results['division']}")

power_base = input("Enter the base for the power operation: ")
power_exponent = input("Enter the exponent for the power operation: ")
power_result = power_operation(power_base, power_exponent)

if power_result is not None:
  print(f"The result of {power_base} to the power of {power_exponent} is {power_result}")

operations = [
  (basic_operations, 5, 2),
  (power_operation, 3, 4),
  (sum, [1, 2, 3, 4, 5]),
]

results = apply_operations(operations)
print(f"Results of applying operations: {results}")
