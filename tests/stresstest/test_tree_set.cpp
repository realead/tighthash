#include <set>

#include "testutils.h"


int main(int argc,  char** argv){
    return do_test<std::set<size_t> >(strtoull(argv[1], NULL, 10), 1.0);
}
