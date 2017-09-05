import unittest
from unittest import mock
from nimoy.runner.spec_loader import SpecLoader
from nimoy.ast_tools.ast_metadata import SpecMetadata


class TestSpecLoader(unittest.TestCase):
    def test_load(self):
        ast_chain = mock.Mock()

        metadata = SpecMetadata('Jimbob')
        ast_chain.apply.return_value = [metadata]

        returned_spec_metadata = SpecLoader(ast_chain).load([('/path/to/spec.py', 'class Jimbob:\n    pass')])

        self.assertEqual(returned_spec_metadata[0].name, 'Jimbob')
        self.assertTrue(returned_spec_metadata[0].owning_module)

        ast_chain.apply.assert_called_once()
