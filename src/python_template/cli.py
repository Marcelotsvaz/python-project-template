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
	testParser = subparsers.add_parser( 'test', help = test.__doc__ )
	testParser.add_argument( 'message', help = 'Message that will be displayed.' )
	testParser.set_defaults( action = test )
	
	# Run.
	args = parser.parse_args()
	args.action( **vars( args ) )



# 
# Actions.
#-------------------------------------------------------------------------------
def test( message: str, **kwargs: Any ) -> None:
	'''
	TODO CLI command docstring.
	'''
	
	myClass = MyClass()
	myClass.print( message )