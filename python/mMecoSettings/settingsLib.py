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
## @file    mMecoSettings/settingsLib.py    @brief [ FILE   ] - Settings module.
## @package mMecoSettings.settingsLib       @brief [ MODULE ] - Settings module.
#
#  This is the settings module where you can change the implementation of the settings functions in order
#  to customize Meco. Please check the relevant function for detailed description below.
#
#  All functions below are invoked by Meco and their arguments are provided automatically.
#
#  @warning Return objects of each function must be implemented correctly for each platform, which Meco will run on.
#
#  @warning Do not rename any of the functions or the arguments.

#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import json
import  os
import  re

from    getpass  import getuser
from    platform import system

import  mMeco.core.packageLib
from    mMecoSettings.envVariablesLib import MECO_USE_PROJECT_APPS_ONLY


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
#
## [ bool ] - Whether the current platform is Windows.
IS_WINDOWS          = system() == 'Windows'

#
## [ str ] - Name of the master project.
MASTER_PROJECT_NAME = 'master'

#
## [ str ] - Reserved env name.
RESERVED_ENV_NAME   = 'main'


#
#
#
# ----------------------------------------------------------------------------------------------------
# ENUMS
# ----------------------------------------------------------------------------------------------------
#
## @brief [ ENUM CLASS ] - Platform names.
class PlatformName(object):

    ## [ str ] - Linux.
    kLinux   = 'Linux'

    ## [ str ] - Mac OS.
    kDarwin  = 'Darwin'

    ## [ str ] - Windows.
    kWindows = 'Windows'

#
#
#
#-----------------------------------------------------------------------------------------------------
# PROJECT & PACKAGE PATH SETTINGS
#-----------------------------------------------------------------------------------------------------
#
## @brief Get absolute path of projects.
#
#  Absolute path of where the projects are kept.
#
#  @param platformName [ str | None                                           | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#  @param projectName  [ str | mMecoSettings.settingsLib.MASTER_PROJECT_NAME  | in  ] - Project name, which the project path will be provided for.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getProjectsPath(platformName, projectName=MASTER_PROJECT_NAME):

    # sys.stdout.write('\n')
    # sys.stdout.write('platformName       : {}\n'.format(platformName))
    # sys.stdout.write('projectName        : {}\n'.format(projectName))

    # Projects path is determined in relative manner.
    # Since published packages has one parent folder called same name as the package name,
    # determining whether this function is invoked in development environment or production environment is done
    # by following regex.
    production = re.search(r'.*(mMecoSettings[\\\\|/][0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}|[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}|[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}|[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}[\\\\|/]mMecoSettings[\\\\|/]python[\\\\|/]mMecoSettings).*',
                           __file__)

    if platformName == PlatformName.kLinux:

        if production:
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', '..', 'meco'))
        else:
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', '..', '..', 'meco'))

    elif platformName == PlatformName.kDarwin:

        if production:
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', '..', 'meco'))
        else:
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', '..', '..', 'meco'))

    elif platformName == PlatformName.kWindows:

        if production:
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', '..', 'meco'))
        else:
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', '..', '..', 'meco'))

#
## @brief Get absolute path of given project.
#
#  Absolute path of where the projects are kept.
#
#  @param platformName [ str | None                                           | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#  @param projectName  [ str | mMecoSettings.settingsLib.MASTER_PROJECT_NAME  | in  ] - Project name, which the project path will be provided for.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getProjectRootPath(platformName, projectName=MASTER_PROJECT_NAME):

    return os.path.join(getProjectsPath(platformName), projectName)

#
## @brief Get reserved packages path.
#
#  Return path is where the reserved packages are kept for given developer.
#
#  An example path would be like;
#
#  `/projectsPath/MASTER_PROJECT_NAME/developers/DEVELOPER_NAME/reserved/main`
#
#  @param developerName      [ str  | None | in  ] - Developer name.
#  @param platformName       [ str  | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getReservedPackagesPath(developerName, platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('developerName      : {}\n'.format(developerName))
    # sys.stdout.write('platformName       : {}\n'.format(platformName))

    path = os.path.join(getProjectsPath(platformName, MASTER_PROJECT_NAME),
                        MASTER_PROJECT_NAME,
                        'developers',
                        developerName,
                        'reserved',
                        RESERVED_ENV_NAME)

    return path

