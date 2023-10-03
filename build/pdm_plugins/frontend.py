'''
TODO
'''

from pdm.cli.commands.base import BaseCommand
from pdm.core import Core



def example_plugin( core: Core ):
	'''
	TODO
	'''
	
	core.register_command( HelloCommand, 'hello' )



class HelloCommand( BaseCommand ):
	'''
	TODO
	'''
	
	def handle( self, project, options ):
		print( 'Hello world!' )