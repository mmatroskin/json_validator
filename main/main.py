from os import path, listdir
from pathlib import Path
import json
from collections import namedtuple
import jsonschema


def main():
    ErrorEnt = namedtuple('ErrorEnt', 'item, message')
    Schema = namedtuple('Schema', 'name, schema')

    root_dir = Path(__file__).resolve().parent.parent
    result_file = path.join(root_dir, r'results.txt')
    schemas_dir = path.join(root_dir, r'task_folder\schema')
    files_dir = path.join(root_dir, r'task_folder\event')
    schemas_list = listdir(schemas_dir)
    events = listdir(files_dir)

    schemas = []
    errors = []

    for f in schemas_list:
        name = path.join(schemas_dir, f)
        with open(name, 'r', encoding='utf-8') as h:
            try:
                item = json.load(h)
                schemas.append(Schema(f, item))
            except Exception as e:
                errors.append(ErrorEnt(f, str(e)))

    for i in events:
        name = path.join(files_dir, i)
        with open(name, 'r', encoding='utf-8') as h:
            try:
                item = json.load(h)
                error_items = []
                for schema in schemas:
                    try:
                        jsonschema.validate(instance=item, schema=schema.schema)
                        break
                    except jsonschema.ValidationError as e:
                        error_items.append(f'{schema.name} - {e.message}')
                if len(error_items) == len(schemas):
                    errors.append(ErrorEnt(i, '; '.join(error_items)))
            except Exception as e:
                errors.append(ErrorEnt(f, str(e)))

    with open(result_file, 'w', encoding='utf-8') as fh:
        fh.writelines([f'{i.item}: {i.message}\n' for i in errors])
    pass


if __name__ == '__main__':
    main()