#
## @brief Get development packages path.
#
#  Return path is where the development packages are kept for given project, developer and development environment.
#
#  An example path would be like;
#
#  `/projectsPath/PROJECT_NAME/developers/DEVELOPER_NAME/development/DEVELOPMENT_ENV_NAME`
#
#  @param projectName        [ str  | None | in  ] - Project name.
#  @param developerName      [ str  | None | in  ] - Developer name.
#  @param developmentEnvName [ str  | None | in  ] - Development environment name.
#  @param platformName       [ str  | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#  @param create             [ bool | None | in  ] - Create the development packages path if it doesn't exist.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getDevelopmentPackagesPath(projectName, developerName, developmentEnvName, platformName, create=False):

    # sys.stdout.write('\n')
    # sys.stdout.write('projectName        : {}\n'.format(projectName))
    # sys.stdout.write('developerName      : {}\n'.format(developerName))
    # sys.stdout.write('developmentEnvName : {}\n'.format(developmentEnvName))
    # sys.stdout.write('platformName       : {}\n'.format(platformName))
    # sys.stdout.write('create             : {}\n'.format(create))

    path = os.path.join(getProjectsPath(platformName, projectName),
                        projectName,
                        'developers',
                        developerName,
                        'development',
                        developmentEnvName)

    if create and not os.path.isdir(path):
        os.makedirs(path)

    return path

#
## @brief Get stage packages path.
#
#  Return path is where the stage packages are kept for given project, developer and stage environment.
#
#  An example path would be like;
#
#  `/projectsPath/PROJECT_NAME/developers/DEVELOPER_NAME/stage/STAGE_ENV_NAME`
#
#  @param projectName   [ str | None | in  ] - Project name.
#  @param developerName [ str | None | in  ] - Developer name.
#  @param stageEnvName  [ str | None | in  ] - Stage environment name.
#  @param platformName  [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getStagePackagesPath(projectName, developerName, stageEnvName, platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('projectName        : {}\n'.format(projectName))
    # sys.stdout.write('developerName      : {}\n'.format(developerName))
    # sys.stdout.write('stageEnvName       : {}\n'.format(stageEnvName))
    # sys.stdout.write('platformName       : {}\n'.format(platformName))

    return os.path.join(getProjectsPath(platformName, projectName),
                        projectName,
                        'developers',
                        developerName,
                        'stage',
                        stageEnvName)

#
## @brief Get project internal packages path.
#
#  Return path is where the internal production packages are kept for given project.
#
#  An example path would be like;
#
#  `/projectsPath/PROJECT_NAME/internal`
#
#  @param projectName  [ str | None | in  ] - Project name.
#  @param platformName [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getProjectInternalPackagesPath(projectName, platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('projectName  : {}\n'.format(projectName))
    # sys.stdout.write('platformName : {}\n'.format(platformName))

    return os.path.join(getProjectsPath(platformName, projectName),
                        projectName,
                        'internal')

#
## @brief Get project external packages path.
#
#  Return path is where the external production packages are kept for given project.
#
#  An example path would be like;
#
#  `/projectsPath/PROJECT_NAME/external`
#
#  @param projectName  [ str | None | in  ] - Project name.
#  @param platformName [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getProjectExternalPackagesPath(projectName, platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('projectName  : {}\n'.format(projectName))
    # sys.stdout.write('platformName : {}\n'.format(platformName))

    return os.path.join(getProjectsPath(platformName, projectName),
                        projectName,
                        'external')

#
## @brief Get master project internal packages path.
#
#  Return path is where the internal production packages are kept for master project.
#
#  An example path would be like;
#
#  `/projectsPath/MASTER_PROJECT_NAME/internal`
#
#  @param platformName [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getMasterProjectInternalPackagesPath(platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('platformName : {}\n'.format(platformName))

    return os.path.join(getProjectsPath(platformName), MASTER_PROJECT_NAME, 'internal')

