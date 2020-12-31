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
## @file    mMecoSettings/enumLib.py    @brief [ FILE      ] - Enum module.
## @package mMecoSettings.enumLib       @brief [ MODULE    ] - Enum module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import mCore.enumAbs


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
## @brief [ ENUM CLASS ] - Meco App file attributes.
class AppFileAttribute(mCore.enumAbs.Enum):

    ## [ str ] - Developer.
    kDeveloper          = 'developer'

    ## [ str ] - Description.
    kDescription        = 'description'

    #

    ## [ str ] - Darwin executable.
    kDarwinExecutable   = 'darwinExecutable'

    ## [ str ] - Linux executable.
    kLinuxExecutable    = 'linuxExecutable'

    ## [ str ] - Windows executable.
    kWindowsExecutable  = 'windowsExecutable'

    #

    ## [ str ] - Global env class name.
    kGlobalEnvClassName = 'globalEnvClassName'

    ## [ str ] - Application.
    kApplication        = 'application'

    ## [ str ] - Folder name.
    kFolderName         = 'folderName'

    ## [ str ] - Version.
    kVersion            = 'version'

    ## [ str ] - Packages.
    kPackages           = 'packages'