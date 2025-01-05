# -*- coding: utf-8 -*-

import json

from rich import print as rprint
from rich.console import Console
from rich.syntax import Syntax

from ..paths import dir_project_root, dir_htmlcov
from ..vendor.pytest_cov_helper import (
    run_unit_test as _run_unit_test,
    run_cov_test as _run_cov_test,
)


def run_unit_test(
    script: str,
):
    _run_unit_test(
        script=script,
        root_dir=f"{dir_project_root}",
    )


def run_cov_test(
    script: str,
    module: str,
    preview: bool = False,
    is_folder: bool = False,
):
    _run_cov_test(
        script=script,
        module=module,
        root_dir=f"{dir_project_root}",
        htmlcov_dir=f"{dir_htmlcov}",
        preview=preview,
        is_folder=is_folder,
    )


console = Console()


def jprint(dct: dict):
    """
    Pretty print json data.
    """
    code = json.dumps(dct, ensure_ascii=False, indent=4)
    syntax = Syntax(code, "json", theme="monokai", line_numbers=True)
    rprint(syntax)
