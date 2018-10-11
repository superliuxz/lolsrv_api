import importlib


def load_class_from_path(path_to_class: str):
    *module_path, class_name = path_to_class.split(".")
    module = importlib.import_module(".".join(module_path))
    return getattr(module, class_name)
