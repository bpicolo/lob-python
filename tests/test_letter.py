import unittest
import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

class LetterFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
        self.addr = lob.Address.list(count=1).data[0]

    def test_list_letters(self):
        letters = lob.Letter.list()
        self.assertTrue(isinstance(letters.data[0], lob.Letter))
        self.assertEqual(letters.object, 'list')

    def test_retrieve_letter(self):
        letter = lob.Letter.retrieve(id=lob.Letter.list().data[0].id)
        self.assertTrue(isinstance(letter, lob.Letter))

    def test_create_letter(self):
        letter = lob.Letter.create(
            from_address = {
                'name': 'Antoinette Reynolds',
                'address_line1': '1859 Kinney St',
                'address_city': 'Agawam',
                'address_zip': '01001',
                'address_state': 'MA'
            },
            to_address = self.addr.id,
            file = '<h1>{{name}}</h1>',
            data = {
                'name': 'Peter'
            },
            color = True
        )
        self.assertEqual(letter.to_address.id, self.addr.id)
        self.assertTrue(isinstance(letter, lob.Letter))

