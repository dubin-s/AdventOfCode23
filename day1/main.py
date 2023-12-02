import os

def main():
  print(read_file(os.getcwd() + '/input.txt'))


def read_file(path):
  calibration_value_sum = 0
  f = open(path, 'r')
  for line in f:
    current_string = line.strip()
    for letter in current_string:
      if letter.isdigit():
        first_digit = letter
        break
    for letter in ''.join(reversed(current_string)):
      if letter.isdigit():
        second_digit = letter
        break
    calibration_value = int(first_digit + second_digit)
    calibration_value_sum += calibration_value
  return calibration_value_sum

if __name__ == '__main__':
  main()
  
  
# Part 1
# need to read the string from the beginning to get the first number
# then need to reverse the string or read it from the back to get the second number
# then I need to concat those two strings and then turn it to an int
# then I need to add that to a running sum and return the running sum