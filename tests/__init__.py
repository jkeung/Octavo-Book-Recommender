import unittest

class InitializationTests(unittest.TestCase):

	def test_sanity(self):
		"""
		Assert the world is sane and 2+2=4
		"""
		self.assertEqual(2+2, 4)

	def test_import(self):
		"""
		Make sure we can import octavo.
		"""
		try:
			import octavo
		except ImportError:
			self.fail("could not import octavo")


