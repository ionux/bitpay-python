from bitpay import key_utils as utils
import re
import unittest

class TestSequenceFunctions(unittest.TestCase):

  def test_generate_pem(self):
    pem = utils.generate_pem()
    match = re.match(r"-----BEGIN EC PRIVATE KEY-----", pem)
    self.assertIsNotNone(match)

  def test_sin_from_pem(self):
    pem = '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEICg7E4NN53YkaWuAwpoqjfAofjzKI7Jq1f532dX+0O6QoAcGBSuBBAAK\noUQDQgAEjZcNa6Kdz6GQwXcUD9iJ+t1tJZCx7hpqBuJV2/IrQBfue8jh8H7Q/4vX\nfAArmNMaGotTpjdnymWlMfszzXJhlw==\n-----END EC PRIVATE KEY-----\n'
    assert utils.get_sin_from_pem(pem) == 'TeyN4LPrXiG5t2yuSamKqP3ynVk3F52iHrX'