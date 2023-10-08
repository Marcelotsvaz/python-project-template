'''
Create shields.io URLs.

https://shields.io/
'''



from urllib.parse import urlencode, quote



badges = [
	# First line.
	{
		'badgeType': 'gitlab/pipeline-status',
		'mainArgument': 'marcelotsvaz/python-project-template',
		'title': 'Gitlab pipeline status',
		'target': 'https://gitlab.com/marcelotsvaz/python-project-template/-/pipelines/latest',
		
		'logo': 'gitlab',
		'label': 'Build',
	},
	{
		'badgeType': 'gitlab/pipeline-coverage',
		'mainArgument': 'marcelotsvaz/python-project-template',
		'title': 'Code coverage',
		'target': 'https://gitlab.com/marcelotsvaz/python-project-template/-/pipelines/latest',
		
		'branch': 'main',
		'label': 'Coverage',
	},
	{
		'badgeType': 'gitlab/v/release',
		'mainArgument': 'marcelotsvaz/python-project-template',
		'title': 'GitLab release',
		'target': 'https://gitlab.com/marcelotsvaz/python-project-template/-/releases/permalink/latest',
		
		'logo': 'gitlab',
		'label': 'Release',
	},
	{
		'badgeType': 'pypi/v',
		'mainArgument': 'marcelotsvaz-python-project-template',
		'title': 'PyPI package',
		'target': 'https://pypi.org/project/marcelotsvaz-python-project-template/',
		
		'logo': 'python',
		'logoColor': '#CCCCCC',
		'label': 'PyPI',
	},
	
	# Second line.
	{
		'badgeType': 'badge',
		'mainArgument': 'sphinx-grey',
		'title': 'Documented with Sphinx',
		'target': 'https://marcelotsvaz.gitlab.io/python-project-template',
		
		'logo': 'sphinx',
	},
	{
		'badgeType': 'badge',
		'mainArgument': 'pdm-managed-blueviolet',
		'title': 'Managed with PDM',
		'target': 'https://pdm.fming.dev',
	},
	{
		'badgeType': 'badge',
		'mainArgument': 'Renovate-grey',
		'title': 'Renovate',
		'target': 'https://github.com/renovatebot/renovate',
		
		'logo': 'renovatebot',
		'logoColor': '#007fa0',
	},
	{
		'badgeType': 'badge',
		'mainArgument': 'Unlicense-grey',
		'title': 'Unlicense',
		'target': 'https://choosealicense.com/licenses/unlicense/',
		
		'logo': 'unlicense',
	},
	{
		'badgeType': 'badge',
		'mainArgument': 'Visual Studio Code-grey',
		'title': 'Visual Studio Code',
		'target': 'https://code.visualstudio.com/',
		
		'logo': 'visual-studio-code',
		'logoColor': '#0066b8',
	},
]



def makeBadge(
	badgeType: str,
	mainArgument: str,
	title: str | None = None,
	target: str | None = None,
	**optionalArguments: str,
) -> str:
	'''
	Create shields.io URL from parameters.
	'''
	
	baseUrl = 'https://img.shields.io'
	
	mainArgument = quote( mainArgument, safe = '' )
	urlArguments = '?' + urlencode( optionalArguments ) if optionalArguments else ''
	
	url = f'{baseUrl}/{badgeType}/{mainArgument}{urlArguments}'
	markdown = f'![{title}]({url})'
	
	if target:
		markdown = f'[{markdown}]({target})'
	
	return markdown



if __name__ == '__main__':
	for badgeDef in badges:
		badge = makeBadge( **badgeDef )
		print( badge )