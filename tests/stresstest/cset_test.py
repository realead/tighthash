
import sys
sys.path.append('..')
from tighthash import cset

from testutils import testing_script

testing_script("Cython TightHashSet", cset)


