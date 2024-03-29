# Color and Style Constants
BlackD = "\033[0;30m"
BlackB = "\033[1;30m"
BlackL = "\033[2;30m"
BlackI = "\033[3;30m"
BlackU = "\033[4;30m"
BlackS = "\033[9;30m"

RedD = "\033[0;31m"
RedB = "\033[1;31m"
RedL = "\033[2;31m"
RedI = "\033[3;31m"
RedU = "\033[4;31m"
RedS = "\033[9;31m"

GreenD = "\033[0;32m"
GreenB = "\033[1;32m"
GreenL = "\033[2;32m"
GreenI = "\033[3;32m"
GreenU = "\033[4;32m"
GreenS = "\033[9;32m"

YellowD = "\033[0;33m"
YellowB = "\033[1;33m"
YellowL = "\033[2;33m"
YellowI = "\033[3;33m"
YellowU = "\033[4;33m"
YellowS = "\033[9;33m"

BlueD = "\033[0;34m"
BlueB = "\033[1;34m"
BlueL = "\033[2;34m"
BlueI = "\033[3;34m"
BlueU = "\033[4;34m"
BlueS = "\033[9;34m"

MagentaD = "\033[0;35m"
MagentaB = "\033[1;35m"
MagentaL = "\033[2;35m"
MagentaI = "\033[3;35m"
MagentaU = "\033[4;35m"
MagentaS = "\033[9;35m"

CyanD = "\033[0;36m"
CyanB = "\033[1;36m"
CyanL = "\033[2;36m"
CyanI = "\033[3;36m"
CyanU = "\033[4;36m"
CyanS = "\033[9;36m"

GreyD = "\033[0;90m"
GreyB = "\033[1;90m"
GreyL = "\033[2;90m"
GreyI = "\033[3;90m"
GreyU = "\033[4;90m"
GreyS = "\033[9;90m"

WhiteB = "\033[0;1m"
WhiteL = "\033[0;2m"
WhiteI = "\033[0;3m"
WhiteU = "\033[0;4m"
WhiteS = "\033[0;8m"

# Background Constants
BlackBg = "\033[7;30m"
RedBg = "\033[7;31m"
GreenBg = "\033[7;32m"
YellowBg = "\033[7;33m"
BlueBg = "\033[7;34m"
MagentaBg = "\033[7;35m"
CyanBg = "\033[7;36m"
WhiteBg = "\033[7;37m"
GreyBg = "\033[7;90m"

# Reset and Invisible Constants
RESET = "\033[0;0m"
INVISIBLE = "\033[0;8m"

print(RedB + "Hello" + GreenB + " World!", end="")

print(RESET,end="")