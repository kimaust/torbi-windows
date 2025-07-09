###############################################################################
# Configuration
###############################################################################


# Default configuration parameters to be modified
from .config import defaults

# Modify configuration
import yapecs
yapecs.configure('torbi', defaults)

# Import configuration parameters
from .config.defaults import *
import torbi
del torbi.defaults # remove unnecessary module
from .config.static import *


###############################################################################
# Module imports
###############################################################################

import torch
from . import _C
from .viterbi import decode
from .core import *
from .chunk import chunk
# Optional imports - these modules have optional dependencies
try:
    from . import data
except ImportError as e:
    import warnings
    warnings.warn(f"torbi.data module not available: {e}")

try:
    from . import evaluate
except ImportError as e:
    import warnings
    warnings.warn(f"torbi.evaluate module not available: {e}")

try:
    from . import partition
except ImportError as e:
    import warnings
    warnings.warn(f"torbi.partition module not available: {e}")

try:
    from . import reference
except ImportError as e:
    import warnings
    warnings.warn(f"torbi.reference module not available: {e}")
