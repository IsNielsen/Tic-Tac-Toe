#!/usr/bin/python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


#    ___   ____  ______
#   / _ | /  _/ /_  __/__ ___ ___ _
#  / __ |_/ /    / / / -_) _ `/  ' \
# /_/ |_/___/   /_/  \__/\_,_/_/_/_/


from interface import *
from engine import *
from ai import *

if __name__ == '__main__':
    while True:
        logo()
        mode = player_select()
        if mode == 0:
            cpu_vs_cpu(strategy_oracle, strategy_oracle)
        elif mode == 1:
            human_vs_cpu(strategy_oracle)
        elif mode == 2:
            cpu_vs_human(strategy_oracle)
        elif mode == 3:
            human_vs_human()
        elif mode == 4:
            game(strategy_oracle, strategy_oracle)
        else:
            break
    print("Thanks for playing!")
