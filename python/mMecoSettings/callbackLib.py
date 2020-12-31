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
## @file    mMecoSettings/callbackLib.py @brief [ FILE   ] - Callback module.
## @package mMecoSettings.callbackLib    @brief [ MODULE ] - Callback module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os
import  sys
import  json
import  argparse

from    importlib import import_module

import  mMeco.libs.aboutLib

import  mMecoSettings.envVariablesLib
import  mMecoSettings.settingsLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief This function is invoked before packages are collected and environment is resolved.
#
#  @param allLib                [ mMeco.libs.allLib.All                    | None | in  ] - All libraries.
#  @param envEntryContainer     [ mMeco.libs.entryLib.EnvEntryContainer    | None | in  ] - Env entry container.
#
#  @exception N/A
#
#  @return None - None.
def getPreBuild(allLib, envEntryContainer):
    
    envPreScriptPath = None

    if allLib.request().platform() == 'Linux':

        envPreScriptPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'script', 'shell', 'preEnv', 'meco-env-pre-linux.sh'))

    elif allLib.request().platform() == 'Darwin':

        envPreScriptPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'script', 'shell', 'preEnv', 'mmecosettings-pre-env-darwin.sh'))

    elif allLib.request().platform() == 'Windows':

        envPreScriptPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'script', 'powershell', 'preEnv', 'mmecosettings-pre-env-windows.ps1'))

    if envPreScriptPath and not os.path.isfile(envPreScriptPath):
        raise IOError('Pre script doesn\'t exist: {}'.format(envPreScriptPath))

    envEntryContainer.addScript(envPreScriptPath)

    #

    envEntryContainer.addSingle('CUSTOM_ENV_NAME', 'CUSTOM_ENV_VALUE')

    # envEntryContainer.addSingle('POST_CUSTOM_SINGLE_ENV_NAME', 'POST_CUSTOM_SINGLE_ENV_NAME')
    #
    # envEntryContainer.addMulti('POST_CUSTOM_MULTI_ENV_NAME', 'POST_CUSTOM_MULTI_ENV_NAME1')
    # envEntryContainer.addMulti('POST_CUSTOM_MULTI_ENV_NAME', 'POST_CUSTOM_MULTI_ENV_NAME2')
    #
    # envEntryContainer.addScript('/POST/script.sh')
    # envEntryContainer.addCommand('echo post')

    envEntryContainer.sort()

