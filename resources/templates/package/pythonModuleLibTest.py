#
# Copyright 2020.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    PACKAGE_NAME/tests/PYTHON_MODULE_NAMETest.py   @brief [ FILE      ] - Python unit test module.
## @package PACKAGE_NAME.tests.PYTHON_MODULE_NAMETest      @brief [ MODULE    ] - Python unit test module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import unittest


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):

        pass

    def test_method(self):

        self.assertEqual(True, True)


#
#-----------------------------------------------------------------------------------------------------
# INVOKE
#-----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    unittest.main()