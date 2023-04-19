import json
import inspect
from typing import Iterable


class InfoEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, BugInfo):
            return o.to_dict()
        if isinstance(o, General):
            return o.to_dict()
        if isinstance(o, PatchInfo):
            return o.to_dict()
        if isinstance(o, PatchHunk):
            return o.to_dict()
        # Base class will raise the TypeError.
        return super().default(o)


class Info:

    def __str__(self):
        return json.dumps(self, cls=InfoEncoder)

    def __dir__(self) -> Iterable[str]:
        return [attr for attr in super.__dir__(self)
                if attr.find("__") == -1 and not inspect.isfunction(getattr(self, attr))
                and not callable(getattr(self, attr))]

    def to_list(self):
        return [str(getattr(self, attr)) for attr in super.__dir__(self)
                if attr.find("__") == -1 and not inspect.isfunction(getattr(self, attr))
                and not callable(getattr(self, attr))]

    def to_dict(self):
        return {}


class BugInfo(Info):

    def __init__(self, general, patches: list):
        super().__init__()
        self.general = general
        self.patches = patches

    def to_dict(self):
        return {
            'general': self.general.to_dict(),
            'patches': self.patches
        }


class BugInfoDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        if 'general' in o and 'patches' in o:
            decoded_BugInfo = BugInfo(
                GeneralDecoder().decode(json.dumps(o.get('general'))),
                PatchInfoDecoder().decode(json.dumps(o.get('patches')))
            )
            return decoded_BugInfo
        return o


class General(Info):

    def __init__(self, compiled, status, failing_compiled, total_time, engine_creation_time, pass_failing_test=None):
        super().__init__()
        self.compiled = compiled
        self.status = status
        self.failing_compiled = failing_compiled
        self.total_time = total_time
        self.engine_creation_time = engine_creation_time
        self.pass_failing_test = pass_failing_test

    def to_dict(self):
        return {
            'NR_RIGHT_COMPILATIONS': self.compiled,
            'OUTPUT_STATUS': self.status,
            'NR_FAILLING_COMPILATIONS': self.failing_compiled,
            'TOTAL_TIME': self.total_time,
            'ENGINE_CREATION_TIME': self.engine_creation_time,
            'PASSED_FAILING_TEST': self.pass_failing_test
        }


class GeneralDecoder(json.JSONDecoder):

    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        # args = dict((key, value) for key, value in o.items())
        # object = General(**args)
        # return object
        decoded_General = General(
            o.get('NR_RIGHT_COMPILATIONS'),
            o.get('OUTPUT_STATUS'),
            o.get('NR_FAILLING_COMPILATIONS'),
            o.get('TOTAL_TIME'),
            o.get('ENGINE_CREATION_TIME'),
            o.get('PASSED_FAILING_TEST')
        )
        return decoded_General


class PatchInfo(Info):

    def __init__(self, patch_diff, id, validation, patch_hunks: list, time, generation):
        super().__init__()
        self.patch_diff = patch_diff
        self.id = id
        self.validation = validation
        self.patch_hunks = patch_hunks
        self.time = time
        self.generation = generation

    def to_dict(self):
        return {
            'PATCH_DIFF_FORMAT': self.patch_diff,
            'VARIANT_ID': self.id,
            'VALIDATION': self.validation,
            'patchhunks': self.patch_hunks,
            'TIME': self.time,
            'GENERATION': self.generation
        }


class PatchInfoDecoder(json.JSONDecoder):

    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        if 'patchhunks' in o:
            decoded_patchInfo = PatchInfo(
                o.get('PATCH_DIFF_FORMAT'),
                o.get('VARIANT_ID'),
                o.get('VALIDATION'),
                PatchHunkDecoder().decode(json.dumps(o.get('patchhunks'))),
                o.get('TIME'),
                o.get('GENERATION')
            )
            return decoded_patchInfo
        return o


class PatchHunk(Info):

    def __init__(self, location, scope, original_code, buggy_code_type, operator,
                 line, suspiciouness, mp_ranking, patch_hunk_code, ingredient_parent, patch_hunk_type):
        super().__init__()
        self.location = location
        self.scope = scope
        self.original_code = original_code
        self.buggy_code_type = buggy_code_type
        self.operator = operator
        self.line = line
        self.suspiciouness = suspiciouness
        self.mp_ranking = mp_ranking
        self.patch_hunk_code = patch_hunk_code
        self.ingredient_parent = ingredient_parent
        self.patch_hunk_type = patch_hunk_type

    def to_dict(self):
        return {
            'LOCATION': self.location,
            'INGREDIENT_SCOPE': self.scope,
            'ORIGINAL_CODE': self.original_code,
            'BUGGY_CODE_TYPE': self.buggy_code_type,
            'OPERATOR': self.operator,
            'LINE': self.line,
            'SUSPICIOUNESS': self.suspiciouness,
            'MP_RANKING': self.mp_ranking,
            'PATCH_HUNK_CODE': self.patch_hunk_code,
            'INGREDIENT_PARENT': self.ingredient_parent,
            'PATCH_HUNK_TYPE': self.patch_hunk_type
        }


class PatchHunkDecoder(json.JSONDecoder):

    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        decoded_patchHunk = PatchHunk(
            o.get('LOCATION'),
            o.get('INGREDIENT_SCOPE'),
            o.get('ORIGINAL_CODE'),
            o.get('BUGGY_CODE_TYPE'),
            o.get('OPERATOR'),
            o.get('LINE'),
            o.get('SUSPICIOUNESS'),
            o.get('MP_RANKING'),
            o.get('PATCH_HUNK_CODE'),
            o.get('INGREDIENT_PARENT'),
            o.get('PATCH_HUNK_TYPE')
        )
        return decoded_patchHunk
