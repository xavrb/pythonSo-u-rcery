# -*- coding: utf-8 -*-
import json
import sys 
#unicodes = "Klüft skräms inför på fédéral électoral große"



unicodes = sys.argv[1]
escapech = str(json.dump(unicodes, sys.stdout))
print(escapech)


