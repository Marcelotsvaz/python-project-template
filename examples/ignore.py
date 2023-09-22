'''
How to ignore linting errors.
'''

# Pyright.
invalidType: int = 'foo'	# pyright: ignore [reportGeneralTypeIssues]



# Pylint.
invalidName = 'foo'	# pylint: disable = invalid-name
# pylint: disable-next = f-string-without-interpolation, inconsistent-quotes
inconsistentQuotes = f"foo"