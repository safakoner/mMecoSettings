#
# Copyright 2020 Safak Oner.
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
## @file    mMecoSettings/tests/appLibTest.py @brief [ FILE   ] - Unit test module.
## @package mMecoSettings.tests.appLibTest    @brief [ MODULE ] - Unit test module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os
import unittest

import mMecoPackage.packageLib
import mMecoPackage.enumLib

import mMecoSettings.appLib


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
class AppFileTest(unittest.TestCase):

    def setUp(self):

        package             = mMecoPackage.packageLib.Package(os.path.abspath(__file__))

        self._appFilePath   = package.getLocalPath(mMecoPackage.enumLib.PackageFolderStructure.kResourcesApp)

        self._appFile       = os.path.join(self._appFilePath, 'atom.json')

    def test_setFile(self):

        _app = mMecoSettings.appLib.AppFile()

        self.assertTrue(_app.setFile(self._appFile), True)

    def test_setFile(self):

        expectedAppData = {'application': 'atom',
                           'darwinExecutable': 'open -a Atom.app',
                           'description': 'Atom',
                           'developer': 'safak@safakoner.com',
                           'folderName': 'atom',
                           'globalEnvClassName': 'Atom',
                           'linuxExecutable': 'atom',
                           'packages': [],
                           'version': '1.53.0',
                           'windowsExecutable': 'atom.exe'}

        _app = mMecoSettings.appLib.AppFile()

        _app.setFile(self._appFile)

        appData = _app.read()

        self.assertEqual(appData, expectedAppData)

    def test_create(self):

        expectedAppData = {"windowsExecutable": "lynx.exe",
                           "description": "Lynx stand-alone application",
                           "darwinExecutable": "open -a Lynx.app",
                           "folderName": "lynx",
                           "version": "317",
                           "globalEnvClassName": "Lynx",
                           "application":"lynx",
                           "packages": [],
                           "linuxExecutable": "lynx",
                           "developer": "safak@safakoner.com"
                           }

        #

        _app = mMecoSettings.appLib.AppFile()

        _app.create(fileName='lynx',
                    developer='safak@safakoner.com',
                    description='Lynx stand-alone application',
                    darwinExecutable='open -a Lynx.app',
                    linuxExecutable='lynx',
                    windowsExecutable='lynx.exe',
                    globalEnvClassName='Lynx',
                    folderName='lynx',
                    application='lynx',
                    version='317',
                    packages=[],
                    overwrite=True
                    )

        #

        _app = mMecoSettings.appLib.AppFile(os.path.join(self._appFilePath, 'lynx'))

        self.assertEqual(_app.content(), expectedAppData)

        #

        _app = mMecoSettings.appLib.AppFile()

        self.assertEqual(_app.setFile(os.path.join(self._appFilePath, 'lynx.json')), True)
        self.assertEqual(_app.content(), expectedAppData)

        _app.remove()

#
#-----------------------------------------------------------------------------------------------------
# INVOKE
#-----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    unittest.main()
