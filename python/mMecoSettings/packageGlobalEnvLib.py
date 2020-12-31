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
## @file    mMecoSettings/packageGlobalEnvLib.py    @brief [ FILE   ] - Package global env module.
## @package mMecoSettings.packageGlobalEnvLib       @brief [ MODULE ] - Package global env module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from platform import system


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
# PACKAGE
#
## @brief [ ENUM CLASS ] - Package folder structure for Linux.
class PackageLinux(object):

    ## [ str ] - Bin (executables) path.
    PATH            = ['bin/{}'.format(system().lower()),
                       'python/bin']

    ## [ str ] - Library path.
    LD_LIBRARY_PATH = ['lib/{}'.format(system().lower())]

    ## [ str ] - Python path.
    PYTHONPATH      = ['python']

#
## @brief [ ENUM CLASS ] - Package folder structure for Darwin.
class PackageDarwin(PackageLinux):

    ## [ str ] - Library path.
    LD_LIBRARY_PATH             = None

    ## [ str ] - Library path.
    DYLD_FALLBACK_LIBRARY_PATH  = ['lib/{}'.format(system().lower())]

#
## @brief [ ENUM CLASS ] - Package folder structure for Windows.
class PackageWindows(object):

    ## [ str ] - Bin (executables) path.
    PATH            = ['bin\\{}'.format(system().lower()),
                       'python\\bin']

    ## [ str ] - Library path.
    LIBRARY_PATH    = ['lib\\{}'.format(system().lower())]

    ## [ str ] - Python path.
    PYTHONPATH      = ['python']

#
# MAYA
#
## @brief [ ENUM CLASS ] - Maya folder structure in a package for Linux.
class MayaLinux(object):

    ## [ str ] - Python path.
    PYTHONPATH          = ['FOLDER_NAME/VERSION/python']

    ## [ str ] - Maya script.
    MAYA_SCRIPT_PATH    = ['FOLDER_NAME/VERSION/mel']

    ## [ str ] - Maya shelves.
    MAYA_SHELF_PATH     = ['FOLDER_NAME/VERSION/shelves']

    ## [ str ] - Maya plugin.
    MAYA_PLUG_IN_PATH   = ['FOLDER_NAME/VERSION/plugin/{}'.format(system().lower())]

    ## [ str ] - Maya XMB.
    XBMLANGPATH         = ['FOLDER_NAME/VERSION/xbm']

#
## @brief [ ENUM CLASS ] - Maya folder structure in a package for Darwin.
class MayaDarwin(MayaLinux):

    pass

#
## @brief [ ENUM CLASS ] - Maya folder structure in a package for Windows.
class MayaWindows(object):

    ## [ str ] - Python path.
    PYTHONPATH          = ['FOLDER_NAME\\VERSION\\python']

    ## [ str ] - Maya script.
    MAYA_SCRIPT_PATH    = ['FOLDER_NAME\\VERSION\\mel']

    ## [ str ] - Maya shelves.
    MAYA_SHELF_PATH     = ['FOLDER_NAME\\VERSION\\shelves']

    ## [ str ] - Maya plugin.
    MAYA_PLUG_IN_PATH   = ['FOLDER_NAME\\VERSION\\plugin\\{}'.format(system().lower())]

    ## [ str ] - Maya XMB.
    XBMLANGPATH         = ['FOLDER_NAME\\VERSION\\xbm']


