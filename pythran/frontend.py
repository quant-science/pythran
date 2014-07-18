"""
    This module contains pythran frontend
"""

from pythran.openmp import GatherOMPData
from pythran.syntax import check_syntax
from pythran.transformations import ExtractTopLevelStmts, NormalizeIdentifiers

import ast
import re


def parse(pm, code):
    # hacky way to turn OpenMP comments into strings
    code = re.sub(r'(\s*)#\s*(omp\s[^\n]+)', r'\1"\2"', code)

    # front end
    ir = ast.parse(code)

    # remove top - level statements
    pm.apply(ExtractTopLevelStmts, ir)

    # parse openmp directive
    pm.apply(GatherOMPData, ir)

    # avoid conflicts with cxx keywords
    renamings = pm.apply(NormalizeIdentifiers, ir)
    check_syntax(ir)
    return ir, renamings
