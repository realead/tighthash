#include <map>

#include "testutils.h"


int main(int argc,  char** argv){
    return do_test_map<tMap>(strtoull(argv[1], NULL, 10), 1.0);
}
