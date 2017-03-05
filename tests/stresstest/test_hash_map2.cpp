#include <unordered_map>

#include "testutils.h"


int main(int argc,  char** argv){
    return do_test_map<uMap>(strtoull(argv[1], NULL, 10), 10.0);
}
