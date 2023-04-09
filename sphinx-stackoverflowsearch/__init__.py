from os import path
from sphinx.jinja2glue import SphinxFileSystemLoader
# from sphinx.application import Sphinx

def add_static_dir(app):
    if app.builder.name != 'html':
        return
    extension_dir = path.dirname(path.abspath(__file__))
    static_dir = path.join(extension_dir, 'static')
    app.builder.config.html_static_path.append(static_dir)
    template_dir = path.join(extension_dir, 'templates')
    app.builder.templates.pathchain.insert(1, template_dir)
    app.builder.templates.loaders.insert(1, SphinxFileSystemLoader(template_dir))
    app.builder.templates.templatepathlen += 1

def setup(app):
    app.connect('builder-inited', add_static_dir)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
