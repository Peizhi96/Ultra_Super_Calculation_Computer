class UltraSuperCalculator:
  def __init__(self, name):
    self.name = name
    self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    self.numbers_index = 1
    self.history_index = 0
    self.temp_history_index = 0
    self.user_display = " "
    self.update_display(f"Welcome to {self.name}'s Calculator!")



  def update_display(self, to_update):
    self.user_display = to_update
    print(self.user_display)

  def store_value_to_register(self, value_to_store):
    if self.numbers_index > 21:
      self.numbers_index = 1
    self.number_registers[self.numbers_index] = int(value_to_store, 2)
    print(f'Value: {int(value_to_store,2)} stored in Register: {self.numbers_index}.')
    self.numbers_index += 1
  
  def load_value_from_register(self, register_address):
    index = int(self.register_address, 2)
    int_value = int(self.number_registers[index])
    return int_value

  def store_to_history_register(self, result_to_store):
    if self.history_index > 9:
      self.history_index = 0
    self.history_register[self.history_index] = bin(result_to_store)
    self.history_index += 1
    self.temp_history_index = self.history_index

  
  def add(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = num1 + num2
    return calculated_value

  def multiply(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = num1 * num2
    return calculated_value
  
  def subtract(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = num1 - num2
    return calculated_value
  
  def divide(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    calculated_value = 0
    if num2 != 0:
      calculated = int(num1 / num2)
    else:
      print(f'Division by 0 error: {num1}/{num2}.')
    return calculated_value
  

  def get_last_calculation(self):
    self.temp_history_index -= 1
    last_value = f"The last calculated value was: {int(self.history_registers[self.temp_history_index], 2)}"
    self.update_display(last_value)

  def binary_reader(self, instruction):
    if len(instruction) != 32:
      self.update_display("Invalid Instruction Length")
      return 
    opcode = instruction[0:6]
    source_one = instruction[6:11]
    source_two = instruction[11:16]
    store = instruction[16:26]
    function_code = instruction[26:]
    if opcode == '000001':
      self.store_value_to_register(store)
      return
    elif opcode == '100001':
      self.get_last_calculation()
      return
    elif opcode != '000000':
      self.update_display("Invalid OPCODE")
      return

    result = 0
    if (function_code == '100000'):
      result = self.add(self.number_registers[source_one], self.number_registers[source_two])
    elif (function_code == '100010'):
      result = self.subtract(self.number_registers[source_one], self.number_registers[source_two])
    elif (function_code == '011000'):
      result = self.multiply(self.number_registers[source_one], self.number_registers[source_two])
    elif (function_code == '011010'):
      result = self.divide(self.number_registers[source_one], self.number_registers[source_two])
    else:
      self.update_display("Invalid Function")
      return




your_calculator = UltraSuperCalculator('Tingwei')
your_calculator.binary_reader("00000100000000000000000101000000")
your_calculator.binary_reader("00000100000000000000001010000000")