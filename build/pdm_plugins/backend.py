'''
PDM-Backend hooks.
'''

from pathlib import Path

from pdm.backend.hooks import Context



class Hooks:
	'''
	PDM-Backend hooks.
	'''
	
	def pdm_build_clean( self, context: Context ) -> None:	# pylint: disable = invalid-name
		'''
		Change default build directory before start of build.
		'''
		
		context.build_dir = Path( '.staging/build/' )
		# context.dist_dir = Path( '.staging/dist/' )
		# context.dist_dir.mkdir( parents = True, exist_ok = True )