'''
Expose functions as CLI commands.
'''



import argparse

from typing import Any

from python_template.core import MyClass



def main() -> None:
	'''
	CLI entry point.
	'''
	
	# Parser init.
	parser = argparse.ArgumentParser(
		description = 'TODO',
		add_help = False,
	)
	subparsers = parser.add_subparsers( title = 'action' )
	
	parser.set_defaults( action = lambda **_: parser.print_usage() )
	parser.add_argument( '-h', '--help', action = 'help', help = 'Show this help message.' )
	parser.add_argument(
		'--version',
		action = 'version',
		version = f'{parser.prog} 1.0.0',
		help = 'Show program\'s version number.',
	)
	
	# Actions.
	invertParser = subparsers.add_parser( 'invert', help = invert.__doc__ )
	invertParser.add_argument( 'message', help = 'Message that will be displayed.' )
	invertParser.set_defaults( action = invert )
	
	# Run.
	args = parser.parse_args()
	args.action( **vars( args ) )



# 
# Actions.
#-------------------------------------------------------------------------------
def invert( message: str, **_kwargs: Any ) -> None:
	'''
	TODO CLI command docstring.
	'''
	
	inverted = MyClass.invertCase( message )
	print( inverted )