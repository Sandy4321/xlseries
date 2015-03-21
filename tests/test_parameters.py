#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import nose
import json
from xlseries.parameters import Parameters

"""
test_parameters
----------------------------------

This module tests the parameters object.
"""


class ParametersTest(unittest.TestCase):

    def setUp(self):
        self.params = Parameters("./parameters/test_params.json")
        self.params_exp = Parameters("./parameters/test_params_exp.json")

    def tearDown(self):
        del self.params

    def test_load_parameters(self):
        self.assertEqual(self.params.__dict__, self.params_exp.__dict__)

    # @unittest.skip("skip")
    def test_eval_param(self):
        self.assertEqual(self.params._eval_param("True"), True)

    # @unittest.skip("skip")
    def test_get_num_series(self):
        # print self.params.__dict__
        self.assertEqual(self.params._get_num_series(self.params.__dict__), 2)

    def test_apply_to_all(self):
        self.assertEqual(self.params._apply_to_all(True, 2), [True, True])


if __name__ == '__main__':
    nose.run(defaultTest=__name__)