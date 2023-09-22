'''
Expose functions as CLI commands.
'''

import argparse
from importlib.metadata import version
from typing import Any

from python_template.core import MyClass



def main() -> int:
	'''
	CLI entry point.
	'''
	
	# Parser setup.
	parser = argparse.ArgumentParser(
		description = 'TODO',
		add_help = False,
	)
	subparsers = parser.add_subparsers( title = 'command' )
	
	parser.set_defaults( command = lambda **_: parser.print_usage() )
	parser.add_argument( '-h', '--help', action = 'help', help = 'Show this help message.' )
	parser.add_argument(
		'--version',
		action = 'version',
		version = f'{parser.prog} {version( __package__ )}',
		help = 'Show program\'s version number.',
	)
	
	# Commands.
	invertParser = subparsers.add_parser( 'invert', help = invert.__doc__ )
	invertParser.add_argument( 'message', help = 'Message that will be displayed.' )
	invertParser.set_defaults( command = invert )
	
	# Run.
	args = parser.parse_args()
	
	return args.command( **vars( args ) )



# 
# Commands.
#-------------------------------------------------------------------------------
def invert( message: str, **_kwargs: Any ) -> int:
	'''
	TODO CLI command docstring.
	'''
	
	inverted = MyClass.invertCase( message )
	print( inverted )
	
	return 0