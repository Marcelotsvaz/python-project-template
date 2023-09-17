'''
PDM build hooks.
'''

from pathlib import Path

from pdm.backend.hooks import Context



def pdm_build_clean( context: Context ) -> None:	# pylint: disable = invalid-name
	'''
	Change default directories at start of build.
	'''
	
	context.build_dir = Path( '.staging/build/' ).resolve()
	# context.dist_dir = Path( '.staging/dist' ).resolve()
	
	# context.dist_dir.mkdir( parents = True, exist_ok = True )