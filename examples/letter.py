import lob
lob.api_key = "test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc" # Replace this API key with your own.

# Creating an Address Object

example_address = lob.Address.create(
    name = 'Julia Sanchez',
    description = 'Julia - Home',
    metadata = {
        'department': 'marketing'
    },
    address_line1 = '104 Printing Boulevard',
    address_city = 'Boston',
    address_state = 'MA',
    address_country = 'US',
    address_zip = '12345'
)
print "\n"
print "Address Response"
print "\n"
print "======================================================="
print "\n"
print example_address
print "\n"
print "======================================================="
print "\n"

# Creating a Letter

example_letter = lob.Letter.create(
    description = 'Test Letter',
    metadata = {
        'campaign': 'enterprise offer'
    },
    to_address = {
        'name': 'Antoinette Reynolds',
        'address_line1': '1859 Kinney St',
        'address_city': 'Agawam',
        'address_zip': '01001',
        'address_state': 'MA',
        'metadata': {
            'customer_type': 'enterprise'
        }
    },
    from_address = example_address,
    file = """
      <html>
        <head>
          <style>
            @font-face {
              font-family: 'Loved by the King';
              src: url('https://s3-us-west-2.amazonaws.com/lob-assets/LovedbytheKing.ttf');
            }
          </style>
        </head>
        <body><h1>Special offer for {{company}}</h1></body>
      </html>""",
    data = {
        'company': 'ACME'
    },
    color = True
)

print "Letter Response"
print "\n"
print "======================================================="
print "\n"
print example_letter
print "\n"
print "======================================================="
print "\n"
