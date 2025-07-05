# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start:end:step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # Indexes the first digit of the string
print(credit_number[:4]) # Indexes the first to the fourth digit (The starting digit is inclusive and could be left blank while the end digit is exclusive)
print(credit_number[5:9]) #Indexes the fifth to the 9th digit.
print(credit_number[5:]) # Indexes the fifth to the last digit (Python will assume the end of the string if the second space is left empty)
print(credit_number[-1]) # Indexes the last digit in the string (COntinuing further negative values will work backwards withint the string EX. -2 will print "5")
print(credit_number[::3]) # Python assumes from start to finish while including a step of 2. This will print every second digit.

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}") # Prints the last four digits of the credit_number

credit_number = credit_number[::-1]
print(credit_number)