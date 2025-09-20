# QTradeX Core Package
__version__ = "1.2.0"

# Import core components
from qtradex.core.base_bot import BaseBot

# Import common utilities
try:
    from qtradex.common import *
except ImportError:
    pass

# Import indicators
try:
    from qtradex.indicators import qi
except ImportError:
    pass

# Import core functionality
try:
    from qtradex.core import *
except ImportError:
    pass