
WRAPPER="/usr/bin/time -fpeak_used_memory:%M(Kb)"


$WRAPPER python stresstest/map_test.py  1000000
$WRAPPER python stresstest/map_test.py 11000000


$WRAPPER python stresstest/default_map_test.py  1000000
$WRAPPER python stresstest/default_map_test.py 11000000



