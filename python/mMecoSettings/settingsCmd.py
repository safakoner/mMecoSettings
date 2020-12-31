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
## @file    mMecoSettings/settingsCmd.py    @brief [ FILE      ] - Command module.
## @package mMecoSettings.settingsCmd       @brief [ MODULE    ] - Command module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import argparse

import mCore.displayLib

import mMecoSettings.appLib


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
## @brief Create a Meco App.
#
#  @exception N/A
#
#  @return None - None.
def createApp():

    parser = argparse.ArgumentParser(description='Create a Meco App')

    parser.add_argument('name',
                        type=str,
                        help='Name of the app')

    _args       = parser.parse_args()

    mecoApp     = mMecoSettings.appLib.AppFile()

    try:
        result = mecoApp.create(fileName=_args.name, overwrite=False)
    except Exception as error:
        mCore.displayLib.Display.displayBlankLine()
        mCore.displayLib.Display.displayFailure(str(error))
        mCore.displayLib.Display.displayBlankLine()
        return

    mCore.displayLib.Display.displaySuccess('Meco App file has been created.')
    mCore.displayLib.Display.displaySuccess(mecoApp.file())
    mCore.displayLib.Display.displayBlankLine()

#
## @brief List Meco App files.
#
#  @exception N/A
#
#  @return None - None.
def listApps():

    parser = argparse.ArgumentParser(description='List Meco App files')

    parser.add_argument('-d',
                        '--detail',
                        action='store_true',
                        help='Display details about the app files')

    _args = parser.parse_args()

    _listApps(detail=_args.detail)

#
## @brief Search Meco App files.
#
#  @exception N/A
#
#  @return None - None.
def searchApps():

    parser = argparse.ArgumentParser(description='Search Meco App files')

    parser.add_argument('keyword',
                        type=str,
                        help='Keyword, which will be used to find Meco App files with')

    parser.add_argument('-d',
                        '--detail',
                        action='store_true',
                        help='Display details about the app files')

    _args = parser.parse_args()

    _listApps(keyword=_args.keyword, detail=_args.detail)

#
## @brief List Meco App files.
#
#  This function is used by the following functions.
#
#  - mMecoSettings.settingsCmd.listApps
#  - mMecoSettings.settingsCmd.searchApps
#
#  @param keyword [ str  | None  | in  ] - Keyword.
#  @param detail  [ bool | False | in  ] - Display detail.
#
#  @exception N/A
#
#  @return None - None.
def _listApps(keyword=None, detail=False):

    appFiles = mMecoSettings.appLib.AppFile.list(keyword)

    if not appFiles:
        mCore.displayLib.Display.displayBlankLine()
        mCore.displayLib.Display.displayInfo('No Meco App found.')
        mCore.displayLib.Display.displayBlankLine()
        return 

    for app in appFiles:

        if detail:
            mCore.displayLib.Display.displayInfo(app, startNewLine=False)
        else:
            mCore.displayLib.Display.displayInfo(app.baseName(), endNewLine=False)

    mCore.displayLib.Display.displayBlankLine()
    mCore.displayLib.Display.displayInfo('{} Meco Apps found.'.format(len(appFiles)))
    mCore.displayLib.Display.displayBlankLine()