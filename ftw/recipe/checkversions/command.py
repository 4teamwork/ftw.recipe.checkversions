from ftw.recipe.checkversions.buildout import read_versions
from ftw.recipe.checkversions.checker import get_version_updates


def main(buildout_dir, versions, blacklists):
    current_versions = read_versions(buildout_dir, versions)
    blacklist = dict()
    for file_or_url in blacklists:
        blacklist.update(read_versions(buildout_dir, file_or_url))

    updates = get_version_updates(current_versions, blacklist.keys())

    for package, version in sorted(updates.items()):
        print package, '=', version
