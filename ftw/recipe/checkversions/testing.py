from pkg_resources import get_distribution
from plone.testing import Layer
import zc.buildout.testing


def resolve_dependencies(pkg_name, result=None):
    if result is None:
        result = set()

    if pkg_name in ('setuptools', 'zc.buildout'):
        return result

    result.add(pkg_name)
    for pkg in get_distribution(pkg_name).requires():
        resolve_dependencies(pkg.project_name, result)

    return result


class RecipeLayer(Layer):

    @property
    def globs(self):
        # globs is required for zc.buildout.testing setup / tear down
        if 'buildout' not in self:
            self['buildout'] = {}
        return self['buildout']

    def testSetUp(self):
        zc.buildout.testing.buildoutSetUp(self)
        for pkgname in resolve_dependencies('ftw.recipe.checkversions'):
            zc.buildout.testing.install_develop(pkgname, self)

    def testTearDown(self):
        zc.buildout.testing.buildoutTearDown(self)


RECIPE_FIXTURE = RecipeLayer()
