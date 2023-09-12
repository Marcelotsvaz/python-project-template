'''
TODO Module docstring.
'''



class MyClass:
	'''
	TODO Class docstring.
	'''
	
	@classmethod
	def invertCase( cls, text: str ) -> str:
		'''
		TODO Method docstring.
		'''
		
		invertedText: list[str] = []
		
		for letter in text:
			if letter.isupper():
				invertedText.append( letter.lower() )
			else:
				invertedText.append( letter.upper() )
		
		return ''.join( invertedText )