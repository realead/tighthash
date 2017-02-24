

WRAPPER="/usr/bin/time -v"
$WRAPPER python stresstest/set_test.py

$WRAPPER python stresstest/cset_test.py

$WRAPPER python stresstest/default_set_test.py

g++ -std=c++11 -O3 stresstest/test_tree_set.cpp -o test_tree_set
$WRAPPER ./test_tree_set

g++ -std=c++11 -O3 stresstest/test_hash_set.cpp -o test_hash_set
$WRAPPER ./test_hash_set
