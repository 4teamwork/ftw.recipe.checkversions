from ftw.recipe.checkversions.pypi import get_newest_release


def get_version_updates(current_versions,
                        blacklist=()):
    """Checks all packages in current_versions for newer releases and returns
    a new dict with all updated packages, ignoring those listed
    in the blacklist.
    """

    updates = {}

    for package, version in current_versions.items():
        if package in blacklist:
            continue

        newest = get_newest_release(package)
        if newest is None:
            continue

        if version != newest:
            updates[package] = newest

    return updates
