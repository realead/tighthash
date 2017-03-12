
import sys
sys.path.append('..')

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashMap as Map

from testutils import testing_map

testing_map("CTightHashMap", Map)

