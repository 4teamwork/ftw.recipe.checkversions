import os


def create_structure(*dirs_and_structure):
    structure = dirs_and_structure[-1]
    if len(dirs_and_structure) > 1:
        basedir = resolve_to_path(dirs_and_structure[:-1])
    else:
        basedir = None

    for filepath, data in structure.items():
        filepath = resolve_to_path((basedir, filepath))
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filepath, 'w+') as file_:
            file_.write(data)


def cat(*pathparts):
    filepath = resolve_to_path(pathparts)
    with open(filepath) as file_:
        return file_.read()


def resolve_to_path(pathparts):
    if isinstance(pathparts, (list, tuple)):
        return os.path.join(*map(resolve_to_path, pathparts))
    elif isinstance(pathparts, unicode):
        return pathparts.encode('utf-8')
    else:
        return pathparts