#
## @brief Get master project external packages path.
#
#  Return path is where the external production packages are kept for master project.
#
#  An example path would be like;
#
#  `/projectsPath/MASTER_PROJECT_NAME/external`
#
#  @param platformName [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return str - Absolute path.
def getMasterProjectExternalPackagesPath(platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('platformName : {}\n'.format(platformName))

    return os.path.join(getProjectsPath(platformName), MASTER_PROJECT_NAME, 'external')

#
#
#
#-----------------------------------------------------------------------------------------------------
# FILE SETTINGS
#-----------------------------------------------------------------------------------------------------
#
## @brief Get absolute path of a log file.
#
#  Log file would contain useful information for debugging purposes.
#
#  The following example path is also the one Meco uses by default.
#
#  `/projectsPath/PROJECT_NAME/users/USER_NAME/env/log/log.txt`
#
#  @param projectName        [ str | None | in  ] - Project name.
#  @param userName           [ str | None | in  ] - User name.
#  @param developmentEnvName [ str | None | in  ] - Development environment name.
#  @param stageEnvName       [ str | None | in  ] - Stage environment name.
#  @param platformName       [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return str - Absolute path of the log file.
def getLogFilePath(projectName, userName, developmentEnvName, stageEnvName, platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('projectName        : {}\n'.format(projectName))
    # sys.stdout.write('userName           : {}\n'.format(userName))
    # sys.stdout.write('developmentEnvName : {}\n'.format(developmentEnvName))
    # sys.stdout.write('stageEnvName       : {}\n'.format(stageEnvName))
    # sys.stdout.write('platformName       : {}\n'.format(platformName))
    # sys.stdout.write('app                : {}\n'.format(app))

    if not projectName:
        projectName = MASTER_PROJECT_NAME

    projectPath = getProjectsPath(platformName, projectName)
    if not os.path.isdir(projectPath):
        return ''

    logPath = os.path.join(projectPath,
                           projectName,
                           'users',
                           userName,
                           'env',
                           'log')

    if not os.path.isdir(logPath):
        os.makedirs(logPath)

    #

    logFileName = 'log_{}_{}'.format(projectName, userName)

    if developmentEnvName:
        logFileName = '{}_development_{}.txt'.format(logFileName, developmentEnvName)
    elif stageEnvName:
        logFileName = '{}_stage_{}.txt'.format(logFileName, stageEnvName)
    else:
        logFileName = '{}.txt'.format(logFileName)

    return os.path.join(logPath, logFileName)

#
## @brief Get absolute path of an app file.
#
#  Function returns the absolute file path of requested app, so information regarding the app can be obtained.
#
#  Location of the app file may vary. Example paths;
#
#  If development environment is initialized;
#
#  `/projectsPath/PROJECT_NAME/developers/DEVELOPER_NAME/development/DEVELOPMENT_ENV_NAME/mMecoSettings/resources/apps/ENV_NAME.json`
#
#  If stage environment is initialized;
#
#  `/projectsPath/PROJECT_NAME/developers/DEVELOPER_NAME/stage/STAGE_ENV_NAME/mMecoSettings/resources/apps/ENV_NAME.json`
#
#  If project environment is initialized;
#
#  `/projectsPath/PROJECT_NAME/packages/mMecoSettings/0.0.0/mMecoSettings/resources/apps/ENV_NAME.json`
#
#  If no project environment is initialized meaning that only master project is initialized;
#
#  `/projectsPath/MASTER_PROJECT_NAME/packages/mMecoSettings/1.0.0/mMecoSettings/resources/apps/ENV_NAME.json`
#
#  App file will be searched for in the paths provided above with the given order.
#
#  @param projectName        [ str | None | in  ] - Project name.
#  @param developerName      [ str | None | in  ] - Developer name.
#  @param developmentEnvName [ str | None | in  ] - Development environment name.
#  @param stageEnvName       [ str | None | in  ] - Stage environment name.
#  @param platformName       [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#  @param app                [ str | None | in  ] - App.
#
#  @exception IOError - If no app file found for given `app`.
#
#  @return str - Absolute path of the app file.
def getAppFilePath(projectName, developerName, developmentEnvName, stageEnvName, platformName, app):

    # sys.stdout.write('\n')
    # sys.stdout.write('projectName        : {}\n'.format(projectName))
    # sys.stdout.write('developerName      : {}\n'.format(developerName))
    # sys.stdout.write('developmentEnvName : {}\n'.format(developmentEnvName))
    # sys.stdout.write('stageEnvName       : {}\n'.format(stageEnvName))
    # sys.stdout.write('platformName       : {}\n'.format(platformName))
    # sys.stdout.write('app                : {}\n'.format(app))

    if not app:
        return ''

    if os.path.isfile(app):
        return app

    missingAppFiles  = []
    appFileExtension = 'json'
    appPath          = os.path.join('mMecoSettings', 'resources', 'apps')


    if developmentEnvName:
        appFile = os.path.join(getDevelopmentPackagesPath(projectName, developerName, developmentEnvName, platformName, False),
                               appPath,
                               '{}.{}'.format(app, appFileExtension))
        if os.path.isfile(appFile):
            return appFile
        else:
            missingAppFiles.append(appFile)

    if stageEnvName:
        appFile = os.path.join(getStagePackagesPath(projectName, developerName, stageEnvName, platformName),
                               appPath,
                               '{}.{}'.format(app, appFileExtension))
        if os.path.isfile(appFile):
            return appFile
        else:
            missingAppFiles.append(appFile)

    #

    latestVersion = mMeco.core.packageLib.getVersionOfAPackage(getProjectInternalPackagesPath(projectName, platformName),
                                                               'mMecoSettings')
    if latestVersion:
        appPath = os.path.join('mMecoSettings', latestVersion, 'mMecoSettings', 'resources', 'apps')

        if projectName != MASTER_PROJECT_NAME:
            appFile = os.path.join(getProjectInternalPackagesPath(projectName, platformName),
                                   appPath,
                                   '{}.{}'.format(app, appFileExtension))
            if os.path.isfile(appFile):
                return appFile
            else:
                missingAppFiles.append(appFile)


    if os.environ.get(MECO_USE_PROJECT_APPS_ONLY) is None:
        latestVersion = mMeco.core.packageLib.getVersionOfAPackage(getMasterProjectInternalPackagesPath(platformName),
                                                                   'mMecoSettings')
        if latestVersion:
            appPath = os.path.join('mMecoSettings', latestVersion, 'mMecoSettings', 'resources', 'apps')
            appFile = os.path.join(getMasterProjectInternalPackagesPath(platformName),
                                   appPath,
                                   '{}.{}'.format(app, appFileExtension))
            if os.path.isfile(appFile):
                return appFile
            else:
                missingAppFiles.append(appFile)

    raise IOError('None of the following app file exist: {}'.format(', '.join(missingAppFiles)))

#
## @brief Get absolute path of a script file.
#
#  Script file will be written out by Meco and will contain the environment, so it can be sourced to set the environment.
#
#  The following example path is also the one Meco uses by default.
#
#  `/projectsPath/PROJECT_NAME/users/USER_NAME/env/script/env_PROJECT_NAME_USER_NAME_DEVELOPMENT_ENV_NAME|STAGE_ENV_NAME.EXTENSION`
#
#  @warning An empty string must be returned from the function is no path is meant to be provided.
#
#  @param projectName        [ str | None | in  ] - Project name.
#  @param userName           [ str | None | in  ] - User name.
#  @param developmentEnvName [ str | None | in  ] - Development environment name.
#  @param stageEnvName       [ str | None | in  ] - Stage environment name.
#  @param platformName       [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#  @param appFile            [ str | None | in  ] - Absolute path of an app file if provided.
#
#  @exception N/A
#
#  @return str - Absolute path of the environment script file.
def getScriptFilePath(projectName, userName, developmentEnvName, stageEnvName, platformName, appFile):

    # sys.stdout.write('\n')
    # sys.stdout.write('projectName        : {}\n'.format(projectName))
    # sys.stdout.write('userName           : {}\n'.format(userName))
    # sys.stdout.write('developmentEnvName : {}\n'.format(developmentEnvName))
    # sys.stdout.write('stageEnvName       : {}\n'.format(stageEnvName))
    # sys.stdout.write('platformName       : {}\n'.format(platformName))
    # sys.stdout.write('platformName       : {}\n'.format(appFile))

    if appFile:
        appFile = '_{}'.format(os.path.splitext(os.path.basename(appFile))[0])
    else:
        appFile = ''

    scriptPath = os.path.join(getProjectsPath(platformName, projectName),
                              projectName,
                              'users',
                              getuser(),
                              'env',
                              'script')

    if not os.path.isdir(scriptPath):
        os.makedirs(scriptPath)

    scriptFileBaseName = 'env_{}_{}'.format(projectName, userName)

    if developmentEnvName:
        scriptFileBaseName = '{}_development_{}'.format(scriptFileBaseName, developmentEnvName)
    elif stageEnvName:
        scriptFileBaseName = '{}_stage_{}'.format(scriptFileBaseName, stageEnvName)

    if platformName == PlatformName.kLinux:

        return os.path.join(scriptPath, '{}{}.sh'.format(scriptFileBaseName, appFile))

    elif platformName == PlatformName.kDarwin:

        return os.path.join(scriptPath, '{}{}.sh'.format(scriptFileBaseName, appFile))

    elif platformName == PlatformName.kWindows:

        return os.path.join(scriptPath, '{}{}.ps1'.format(scriptFileBaseName, appFile))

#
#
#
#-----------------------------------------------------------------------------------------------------
# COLOR SETTINGS
#-----------------------------------------------------------------------------------------------------
#
## @brief Get terminal header display colors.
#
#  You can customize the terminal header display colors by changing the return value of this function.
#
#  Index   | Description                                                             |
#  :------ | :---------------------------------------------------------------------- |
#  0.      | Color of the dashes in headers                                          |
#  1.      | Color of the text in headers                                            |
#
#  @warning Only following colors are available on Windows OS.
#
# - Black
# - DarkBlue
# - DarkGreen
# - DarkCyan
# - DarkRed
# - DarkMagenta
# - DarkYellow
# - Gray
# - DarkGray
# - Blue
# - Green
# - Cyan
# - Red
# - Magenta
# - Yellow
# - White
#
#  @param platformName [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return list of str - Values that represents colors.
def getTerminalHeaderDisplayColors(platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('platformName : {}\n'.format(platformName))

    if platformName == PlatformName.kLinux:

        return ['"\e[37m{}\e[m"',
                '"\e[97m{}\e[m"']

    elif platformName == PlatformName.kDarwin:

        return ['"\e[37m{}\e[m"',
                '"\e[97m{}\e[m"']

    elif platformName == PlatformName.kWindows:

        return ['DarkGray', 'Gray']

#
## @brief Get terminal display colors.
#
#  You can customize the terminal display colors by changing the return value of this function.
#
#  Index   | Description                                                             |
#  :------ | :---------------------------------------------------------------------- |
#  0.      | Color of the development environment                                    |
#  1.      | Color of the stage environment                                          |
#  2.      | Color of the project environment                                        |
#  3.      | Color of the master project environment                                 |
#  4.      | Color of the before environment                                         |
#  5.      | Color of the after environment                                          |
#  6.      | Color of info                                                           |
#
#  @warning Only following colors are available on Windows OS.
#
# - Black
# - DarkBlue
# - DarkGreen
# - DarkCyan
# - DarkRed
# - DarkMagenta
# - DarkYellow
# - Gray
# - DarkGray
# - Blue
# - Green
# - Cyan
# - Red
# - Magenta
# - Yellow
# - White
#
#  @param platformName [ str | None | in  ] - Platform name, one of the following; Linux, Darwin, Windows.
#
#  @exception N/A
#
#  @return list of str - Values that represents colors.
def getTerminalDisplayColors(platformName):

    # sys.stdout.write('\n')
    # sys.stdout.write('platformName : {}\n'.format(platformName))

    if platformName == PlatformName.kLinux:

        return {
                'pre-build'                 : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;4m{}\e[m'
                                               },

                'reserved'                  : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;9m{}\e[m'
                                               },

                'development'               : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;9m{}\e[m'
                                               },

                'stage'                     : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;9m{}\e[m'
                                               },

                'project-internal'          : {'packageVariable'        :'\e[38;5;11m{}\e[m',
                                               'packageValue'           :'\e[38;5;3m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;11m{}\e[m'
                                               },

                'project-external'          : {'packageVariable'        :'\e[38;5;11m{}\e[m',
                                               'packageValue'           :'\e[38;5;3m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;11m{}\e[m'
                                               },

                'master-project-internal'   : {'packageVariable'        :'\e[38;5;46m{}\e[m',
                                               'packageValue'           :'\e[38;5;47m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;46m{}\e[m'
                                               },

                'master-project-external'   : {'packageVariable'        :'\e[38;5;46m{}\e[m',
                                               'packageValue'           :'\e[38;5;47m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;46m{}\e[m'
                                               },

                'post-build'                : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;4m{}\e[m'
                                               },

                'env'                       : {'colon'                  :'\e[38;5;4m{}\e[m',
                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',
                                               },

                'info'                      : {'colon'                  :'\e[38;5;4m{}\e[m',
                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',
                                               },

                'product-info'              : {'colon'                  :'\e[38;5;4m{}\e[m',
                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',
                                               },

                }

    elif platformName == PlatformName.kDarwin:

        return {
                'pre-build'                 : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;4m{}\e[m'
                                               },

                'reserved'                  : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;9m{}\e[m'
                                               },

                'development'               : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;9m{}\e[m'
                                               },

                'stage'                     : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;9m{}\e[m'
                                               },

                'project-internal'          : {'packageVariable'        :'\e[38;5;11m{}\e[m',
                                               'packageValue'           :'\e[38;5;3m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;11m{}\e[m'
                                               },

                'project-external'          : {'packageVariable'        :'\e[38;5;11m{}\e[m',
                                               'packageValue'           :'\e[38;5;3m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;11m{}\e[m'
                                               },

                'master-project-internal'   : {'packageVariable'        :'\e[38;5;46m{}\e[m',
                                               'packageValue'           :'\e[38;5;47m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;46m{}\e[m'
                                               },

                'master-project-external'   : {'packageVariable'        :'\e[38;5;46m{}\e[m',
                                               'packageValue'           :'\e[38;5;47m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;46m{}\e[m'
                                               },

                'post-build'                : {'packageVariable'        :'\e[38;5;9m{}\e[m',
                                               'packageValue'           :'\e[38;5;9m{}\e[m',

                                               'multiVariable'          :'\e[38;5;4m{}\e[m',
                                               'multiValue'             :'\e[38;5;27m{}\e[m',

                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',

                                               'script'                 :'\e[38;5;219m{}\e[m',
                                               'command'                :'\e[38;5;219m{}\e[m',

                                               'colon'                  :'\e[38;5;4m{}\e[m',
                                               'arrow'                  :'\e[38;5;4m{}\e[m'
                                               },

                'env'                       : {'colon'                  :'\e[38;5;4m{}\e[m',
                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',
                                               },

                'info'                      : {'colon'                  :'\e[38;5;4m{}\e[m',
                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',
                                               },

                'product-info'              : {'colon'                  :'\e[38;5;4m{}\e[m',
                                               'singleVariable'         :'\e[38;5;4m{}\e[m',
                                               'singleValue'            :'\e[38;5;27m{}\e[m',
                                               },

                }

    elif platformName == PlatformName.kWindows:

        return {
            'pre-build'                 : {'packageVariable'        :'Blue',
                                           'packageValue'           :'DarkCyan',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Blue'
                                           },

            'reserved'                  : {'packageVariable'        :'Red',
                                           'packageValue'           :'Red',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Red'
                                           },

            'development'               : {'packageVariable'        :'Red',
                                           'packageValue'           :'Red',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Red'
                                           },

            'stage'                     : {'packageVariable'        :'Red',
                                           'packageValue'           :'Red',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Red'
                                           },

            'project-internal'          : {'packageVariable'        :'Green',
                                           'packageValue'           :'Green',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Green'
                                           },

            'project-external'          : {'packageVariable'        :'Green',
                                           'packageValue'           :'Green',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Green'
                                           },

            'master-project-internal'   : {'packageVariable'        :'Green',
                                           'packageValue'           :'Green',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Green'
                                           },

            'master-project-external'   : {'packageVariable'        :'Green',
                                           'packageValue'           :'Green',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'Cyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'Cyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Green'
                                           },

            'post-build'                : {'packageVariable'        :'Blue',
                                           'packageValue'           :'DarkCyan',

                                           'multiVariable'          :'Blue',
                                           'multiValue'             :'DarkCyan',

                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',

                                           'script'                 :'Magenta',
                                           'command'                :'Magenta',

                                           'colon'                  :'Blue',
                                           'arrow'                  :'Blue'
                                           },

            'env'                       : {'colon'                  :'Blue',
                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',
                                           },

            'info'                      : {'colon'                  :'Blue',
                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',
                                           },

            'product-info'              : {'colon'                  :'Blue',
                                           'singleVariable'         :'Blue',
                                           'singleValue'            :'DarkCyan',
                                           },

        }
