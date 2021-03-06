# Usage
# python verify.py input.csv

import lob
import csv
import sys

lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

skipFirstLine  = True

# Column indices in CSV
address1    = 0;
address2    = 1;
city        = 2;
state       = 3;
postcode    = 4;
country     = 'US'

try:
  sys.argv[1]
except IndexError:
  print "Please provide an input CSV file as an argument."
  sys.exit()

# Open input files
inputFile = open(sys.argv[1], 'rU')
csvInput = csv.reader(inputFile)

# Create output files
errors = open('errors.csv', 'w')
verified = open('verified.csv', 'w')

# Loop through input CSV rows
for idx, row in enumerate(csvInput):
  if skipFirstLine and idx == 0:
    continue

  # Sanity check
  sys.stdout.write('.')
  sys.stdout.flush()

  try:
    verifiedAddress = lob.Verification.create(
      address_line1 = row[address1],
      address_line2 = row[address2],
      address_city = row[city],
      address_state = row[state],
      address_zip = row[postcode],
      address_country = country
    )
  except Exception, e:
    outputRow = ",".join(row) + "," + str(e)+ "\n"
    errors.write(outputRow)
  else:
    outputRow = verifiedAddress.address.address_line1 + ","
    outputRow += verifiedAddress.address.address_line2 + ","
    outputRow += verifiedAddress.address.address_city + ","
    outputRow += verifiedAddress.address.address_state + ","
    outputRow += verifiedAddress.address.address_zip + "\n"
    verified.write(outputRow)

errors.close()
verified.close()
print "\n"
