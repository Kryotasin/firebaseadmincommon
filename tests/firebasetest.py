import unittest
from connecttofirebase import ConnectToFirebase

class TestFirebaseConnection(unittest.TestCase):
    def setUp(self):
        self.fbconn = ConnectToFirebase('')

    def test_fbconn(self):
        self.assertTrue(self.fbconn.checkStatus)

if __name__ == '__main__':
    unittest.main()