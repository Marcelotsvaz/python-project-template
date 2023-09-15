'''
How to ignore linting errors.
'''

invalidType: int = 1.0	# pyright: ignore [reportGeneralTypeIssues]

invalidName1 = 123	# pylint: disable = invalid-name

# pylint: disable-next = invalid-name
invalidName2 = 234