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
## @file    mMecoSettings/appLib.py    @brief [ FILE      ] - Meco App functionalities module.
## @package mMecoSettings.appLib       @brief [ MODULE    ] - Meco App functionalities module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os
import json

import mFileSystem.directoryLib
import mFileSystem.jsonFileLib

import mMecoSettings.enumLib
import mMecoSettings.envVariablesLib
import mMecoSettings.exceptionLib

import mMecoPackage.packageLib
import mMecoPackage.enumLib


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
## @brief [ CLASS ] - Operate on Meco App files.
class AppFile(mFileSystem.jsonFileLib.JSONFile):
    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC STATIC MEMBERS
    # ------------------------------------------------------------------------------------------------
    ## [ str ] - Meco App file extension.
    EXTENSION       = 'json'

    ## [ str ] - Name of the app package.
    PACKAGE_NAME    = 'mMecoSettings'

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param absFile [ str | None | in  ] - Absolute path of a Meco App file.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self, absFile=None):

        ## [ str ] - Developer.
        self._developer             = ''

        ## [ str ] - Description.
        self._description           = ''

        #

        ## [ str ] - Mac OS executable.
        self._darwinExecutable      = ''

        ## [ str ] - Linux executable.
        self._linuxExecutable       = ''

        ## [ str ] - Windows executable.
        self._windowsExecutable     = ''

        #

        ## [ str ] - Global env class name.
        self._globalEnvClassName    = ''

        ## [ str ] - Application.
        self._application           = ''

        ## [ str ] - Folder name.
        self._folderName            = ''

        ## [ str ] - Version.
        self._version               = ''

        #

        ## [ str ] - Packages.
        self._packages        = ''

        #

        mFileSystem.jsonFileLib.JSONFile.__dict__['__init__'](self, absFile)

    #
    # ------------------------------------------------------------------------------------------------
    # PROPERTY METHODS
    # ------------------------------------------------------------------------------------------------
    ## @name PROPERTIES

    ## @{
    #
    ## @brief Set developer.
    #
    #  @param developer [ str | None | in  ] - Developer's email address.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setDeveloper(self, developer):

        self._developer = developer

    #
    ## @brief Developer.
    #
    #  @exception N/A
    #
    #  @return str - Developer.
    def developer(self):

        return self._developer

    #
    ## @brief Set description.
    #
    #  @param description [ str | None | in  ] - Description.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setDescription(self, description):

        self._description = description

    #
    ## @brief Description.
    #
    #  @exception N/A
    #
    #  @return str - Description.
    def description(self):

        return self._description

    #
    ## @brief Set Darwin executable.
    #
    #  @param darwinExecutable [ str | None | in  ] - Mac OS executable.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setDarwinExecutable(self, darwinExecutable):

        self._darwinExecutable = darwinExecutable

    #
    ## @brief Darwin executable.
    #
    #  @exception N/A
    #
    #  @return str - Darwin executable.
    def darwinExecutable(self):

        return self._darwinExecutable

    #
    ## @brief Set Linux executable.
    #
    #  @param linuxExecutable [ str | None | in  ] - Linux OS executable.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setLinuxExecutable(self, linuxExecutable):

        self._linuxExecutable = linuxExecutable

    #
    ## @brief Linux executable.
    #
    #  @exception N/A
    #
    #  @return str - Linux executable.
    def linuxExecutable(self):

        return self._linuxExecutable

    #
    ## @brief Set Windows executable.
    #
    #  @param windowsExecutable [ str | None | in  ] - Windows OS executable.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setWindowsExecutable(self, windowsExecutable):

        self._windowsExecutable = windowsExecutable

    #
    ## @brief Windows executable.
    #
    #  @exception N/A
    #
    #  @return str - Windows executable.
    def windowsExecutable(self):

        return self._windowsExecutable

    #
    ## @brief Set global env class name.
    #
    #  @param globalEnvClassName [ str | None | in  ] - Global env class name.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setGlobalEnvClassName(self, globalEnvClassName):

        self._globalEnvClassName = globalEnvClassName

    #
    ## @brief Global env class name.
    #
    #  @exception N/A
    #
    #  @return str - Global env class name.
    def globalEnvClassName(self):

        return self._globalEnvClassName

    #
    ## @brief Set application.
    #
    #  @param application [ str | None | in  ] - Application.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setApplication(self, application):

        self._application = application

    #
    ## @brief Application.
    #
    #  @exception N/A
    #
    #  @return str - Application.
    def application(self):

        return self._application

    #
    ## @brief Set folder name.
    #
    #  @param folderName [ str | None | in  ] - Folder name.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setFolderName(self, folderName):

        self._folderName = folderName

    #
    ## @brief Folder name.
    #
    #  @exception N/A
    #
    #  @return str - Folder name.
    def folderName(self):

        return self._folderName

    #
    ## @brief Set version.
    #
    #  @param version [ str | None | in  ] - Version.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setVersion(self, version):

        self._version = version

    #
    ## @brief Version.
    #
    #  @exception N/A
    #
    #  @return str - Version.
    def version(self):

        return self._version

    #
    ## @brief Set packages.
    #
    #  @param packages [ list of str | None | in  ] - Packages.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def setPackages(self, packages):

        self._packages = packages

    #
    ## @brief Packages.
    #
    #  @exception N/A
    #
    #  @return list of str - Packages.
    def packages(self):

        return self._packages

    #
    ## @}

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param fileName              [ str  | None  | in  ] - Name of the Meco App file, which will be created.
    #  @param developer             [ str  | None  | in  ] - Email address of the developer.
    #  @param description           [ str  | None  | in  ] - Description about the app.
    #  @param darwinExecutable      [ str  | None  | in  ] - Mac OS executable.
    #  @param linuxExecutable       [ str  | None  | in  ] - Linux executable.
    #  @param windowsExecutable     [ str  | None  | in  ] - Windows executable.
    #  @param globalEnvClassName    [ str  | None  | in  ] - Global env class name.
    #  @param application           [ str  | None  | in  ] - Application.
    #  @param folderName            [ str  | None  | in  ] - Folder name of the app.
    #  @param version               [ str  | None  | in  ] - Version of the app.
    #  @param packages              [ str  | []    | in  ] - Packages.
    #  @param overwrite             [ bool | False | in  ] - Whether to overwrite existing app file.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def create(self,
               fileName,
               developer='',
               description='',
               darwinExecutable='',
               linuxExecutable='',
               windowsExecutable='',
               globalEnvClassName='',
               application='',
               folderName='',
               version='',
               packages=[],
               overwrite=False
               ):

        localDict = locals()

        content = {}

        for key, value in localDict.items():
            if key in ['self', 'fileName', 'overwrite']:
                continue
            content[key] = value

        developmentPackagesPath = os.environ.get(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_PACKAGES_PATH)
        if not developmentPackagesPath:
            raise mMecoSettings.exceptionLib.ValidEnvironmentIsNotError('You must initialize development environment to create a Meco App.')

        packagePath = os.path.join(developmentPackagesPath, AppFile.PACKAGE_NAME)
        if not os.path.isdir(packagePath):
            raise mMecoSettings.exceptionLib.MissingPackageError('You must have {} package in your development environment to create a Meco App.'.format(AppFile.PACKAGE_NAME))

        #

        _package = mMecoPackage.packageLib.Package(packagePath)

        appFilePath = os.path.join(_package.getLocalPath(mMecoPackage.enumLib.PackageFolderStructure.kResourcesApp))
        if not os.path.isdir(appFilePath):
            os.makedirs(appFilePath)

        if not fileName.endswith(AppFile.EXTENSION):
            fileName = '{}.{}'.format(fileName, AppFile.EXTENSION)
        appFile = os.path.join(appFilePath, fileName)

        #

        if os.path.isfile(appFile) and not overwrite:
            raise IOError('App file already exists: {}'.format(appFile))

        with open(appFile, 'w') as outFile:
            json.dump(content, outFile, indent=4)

        return self.setFile(appFile)

    #
    ## @brief Determine whether this app file is valid.
    #
    #  For an app file to be valid it must have values for the following keys.
    #  - `developer`
    #  - `description`
    #
    #  @exception N/A
    #
    #  @return None - None.
    def isValid(self):

        if not self._file:
            return False

        if not self._developer:
            return False

        if not self._description:
            return False

        return True

    #
    # ------------------------------------------------------------------------------------------------
    # REIMPLEMENTED PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Set JSON file.
    #
    #  @param path [ str | None | in  ] - Absolute path of the file.
    #
    #  @exception N/A
    #
    #  @return bool - Result, returns False is the file doesn't exist.
    def setFile(self, path):

        if not path.endswith(AppFile.EXTENSION):
            path = '{}.{}'.format(path, AppFile.EXTENSION)

        if mFileSystem.jsonFileLib.JSONFile.__dict__['setFile'](self, path):
            self.read()
            return True

        return False

    #
    ## @brief Get string representation.
    #
    #  @exception N/A
    #
    #  @return str - File info
    def asStr(self):

        info = '\n'
        info += 'Meco App File      : {}\n'.format(self._file)

        info += 'developer          : {}\n'.format(self._developer)
        info += 'description        : {}\n'.format(self._description)

        info += 'darwinExecutable   : {}\n'.format(self._darwinExecutable)
        info += 'linuxExecutable    : {}\n'.format(self._linuxExecutable)
        info += 'windowsExecutable  : {}\n'.format(self._windowsExecutable)

        info += 'globalEnvClassName : {}\n'.format(self._globalEnvClassName)
        info += 'application        : {}\n'.format(self._application)
        info += 'folderName         : {}\n'.format(self._folderName)
        info += 'version            : {}\n'.format(self._version)

        info += 'packages           : {}\n'.format(','.join(self._packages))

        return info

    #
    ## @brief Write the content into the file.
    #
    #  @exception ValueError - If content is not an instance of dict.
    #
    #  @return bool - Result.
    def write(self):

        if not isinstance(self._content, dict):
            raise ValueError('Content of a Meco App file must be a dict instance, it is not.')

        result = mFileSystem.jsonFileLib.JSONFile.__dict__['write'](self, indent=4)

        for key, value in self._content.items():
            setattr(self, '_{}'.format(key), value)

        return result

    #
    ## @brief Read the content of the file and store it in content member.
    #
    #  @exception N/A
    #
    #  @return variant - Content.
    def read(self):

        mFileSystem.jsonFileLib.JSONFile.__dict__['read'](self)

        for key, value in self._content.items():
            setattr(self, '_{}'.format(key), value)

        return self._content

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief List Meco app files available in the initialized environment.
    #
    #  @param keyword [ str  | None | in  ] - Keyword to filter the app files.
    #
    #  @exception N/A
    #
    #  @return list of mMecoSettings.appLib.AppFile - App files.
    #  @return None                                 - If no app file found.
    @staticmethod
    def list(keyword=None):

        directory   = mFileSystem.directoryLib.Directory()
        package     = mMecoPackage.packageLib.Package(os.path.abspath(__file__))

        if not directory.setDirectory(package.getLocalPath(mMecoPackage.enumLib.PackageFolderStructure.kResourcesApp)):
            return None

        appFiles = directory.listFilesWithAbsolutePath(ignoreDot=True, extension=AppFile.EXTENSION)
        appFiles = [AppFile(x) for x in appFiles]

        if keyword:
            appFiles = [x for x in appFiles if keyword in x.developer() or          \
                                               keyword in x.description() or        \
                                               keyword in x.globalEnvClassName() or \
                                               keyword in x.application() or        \
                                               keyword in x.folderName() or         \
                                               keyword in x.version() or            \
                                               keyword in x.packages()
                        ]

        return appFiles

