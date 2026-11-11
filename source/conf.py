# Configuration file for the Sphinx documentation builder.

# Monkey patch shibuya to use available pygments styles
import shibuya._pygments
# Override shibuya's default styles with available ones
shibuya._pygments.ShibuyaPygmentsBridge.light_style_name = "default"
shibuya._pygments.ShibuyaPygmentsBridge.dark_style_name = "github-dark"

# -- Project information

project = 'mcprack'
copyright = '2026, VitexSoftware'
author = 'Vitex'

release = '1.7.0'
version = '1.7.0'

# -- General configuration

extensions = [
    'shibuya',
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

todo_include_todos = True
todo_emit_warnings = True

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []

# -- Options for HTML output

html_theme = "shibuya"
pygments_style = "default"
pygments_dark_style = "github-dark"

html_theme_options = {
    "github_url": "https://github.com/VitexSoftware/mcprack",
    "dark_code": True,
    "nav_links": [
        {"title": "GitHub", "url": "https://github.com/VitexSoftware/mcprack"},
    ],
}

html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True

epub_show_urls = 'footnote'

html_logo = "_static/project-logo.svg"

html_context = {
    'display_github': True,
    'github_user': 'VitexSoftware',
    'github_repo': 'mcprack-doc-en',
    'github_version': 'main',
    'conf_py_path': '/source/',
}
