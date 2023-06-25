import authlib

project = u'Authlib'
copyright = u'&copy; 2017, Hsiaoming Ltd'
author = u'Hsiaoming Yang'
version = authlib.__version__
release = version

templates_path = ["_templates"]
html_static_path = ["_static"]
html_css_files = [
  'custom.css',
]
html_theme = "shibuya"

html_copy_source = False
html_show_sourcelink = False

language = 'en'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx_copybutton",
    "sphinx_design",
]

extlinks = {
    'issue': ('https://github.com/lepture/authlib/issues/%s', 'issue #%s'),
    'PR': ('https://github.com/lepture/authlib/issues/%s', 'pull request #%s'),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
html_favicon = '_static/icon.svg'
html_theme_options = {
    'og_image_url': 'https://authlib.org/logo.png',
    "light_logo": "_static/light-logo.svg",
    "dark_logo": "_static/dark-logo.svg",
    "light_css_variables": {
        "--sy-rc-theme": "62,127,203",
    },
    "dark_css_variables": {
        "--sy-rc-theme": "102,173,255",
    },
    "twitter_site": "authlib",
    "twitter_creator": "lepture",
    "twitter_url": "https://twitter.com/authlib",
    "github_url": "https://github.com/lepture/authlib",
    "nav_links": [
        {
            "title": "Projects",
            "children": [
                {
                    "title": "Authlib",
                    "url": "https://authlib.org/",
                    "summary": "OAuth, JOSE, OpenID, etc."
                },
                {
                    "title": "JOSE RFC",
                    "url": "https://jose.authlib.org/",
                    "summary": "JWS, JWE, JWK, and JWT."
                },
                {
                    "title": "OTP Auth",
                    "url": "https://otp.authlib.org/",
                    "summary": "One time password, HOTP/TOTP.",
                },
            ]
        },
        {"title": "Sponsor me", "url": "https://github.com/sponsors/lepture"},
    ]
}

html_context = {}
