from ftw.recipe.checkversions.buildout import read_versions
from ftw.recipe.checkversions.testing import TEMP_DIRECTORY_FIXTURE
from ftw.recipe.checkversions.tests import fshelpers
from unittest2 import TestCase


HOTFIXES_415 = 'https://raw.githubusercontent.com/4teamwork/' + \
               'ftw-buildouts/master/hotfixes/4.1.5.cfg'


class TestBuildout(TestCase):
    layer = TEMP_DIRECTORY_FIXTURE

    def setUp(self):
        self.tempdir = self.layer[u'tempdir']

    def test_versions_from_local_file(self):
        fshelpers.create_structure(self.tempdir, {
                'versions.cfg': '\n'.join((
                        '[versions]',
                        'foo = 1.0.0',
                        'bar = 1.2.0'))})

        self.assertEquals(
            {'foo': '1.0.0',
             'bar': '1.2.0'},
            read_versions(self.tempdir, 'versions.cfg'))

    def test_versions_from_local_file_with_extends(self):
        fshelpers.create_structure(self.tempdir, {
                'versions.cfg': '\n'.join((
                        '[versions]',
                        'foo = 1.0.0',
                        'bar = 1.2.0')),

                'buildout.cfg': '\n'.join((
                        '[buildout]',
                        'extends = versions.cfg'))})

        self.assertEquals(
            {'foo': '1.0.0',
             'bar': '1.2.0'},
            read_versions(self.tempdir, 'buildout.cfg'))

    def test_versions_from_URL(self):
        self.assertDictContainsSubset(
            {
                'Products.PloneHotfix20121106': '1.2',
                'Products.PloneHotfix20130618': '1.3.1',
                'Products.PloneHotfix20131210': '1.0',
            },
            read_versions(self.tempdir, HOTFIXES_415))

    def test_versions_from_file_extending_URL(self):
        fshelpers.create_structure(self.tempdir, {
                'versions.cfg': '\n'.join((
                        '[buildout]\n',
                        'extends = %s' % HOTFIXES_415))})

        self.assertDictContainsSubset(
            {
                'Products.PloneHotfix20121106': '1.2',
                'Products.PloneHotfix20130618': '1.3.1',
                'Products.PloneHotfix20131210': '1.0',
            },
            read_versions(self.tempdir, 'versions.cfg'))