#
## @brief This function is invoked after packages are collected and environment is resolved.
#
#  @param allLib                [ mMeco.libs.allLib.All                    | None | in  ] - All libraries.
#  @param envEntryContainer     [ mMeco.libs.entryLib.EnvEntryContainer    | None | in  ] - Env entry container.
#
#  @exception N/A
#
#  @return None - None.
def getPostBuild(allLib, envEntryContainer):

    envPostScriptPath = None

    if allLib.request().platform() == 'Linux':

        envPostScriptPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'script', 'shell', 'postEnv', 'mmecosettings-post-env-linux.sh'))

    elif allLib.request().platform() == 'Darwin':

        envPostScriptPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'script', 'shell', 'postEnv', 'mmecosettings-post-env-darwin.sh'))

    elif allLib.request().platform() == 'Windows':

        envPostScriptPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'script', 'powershell', 'postEnv', 'mmecosettings-post-env-windows.ps1'))

    if envPostScriptPath and not os.path.isfile(envPostScriptPath):
        raise IOError('Post script doesn\'t exist: {}'.format(envPostScriptPath))

    envEntryContainer.addScript(envPostScriptPath)

    #

    #
    # CUSTOM ARGUMENTS
    argumentParser = argparse.ArgumentParser()

    if allLib.request().platform() == 'Windows':
        argumentParser.add_argument('-custom-flag', action='store_true', default=False)
    else:
        argumentParser.add_argument('--custom-flag', action='store_true', default=False)

    knownArgs, unknownArgs = argumentParser.parse_known_args(allLib.request().unknownArgs())
    customFlag = knownArgs.custom_flag


    #

    # MECO
    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_ES_VERSION,
                           mMeco.libs.aboutLib.getVersion())

    if allLib.request().platform() == 'Windows':
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_ES_COMMAND,
                               '{}'.format(allLib.request().command()))
    else:
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_ES_COMMAND,
                       '"\'{}\'"'.format(allLib.request().command()))


    # PYTHON
    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_PYTHON_EXECUTABLE_PATH,
                           sys.executable)

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_PYTHON_VERSION,
                           allLib.request().pythonVersion())


    # DEVELOPER
    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_DEVELOPER_NAME,
                           allLib.request().developer())


    # RESERVED
    if allLib.settingsOperator().reservedPackagesPath():

        # Reserved name
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_RESERVED_ENV_NAME,
                               mMecoSettings.settingsLib.RESERVED_ENV_NAME)

        # Reserved packages path
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_RESERVED_PACKAGES_PATH,
                               mMecoSettings.settingsLib.getReservedPackagesPath(allLib.request().developer(),
                                                                                 allLib.request().platform()
                                                                                 ))

    else:
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_RESERVED_ENV_NAME, '')

        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_RESERVED_PACKAGES_PATH, '')


    # DEVELOPMENT
    if allLib.request().development():

        # Env name
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_ENV_NAME,
                               allLib.request().development())

        # Env packages path
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_PACKAGES_PATH,
                               mMecoSettings.settingsLib.getDevelopmentPackagesPath(allLib.settingsOperator().projectNameInUse(),
                                                                                    allLib.request().developer(),
                                                                                    allLib.request().development(),
                                                                                    allLib.request().platform()
                                                                                    ))

    else:
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_ENV_NAME, '')

        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_PACKAGES_PATH, '')


    # STAGE
    if allLib.request().stage():

        # Env name
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_STAGE_ENV_NAME,
                               allLib.request().stage())

        # Env packages path
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_STAGE_PACKAGES_PATH,
                               mMecoSettings.settingsLib.getStagePackagesPath(allLib.settingsOperator().projectNameInUse(),
                                                                              allLib.request().developer(),
                                                                              allLib.request().stage(),
                                                                              allLib.request().platform()
                                                                              ))

    else:
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_STAGE_ENV_NAME, '')

        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_STAGE_PACKAGES_PATH, '')


    # PROJECT
    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_PROJECT_NAME,
                           allLib.settingsOperator().projectNameInUse())

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_PROJECT_INTERNAL_PACKAGES_PATH,
                           mMecoSettings.settingsLib.getProjectInternalPackagesPath(allLib.settingsOperator().projectNameInUse(),
                                                                                    allLib.request().platform()))

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_PROJECT_EXTERNAL_PACKAGES_PATH,
                           mMecoSettings.settingsLib.getProjectExternalPackagesPath(allLib.settingsOperator().projectNameInUse(),
                                                                                    allLib.request().platform()))

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_PROJECT_PATH,
                           mMecoSettings.settingsLib.getProjectsPath(allLib.request().platform(),
                                                                     allLib.settingsOperator().projectNameInUse()))

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_PROJECT_ROOT_PATH,
                           mMecoSettings.settingsLib.getProjectRootPath(allLib.request().platform(),
                                                                        allLib.settingsOperator().projectNameInUse()))

    #

    if allLib.settingsOperator().scriptFilePath():
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_ENV_SCRIPT_FILE_PATH,
                               allLib.settingsOperator().scriptFilePath())
    else:
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_ENV_SCRIPT_FILE_PATH,
                               '')


    # MASTER PROJECT
    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_MASTER_PROJECT_NAME,
                           mMecoSettings.settingsLib.MASTER_PROJECT_NAME)


    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_MASTER_PROJECT_INTERNAL_PACKAGES_PATH,
                           mMecoSettings.settingsLib.getProjectInternalPackagesPath(mMecoSettings.settingsLib.MASTER_PROJECT_NAME,
                                                                                    allLib.request().platform()))

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_MASTER_PROJECT_EXTERNAL_PACKAGES_PATH,
                           mMecoSettings.settingsLib.getProjectExternalPackagesPath(mMecoSettings.settingsLib.MASTER_PROJECT_NAME,
                                                                                    allLib.request().platform()))

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_MASTER_PROJECT_PATH,
                           mMecoSettings.settingsLib.getProjectsPath(allLib.request().platform()))

    envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_MASTER_PROJECT_ROOT_PATH,
                           mMecoSettings.settingsLib.getProjectRootPath(allLib.request().platform()))


    # ENV
    MECO_USE_PROJECT_ENVS_ONLY = os.environ.get(mMecoSettings.settingsLib.MECO_USE_PROJECT_APPS_ONLY,
                                                '0' if allLib.request().platform() == 'Windows' else '"0"'
                                                )
    envEntryContainer.addSingle(mMecoSettings.settingsLib.MECO_USE_PROJECT_APPS_ONLY,
                           MECO_USE_PROJECT_ENVS_ONLY)

    if allLib.settingsOperator().appFilePath():

        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_APP_NAME, allLib.request().app())

        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_APP_PATH, allLib.settingsOperator().appFilePath())

        #

        envFile = open(allLib.settingsOperator().appFilePath(), 'r')
        envData = json.loads(envFile.read())
        envFile.close()

        if envData['application'] == 'houdini':

            pass

        elif envData['application'] == 'katana':

            pass

        elif envData['application'] == 'mari':

            pass

        elif envData['application'] == 'maya':

            pass

        elif envData['application'] == 'nuke':

            pass

    else:

        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_APP_NAME, '')
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_APP_PATH, '')


    if allLib.settingsOperator().logFilePath():
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_ENV_LOG_FILE_PATH,
                               allLib.settingsOperator().logFilePath())
    else:
        envEntryContainer.addSingle(mMecoSettings.envVariablesLib.MECO_ENV_LOG_FILE_PATH,
                               '')

    # CHANGE DIRECTORY
    if allLib.settingsOperator().developmentPackagesPath():
        if allLib.request().platform() == 'Windows':
            envEntryContainer.addCommand('cd $env:{};'.format(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_PACKAGES_PATH))
        else:
            envEntryContainer.addCommand('cd "${}";'.format(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_PACKAGES_PATH))

    if allLib.settingsOperator().stagePackagesPath():
        if allLib.request().platform() == 'Windows':
            envEntryContainer.addCommand('cd $env:{};'.format(mMecoSettings.envVariablesLib.MECO_STAGE_PACKAGES_PATH))
        else:
            envEntryContainer.addCommand('cd "${}";'.format(mMecoSettings.envVariablesLib.MECO_STAGE_PACKAGES_PATH))


    envEntryContainer.sort()

