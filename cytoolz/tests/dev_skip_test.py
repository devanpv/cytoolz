"""
Determine when dev tests should be skipped by regular users.

Some tests are only intended to be tested during development right
before performing a release.  These do not test core functionality
of `cytoolz` and may be skipped.  These tests are only run if the
following conditions are true:

    - toolz is installed
    - toolz is the correct version
    - cytoolz is a release version
"""
import cytoolz
from nose.tools import nottest, istest

try:
    import toolz
    do_toolz_tests = True
except ImportError:
    do_toolz_tests = False

if do_toolz_tests:
    do_toolz_tests = cytoolz.__toolz_version__ == toolz.__version__
    do_toolz_tests &= 'dev' not in cytoolz.__version__

# Decorator used to skip tests for developmental versions of CyToolz
if do_toolz_tests:
    dev_skip_test = istest
else:
    dev_skip_test = nottest
