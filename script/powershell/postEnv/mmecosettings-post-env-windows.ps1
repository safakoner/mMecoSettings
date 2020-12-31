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
## @file mMecoSettings/script/powershell/postEnv/mmecosettings-post-env-windows.ps1 [ FILE ] - PowerShell script file.


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
function global:prompt
{

    #
    Write-Host "`n$([char]0x2554)$([char]0x2550) " -nonewline -Foregroundcolor White

    # user @ host
    Write-Host "[ $env:UserName @ $env:ComputerName ]" -nonewline -Foregroundcolor Magenta

    # date - time
    Write-Host " [ $(get-date) ]" -nonewline -Foregroundcolor Magenta

    #

    $developmentOrStageState = ""
    $developmentOrStageEnvName = ""

    $development=$env:MECO_DEVELOPMENT_ENV_NAME
    $stage=$env:MECO_STAGE_ENV_NAME

    if($development)
    {
        $developmentOrStageState = "development"
        $developmentOrStageEnvName = $development
    }
    elseif($stage)
    {
        $developmentOrStageState = "stage"
        $developmentOrStageEnvName = $stage
    }

    # Project start
    $projectPrompt = " [ $env:MECO_PROJECT_NAME"

    # Development or stage
    if($developmentOrStageState)
    {
        $projectPrompt += " - $env:MECO_DEVELOPER_NAME/$developmentOrStageState/$developmentOrStageEnvName";
    }

    if($env:MECO_APP_NAME)
    {
        $projectPrompt += " - $env:MECO_APP_NAME"
    }

    # Project end
    $projectPrompt += " ]"

    Write-Host $projectPrompt -Foregroundcolor Red

    #

    # Current working directory
    Write-Host "$([char]0x2560)$([char]0x2550) " -nonewline -Foregroundcolor White

    if(Get-Command git -errorAction SilentlyContinue)
    {
        # ╠═ Git Branch
        $gitBranch = git branch --show-current
        if($gitBranch)
        {
            Write-Host $(pwd) -Foregroundcolor Blue
            Write-Host "$([char]0x2560)$([char]0x2550) " -nonewline -Foregroundcolor White
            Write-Host $gitBranch -nonewline -Foregroundcolor Red
        }
        else
        {
            Write-Host $(pwd) -nonewline -Foregroundcolor Blue
        }
    }
    else
    {
        Write-Host $(pwd) -nonewline -Foregroundcolor Blue
    }

    # ╚═ Command prompt
    Write-Host "`n$([char]0x255A)$([char]0x2550)" -nonewline -Foregroundcolor White

    return " "
}