#
## @brief This function provides additional flags for given app executable.
#
#  @param allLib [ mMeco.libs.allLib.All | None | in  ] - All libraries.
#
#  @exception N/A
#
#  @return str  - Additional app executable flags.
#  @return None - If not additional app executable flags are available.
def getAppExecutableFlags(allLib):

    if not allLib.settingsOperator().appFilePath():
        return None

    _appFile = open(allLib.settingsOperator().appFilePath(), 'r')
    appData  = json.loads(_appFile.read())
    _appFile.close()

    if not 'application' in appData:
        return None

    editors = ['atom',
               'brackets',
               'charm',
               'code',
               'coda',
               'coffecup',
               'jedit',
               'kate',
               'komodo',
               'notepad',
               'notepadpp',
               'pycharm',
               'sublime',
               'textwrangler',
               'wingide']

    if allLib.request().platform() == 'Windows':

        if appData['application'] in editors:

            if allLib.request().development():
                return '$env:{}'.format(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_PACKAGES_PATH)

    else:

        if appData['application'] in editors:

            if allLib.request().development():
                return '"${}"'.format(mMecoSettings.envVariablesLib.MECO_DEVELOPMENT_PACKAGES_PATH)

    return None

#
## @brief This function determines whether given package should be initialized.
#
#  @param allLib         [ mMeco.libs.allLib.All | None | in  ] - All libraries.
#  @param packagePath    [ str                   | None | in  ] - Absolute path of the root of a package.
#
#  @exception N/A
#
#  @return bool - `True` if the package should be initialized, `False` otherwise.
def shouldInitializePackage(allLib, packagePath):

    if not hasattr(sys, 'argv'):
        sys.argv  = ['']

    #

    packageName               = os.path.basename(packagePath)
    packagePythonPath         = os.path.join(packagePath, 'python')
    packageInfoModuleFilePath = os.path.join(packagePath, 'python', packageName, 'packageInfoLib.py')

    if not os.path.isdir(packagePythonPath) or not  os.path.isfile(packageInfoModuleFilePath):
        return False

    #

    packageInfoModuleStr = '{}.packageInfoLib'.format(os.path.basename(packagePath))
    packageInfoModule    = None
    pathAdded            = False

    if not packagePythonPath in sys.path:
        sys.path.insert(0, packagePythonPath)
        pathAdded = True

    try:
        packageInfoModule = import_module(packageInfoModuleStr)

        # Do not initialize this package if it is not active
        if hasattr(packageInfoModule, 'IS_ACTIVE'):
            if not getattr(packageInfoModule, 'IS_ACTIVE'):
                return False

        # Do not initialize this package if current platform is not supported
        if hasattr(packageInfoModule, 'PLATFORMS'):
            if not allLib.request().platform() in getattr(packageInfoModule, 'PLATFORMS'):
                return False

        # Do not initialize this package if current Python version is not supported by it
        if hasattr(packageInfoModule, 'PYTHON_VERSIONS'):

            packagePythonVersions = getattr(packageInfoModule, 'PYTHON_VERSIONS')

            # Check major version of Python in use
            # More specific check can be made here to determine whether the package should be initialize
            # based on Python version
            if packagePythonVersions:
                pythonMajorVersion = allLib.request().pythonVersion().split('.')[0]
                if not pythonMajorVersion in packagePythonVersions:
                    return False

    except Exception as error:
        allLib.logger().addFailure(str(error))
        return False


    for module in ['packageInfoLib', packageName, packageInfoModuleStr]:
        if module in sys.modules:
            del sys.modules[module]

    if pathAdded:
        del sys.path[0]


    #
    #
    #
    # IGNORE PACKAGE by APP
    #
    packageApplications = []
    if hasattr(packageInfoModule, 'APPLICATIONS'):
        packageApplications = getattr(packageInfoModule, 'APPLICATIONS')

    if not packageApplications:
        return True

    # Package should be initialized for all applications
    if 'all' in packageApplications:
        return True

    appFileApplication = None
    if allLib.settingsOperator().appFilePath():
        # Application provided by the user so get the name of it
        _appFile = open(allLib.settingsOperator().appFilePath(), 'r')
        appData  = json.loads(_appFile.read())
        _appFile.close()
        if 'application' in appData:
            appFileApplication = appData['application']

    if not appFileApplication:
        # Application is not provided by the user
        # The environment is run in command line
        # Meaning that its standalone
        appFileApplication = 'standalone'

    # Provided application is not in the package applications
    # Therefore this package shouldn't be initialized
    if not appFileApplication in packageApplications:
        return False

    return True

