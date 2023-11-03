---
icon: material/file-document
---
Documentation with MkDocs.



## Tables
| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |



## Code Blocks
[Material for MkDocs documentation for code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)

### Configuration
``` yaml title='mkdocs.yaml'
theme:
    features:
      - content.code.copy # Copy button.

markdown_extensions:
  - pymdownx.superfences: # Fenced code block, highlighting and block title.
        preserve_tabs: true
        disable_indented_code_blocks: true
  - pymdownx.highlight: # Enabled by default with SuperFences.
        anchor_linenums: true
        linenums_style: pymdownx-inline
        pygments_lang_class: true
  - pymdownx.inlinehilite # Inline highlighting.
```

### Examples
Inline syntax highlighting: `#!python print( 'foo' )`

``` python
print( 'foo' )
```

``` python title='With Title'
print( 'foo' )
```

``` python title='With Line Numbers and Line Selection' linenums='1' hl_lines='2-4'
class Foo
	'''
	Docstring.
	'''
	
	def bar( self, value: str ) -> None:
		print( value )
```

``` python title='Embedded File'
----8<---- 'include/example.py'
```



## Admonitions
[Material for MkDocs documentation for admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

### Configuration
``` yaml title='mkdocs.yaml'
markdown_extensions:
  - admonition
  - pymdownx.details # Collapsible admonitions.
```

### Examples
!!! example
	Lorem ipsum dolor sit amet.

!!! example "Custom Title"
	Lorem ipsum dolor sit amet.

??? example "Collapsible"
	Lorem ipsum dolor sit amet.

???+ example "Collapsible (Pre-Expanded)"
	Lorem ipsum dolor sit amet.

!!! example inline "Custom Title"
	Lorem ipsum dolor sit amet.

!!! example "Custom Title"
	Lorem ipsum dolor sit amet.


### Types
!!! abstract
!!! bug
!!! danger
!!! example
!!! failure
!!! info
!!! note
!!! question
!!! quote
!!! success
!!! tip
!!! warning



## Annotations
[Material for MkDocs documentation for annotations](https://squidfunk.github.io/mkdocs-material/reference/annotations/)

### Configuration
``` yaml title='mkdocs.yaml'
theme:
    features:
      - content.code.annotate # Inside code blocks.

markdown_extensions:
  - pymdownx.superfences
  - attr_list # Outside code blocks.
```

### Examples
``` python
print( 'foo' ) # Some comment.(1)
print( 'foo' )# (2)!
```

1. Put `(1)` inside a comment.
1. Use `(1)!` to delete the comment.

Use `{ .annotate }` to add annotations (1) anywhere.
{ .annotate }

1. Lorem ipsum dolor sit amet.



## Task Lists

### Configuration
``` yaml title='mkdocs.yaml'
markdown_extensions:
  - pymdownx.tasklist:
        custom_checkbox: true
```

### Examples
- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
	* [x] In hac habitasse platea dictumst
	* [x] In scelerisque nibh non dolor mollis congue sed et metus
	* [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque



## Tabs

### Configuration
``` yaml title='mkdocs.yaml'
theme:
    features:
      - content.tabs.link

markdown_extensions:
  - pymdownx.superfences
  - pymdownx.tabbed:
        alternate_style: true
```

### Examples
=== "C"
	``` c
	#include <stdio.h>
	
	int main()
	{
		printf( "Hello world!\n" );
		
		return 0;
	}
	```

=== "C++"
	``` c++
	#include <iostream>
	
	int main()
	{
		std::cout << "Hello world!" << std::endl;
		
		return 0;
	}
	```



## Tooltips

### Configuration
``` yaml title='mkdocs.yaml'
markdown_extensions:
  - attr_list
```

### Examples
Foo :material-information-outline:{ title='Important information' }



## Abbreviations

### Configuration
``` yaml title='mkdocs.yaml'
markdown_extensions:
  - abbr
  - pymdownx.snippets:
        auto_append: [ include/abbreviations.md ]
```

### Examples
The HTML specification is maintained by the W3C.



## SuperFences

### Configuration
``` yaml title='mkdocs.yaml'
markdown_extensions:
  - pymdownx.superfences
```

### Examples
!!! example
	Lorem ipsum dolor sit amet.
	
	```python title='Nested Block'
	print( 'foo' )
	```