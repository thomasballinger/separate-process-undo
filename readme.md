Undo via rerunning a cli process with old interaction

This is an example script to accompany the article at
[ballingt.com/interpreter-undo](http://ballingt.com/interpreter-undo).

If you're interested in making something like this for real, you may find the
terminal rewriting code in [rlundo](https://github.com/thomasballinger/rlundo) useful.


written in Python 2

requires pexpect, `pip install pexpect`

usage:

    python test.py python

    python test.py irb

    python test.py ghci

    etc.
