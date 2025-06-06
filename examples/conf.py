import os
import sys
from pathlib import Path
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------
project = "PyMC"
copyright = "2022, PyMC Community"
author = "PyMC Community"

# -- General configuration ---------------------------------------------------

sys.path.insert(0, os.path.abspath("../sphinxext"))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinxcontrib.bibtex",
    "sphinx_codeautolink",
    "notfound.extension",
    "thumbnail_extractor",
    "sphinxext.rediraffe",
    "sphinx_sitemap",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/.ipynb_checkpoints/*",
    "extra_installs.md",
    "page_footer.md",
    "**/*.myst.md",
]
numfig = True


def remove_index(app):
    """
    This removes the index pages so rediraffe generates the redirect placeholder
    It needs to be present initially for the toctree as it defines the navbar.
    """

    index_file = Path(app.outdir) / "index.html"
    index_file.unlink()

    app.env.project.docnames -= {"index"}
    yield "", {}, "layout.html"


def setup(app: Sphinx):
    app.connect("html-collect-pages", remove_index, 100)


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# theme options
html_theme = "pymc_sphinx_theme"
html_baseurl = "https://www.pymc.io/projects/examples/"
rtd_version = os.environ.get("READTHEDOCS_VERSION", "")
sitemap_url_scheme = f"{{lang}}{rtd_version}/{{link}}"
html_theme_options = {
    "secondary_sidebar_items": ["postcard", "page-toc", "edit-this-page", "sourcelink", "donate"],
    "navbar_start": ["navbar-logo"],
    "logo": {
        "link": "https://www.pymc.io",
    },
    "article_header_end": ["nb-badges"],
    "show_prev_next": True,
    "article_footer_items": ["rendered_citation.html"],
}
version = version if "." in rtd_version else "main"
doi_code = os.environ.get("DOI_READTHEDOCS", "10.5281/zenodo.5654871")
html_context = {
    "github_url": "https://github.com",
    "github_user": "pymc-devs",
    "github_repo": "pymc-examples",
    "github_version": version,
    "doc_path": "examples/",
    "sandbox_repo": f"pymc-devs/pymc-sandbox/{version}",
    "doi_url": f"https://doi.org/{doi_code}",
    "doi_code": doi_code,
    "default_mode": "light",
}


html_favicon = "../_static/PyMC.ico"
html_logo = "../_static/PyMC.png"
html_title = "PyMC example gallery"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../_static"]
html_css_files = ["custom.css"]
html_extra_path = ["../_thumbnails", "robots.txt"]
templates_path = ["../_templates"]
html_sidebars = {
    "**": [
        "sidebar-nav-bs.html",
        "postcard_categories.html",
        "ablog/tagcloud.html",
    ],
}

# ablog config
blog_baseurl = "https://docs.pymc.io/projects/examples/en/latest/"
blog_title = "PyMC Examples"
blog_path = "blog"
blog_authors = {
    "contributors": ("PyMC Contributors", "https://docs.pymc.io"),
}
blog_default_author = "contributors"
post_show_prev_next = False
fontawesome_included = True
# post_redirect_refresh = 1
# post_auto_image = 1
# post_auto_excerpt = 2

notfound_urls_prefix = "/projects/examples/en/latest/"

# MyST config
myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath", "substitution"]
myst_dmath_double_inline = True
citation_code = f"""
```bibtex
@incollection{{citekey,
  author    = "<notebook authors, see above>",
  title     = "<notebook title>",
  editor    = "PyMC Team",
  booktitle = "PyMC examples",
  doi       = "{doi_code}"
}}
```
"""


myst_substitutions = {
    "pip_dependencies": "{{ extra_dependencies }}",
    "conda_dependencies": "{{ extra_dependencies }}",
    "extra_install_notes": "",
    "citation_code": citation_code,
}
nb_execution_mode = "off"

rediraffe_redirects = {
    "index.md": "gallery.md",
}

# bibtex config
bibtex_bibfiles = ["references.bib"]
bibtex_default_style = "unsrt"
bibtex_reference_style = "author_year"

# OpenGraph config
# use default readthedocs integration aka no config here

codeautolink_autodoc_inject = False
codeautolink_concat_default = True

# intersphinx mappings
intersphinx_mapping = {
    "arviz": ("https://python.arviz.org/en/latest/", None),
    "bambi": ("https://bambinos.github.io/bambi", None),
    "einstats": ("https://einstats.python.arviz.org/en/latest/", None),
    "mpl": ("https://matplotlib.org/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pymc": ("https://www.pymc.io/projects/docs/en/stable/", None),
    "pymc-bart": ("https://www.pymc.io/projects/bart/en/latest/", None),
    "pytensor": ("https://pytensor.readthedocs.io/en/latest/", None),
    "pmx": ("https://www.pymc.io/projects/experimental/en/latest/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "xarray": ("https://docs.xarray.dev/en/stable/", None),
}
