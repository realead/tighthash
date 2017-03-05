
WRAPPER="/usr/bin/time -fpeak_used_memory:%M(Kb)"


$WRAPPER python stresstest/map_test.py  1000000
$WRAPPER python stresstest/map_test.py 11000000


$WRAPPER python stresstest/default_map_test.py  1000000
$WRAPPER python stresstest/default_map_test.py 11000000


g++ -std=c++11 -O3 stresstest/test_tree_map.cpp -o test_tree_map
$WRAPPER ./test_tree_map 1000000
$WRAPPER ./test_tree_map 11000000

g++ -std=c++11 -O3 stresstest/test_hash_map.cpp -o test_hash_map
$WRAPPER ./test_hash_map 1000000
$WRAPPER ./test_hash_map 11000000

g++ -std=c++11 -O3 stresstest/test_hash_map2.cpp -o test_hash_map2
$WRAPPER ./test_hash_map2 1000000
$WRAPPER ./test_hash_map2 11000000

rm test_hash_map
rm test_hash_map2
rm test_tree_map



