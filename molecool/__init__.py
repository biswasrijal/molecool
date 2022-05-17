"""A python package to analyze and visualize xyz files"""

# Add imports here
from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram
# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

