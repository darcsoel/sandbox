import json
import os
import re


class DialogsRetriever:
    dataset_file_extension_pattern = r'^data(?s:.*)\.json$'

    def __init__(self, root_dir=None):
        if root_dir is None:
            root_dir = '../../../../'

        self._root_dir = root_dir

    def _get_json_files_list(self):
        all_files = [f for f in os.listdir(self._root_dir) if
                     os.path.isfile(os.path.join(self._root_dir, f))]
        return [f for f in all_files
                if re.search(self.dataset_file_extension_pattern, f)]

    def _parse_json_file(self, file):
        with open(os.path.join(self._root_dir, file), 'rb') as json_file:
            data = json.load(json_file)

            for dialog in data:
                if len(dialog.get('thread', [])) > 1:
                    yield dialog.get('thread')

    @property
    def data(self):
        files = self._get_json_files_list()

        for file in files:
            yield self._parse_json_file(file)
