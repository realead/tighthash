
WRAPPER="/usr/bin/time -fpeak_used_memory:%M(Kb)"


$WRAPPER python stresstest/set_test.py  1000000
$WRAPPER python stresstest/set_test.py 11000000

$WRAPPER python stresstest/cset_test.py  1000000
$WRAPPER python stresstest/cset_test.py 11000000

$WRAPPER python stresstest/default_set_test.py  1000000
$WRAPPER python stresstest/default_set_test.py 11000000

g++ -std=c++11 -O3 stresstest/test_tree_set.cpp -o test_tree_set
$WRAPPER ./test_tree_set 1000000
$WRAPPER ./test_tree_set 11000000

g++ -std=c++11 -O3 stresstest/test_hash_set.cpp -o test_hash_set
$WRAPPER ./test_hash_set 1000000
$WRAPPER ./test_hash_set 11000000

g++ -std=c++11 -O3 stresstest/test_hash_set2.cpp -o test_hash_set2
$WRAPPER ./test_hash_set2 1000000
$WRAPPER ./test_hash_set2 11000000


