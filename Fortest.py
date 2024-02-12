#!/usr/bin/env python3

Birds = ["blackbird" "seagull" "raptor"]

Reality = ["real!"]

for birds in Birds:
    print("Birds ", end="")

    if birds not in Reality: 
        print("Birds aren\t" + Reality)
