

(cd tighthash && python setup.py build_ext --inplace)

if [ "$1" = "--show" ] ; then
    firefox tighthash/ctighthash.html&
fi


