'''
Unit tests for `project_template.core`.
'''

from unittest import TestCase

from project_template.core import MyClass



class MyClassTests( TestCase ):
	def testInvertCaseLower( self ) -> None:
		text = MyClass.invertCase( 'hello world' )
		
		self.assertEqual( text, 'HELLO WORLD' )
	
	def testInvertCaseUpper( self ) -> None:
		text = MyClass.invertCase( 'HELLO WORLD' )
		
		self.assertEqual( text, 'hello world' )
	
	def testInvertCaseMixed( self ) -> None:
		text = MyClass.invertCase( 'HelLo WoRld' )
		
		self.assertEqual( text, 'hELlO wOrLD' )