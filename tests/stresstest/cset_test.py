
import sys
sys.path.append('..')

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashSet as Set

from testutils import testing_script

testing_script("Cython TightHashSet", Set)


