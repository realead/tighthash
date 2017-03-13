echo "unit tests..."
sh unit_tests.sh

echo "random tests..."
sh  random_tests.sh

echo "stress tests..."
sh stress_tests_for_map.sh
sh stress_tests_for_set.sh
