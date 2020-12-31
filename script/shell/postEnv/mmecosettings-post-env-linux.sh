#!/usr/bin/env bash
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
## @file mMecoSetting/script/shell/postEnv/mmecosettings-post-env-linux.sh @brief [ FILE ] - Shell script file.


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
function _mMecoPostEnvLinuxGetCurrentGitBranch()
{
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ \1/';
}

function _mMecoPostEnvLinuxMain()
{
    # ╔═
    PS1="\n\[\e[37m\]╔═";

    # user @ host
    PS1=$PS1"\[\e[35m\] [ \u @ \h ] ";

    # date - time
    PS1=$PS1"[ \d - \t ] ";

    #

    local developmentOrStageState="";
    local developmentOrStageEnvName="";

    local development="$MECO_DEVELOPMENT_ENV_NAME";
    local stage="$MECO_STAGE_ENV_NAME";

    if [[ "$development" ]]; then
        developmentOrStageState="development";
        developmentOrStageEnvName="$development";
    elif [[ "$stage" ]]; then
        developmentOrStageState="stage";
        developmentOrStageEnvName="$stage";
    fi

    local envName="";
    if [[ "$MECO_ENV_NAME" ]]; then
        envName="- $MECO_ENV_NAME ";
    fi

    # Project start
    PS1=$PS1"\[\e[31m\][ $MECO_PROJECT_NAME ";

    # Development or stage
    if [[ "$developmentOrStageState" ]]; then
        PS1=$PS1"- $MECO_DEVELOPER_NAME/$developmentOrStageState/$developmentOrStageEnvName $envName";
    else
        PS1=$PS1"$envName";
    fi

    # Project end
    PS1=$PS1"] "

    #

    # Current working directory
    PS1=$PS1"\[\033[38;5;7m\]\n╠═ \[\e[34m\]\w";

    # ╠═ git branch
    local gitBranch=$(_mMecoPostEnvLinuxGetCurrentGitBranch)
    if [[ "$gitBranch" ]]; then
        PS1=$PS1"\n\[\e[37m\]╠═\[\e[31m\]$gitBranch";
    fi

    # ╚═ Command prompt
    PS1=$PS1"\n\[\e[37m\]╚═ \[\e[37m\]";

    export PS1
}
_mMecoPostEnvLinuxMain
PROMPT_COMMAND=_mMecoPostEnvLinuxMain

#printf "\nPost env script has been executed.\n"

