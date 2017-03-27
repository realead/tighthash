# tighthash

python set/map classes with tiny memory footprint

## Motivation

It may come as a surprise, but the memory footprint of `dict` or `set` is huge,  but a even bigger surprise is that the same is the case for c++ classes. 

In the following table there are memory cost to save a 64bit integer in a set:

| set type             | cost per 8byte (64bit) integer |
|----------------------|--------------------------------|
|python set            | 47.2      (x5.9)               |
| std::set             | 48.0      (x6.0)               |
| std::unordered\_set  | 40.0      (x5.0)               |
| std::unordered\_set* | 32.8      (x4.1)               |
|thighthash.cset       |  9.6      (x1.2)               |
|thighthash.pset       |  9.6      (x1.2)               |

\* with max\_load\_factor=10.0.

The tighthash package comes in two flavors: the python (pset) and cython (cset), which both need only 1/5 of memory of a standard python set or mere 20% overhead compared to the raw 8bytes.

The situation is similar concerning dictionaries/maps for storing of two 8byte values:

| map type             | cost per 2x8byte (64bit) integer |
|----------------------|--------------------------------|
|python dict           | 64.9     (x4.1)                |
|std::map              | 64.0     (x4.0)                |
|std::unordered\_map   | 40.0     (x2.5)                |
|std::unordered\_map*  | 32.8     (x2.1)                |
|thighthash.cmap       | 19.2     (x1.2)                |
|thighthash.pmap       | 19.2     (x1.2)                |

\* with max\_load\_factor=10.0.

## Constraints

`tighthash.cset`, `tighthash.pset`, `tighthash.pmap`, and `tighthash.cmap` have only support for 64bit unsigned integers. It would be possible to extend these data structures also for other datatypes, but they are less useful: 

   1. A bitset would be enough for a 32bit integer and would easily pass into the RAM of a modern computer.
   2. An arbitrary Python class would be contradictory to the goal of having a small memory footprint, because of its overhead.
   
Normally a bijektion is used to encode/decode object into/from 64bit integers.

The tighthash sets and maps can grow dynamically, however the current implementation leads to memory usage spikes of factor almost 2. This can and should be avoided by providing the final number of element to the constructor. 


## Performance

There is a price to pay for smaller memory footprint: the time needed to carry out the operations. The fastest implentation is std::ordered\_xxx, so all times are given compared to it:

| set type             |add   | look up | delete |
|----------------------|------|---------|--------|
|python set            | x1.1    | x2.6 |	x2.7 |
|std::set (10^7 elems) | x4.8  | x7.9 | x6.8 |
|std::unordered\_set   | x1.0  | x1.0 | x1.0 |
|std::unordered\_set*  | x1.1  | x2.2 |	x2.2 |
|thighthash.cset       | x1.1  | x2.9 |	x2.6 |
|thighthash.pset       | x10.6 | x29.0| x104.3|

The python version of thighthash suffers from the need to covert c-integers into python integers. The cython version does not have to do that and is thus competitive with the default python set. std::set is far behind and is only advisable if the keys are long and it takes a lot of time for calculating the hash, which is not the case for 64bit integers.

It is very similar for the map, with cmap loosing a little bit more ground against the c++ version:

| map type             |add   | look up | delete |
|----------------------|------|---------|--------|
|python dict           | x1.5    | x3.2 |	x3.0 |
|std::map (10^7 elems) | x5.8  | x8.3 | x6.0 |
|std::unordered\_map   | x1.0  | x1.0 | x1.0 |
|std::unordered\_map*  | x1.8  | x3.3 |	x2.9 |
|thighthash.cmap       | x2.2  | x6.1 |	x2.9 |
|thighthash.pmap       | x25.5 | x54.6| x190.0|

## Usage

### Prerequisites

If the faster cmap/cset classes should be used:

    1. cython
    2. python-dev package (*sudo apt-get install python-dev* or similar)
    
### Build

call 

    sh build_ctighthash.sh
    
to build the cython versions of the data structures.

### Use

Just import `tighthash` and get access to `cmap`, `cset`, `pmap` and `pset`. 

Sample:

    from tighthash import cset
       
    s=cset(10) #10 elements without rehashing
    s.add(5)
    if 5 in s:
        print "5 is in set"
    s.discard(5)
    if not 5 in s:
        print "5 is not in set"
  
### Test

  use scripts in `tests` subfolder for unit/random/stress tests.
        
### Outlook

  1. Xset/Xmap are not yet a drop-in replacement of the standard set and dict, this is mostly because of the laziness and not a limitation of the approach.
  2. It would be intersting to minimize the memory spikes during the rehashing
  
## Noteworthy:
    
  1. Google sparse hash: https://github.com/sparsehash/sparsehash 





