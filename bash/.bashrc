# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions

function start_server
{
    export FLASK_APP=$1
    python -m flask run
}
