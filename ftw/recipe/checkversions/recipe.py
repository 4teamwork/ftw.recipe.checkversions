from pprint import pformat
from zc.recipe.egg import Egg


class Recipe(Egg):

    def __init__(self, buildout, name, options):
        self.options = options
        name = 'ftw.recipe.checkversions'

        # Only install "bin/masstranslate" script, not other scripts.
        options['scripts'] = 'checkversions'

        blacklists = options.get('blacklists')
        kwargs = {'buildout_dir': buildout['buildout']['directory'],
                  'versions': options.get('versions', 'versions.cfg'),
                  'blacklists': blacklists and blacklists.split() or []}
        options['arguments'] = '**%s' % pformat(kwargs)

        super(Recipe, self).__init__(buildout, name, options)
