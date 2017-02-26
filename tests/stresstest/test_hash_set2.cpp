#include <unordered_set>

#include "testutils.h"


int main(int argc,  char** argv){
    return do_test<std::unordered_set<size_t> >(strtoull(argv[1], NULL, 10), 10.0);
}
