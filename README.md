# FreeBSD Port for NCPA

### Usage

Use this as a overlay to your ports checkout in Poudriere.

### Why on github and not in the FreeBSD Ports Collection?

Currently, [NCPA](https://github.com/NagiosEnterprises/ncpa) requires
Python 2.7 and has no Python 3 support.  I expect pushback with adding
a port that depends on a soon to be removed Python 2.7.

Once NCPA is updated to work on Python 3, I will update this and
submit the new version to the FreeBSD Ports Collection.

