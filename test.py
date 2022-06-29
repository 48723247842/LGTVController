#!/usr/bin/env python3
from pprint import pprint
import yaml # pip install pyyaml

from LGTVController import LGTVController

def read_yaml( file_path ):
    with open( file_path ) as f:
        return yaml.safe_load( f )

if __name__ == "__main__":
	personal = read_yaml( "./personal.yaml" )
	x = LGTVController( personal )
	pprint( x.get_current_app() )
	pprint( x.power_off() )