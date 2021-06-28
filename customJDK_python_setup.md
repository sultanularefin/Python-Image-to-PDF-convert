

## python setup::

## sudo tar zxvf Python-3.9.4.tgz 


```js
taxi@taxi-HP-ProBook-4540s:/opt/Python-3.9.4$ ls
aclocal.m4          config.sub    Doc      install-sh  Mac              Modules       Parser   Programs       README.rst
CODE_OF_CONDUCT.md  configure     Grammar  Lib         Makefile.pre.in  netlify.toml  PC       pyconfig.h.in  setup.py
config.guess        configure.ac  Include  LICENSE     Misc             Objects       PCbuild  Python         Tools
taxi@taxi-HP-ProBook-4540s:/opt/Python-3.9.4$ sudo tar zxvf Python-3.9.4.tgz 


```


## readme file ...

## file:///opt/Python-3.9.4/READMEArefin.md

```js
Build Instructions
------------------

On Unix, Linux, BSD, macOS, and Cygwin::

    ./configure
    make
    make test
    sudo make install

This will install Python as ``python3``.
```

## doesn't work in opt dir:

```js

taxi@taxi-HP-ProBook-4540s:/opt/Python-3.9.4$ sudo ./configure
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking for python3.9... no
checking for python3... python3
checking for --enable-universalsdk... no
checking for --with-universal-archs... no
checking MACHDEP... "linux"
checking for gcc... gcc
checking whether the C compiler works... no
configure: error: in `/opt/Python-3.9.4':
configure: error: C compiler cannot create executables
See `config.log' for more details
taxi@taxi-HP-ProBook-4540s:/opt/Python-3.9.4$ ./configure
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking for python3.9... no
checking for python3... python3
checking for --enable-universalsdk... no
checking for --with-universal-archs... no
checking MACHDEP... "linux"
checking for gcc... gcc
checking whether the C compiler works... no
configure: error: in `/opt/Python-3.9.4':
configure: error: C compiler cannot create executables
See `config.log' for more details
taxi@taxi-HP-ProBook-4540s:/opt/Python-3.9.4$ make
make: *** No targets specified and no makefile found.  Stop.
taxi@taxi-HP-ProBook-4540s:/opt/Python-3.9.4$ make test
make: *** No rule to make target 'test'.  Stop.
taxi@taxi-HP-ProBook-4540s:/opt/Python-3.9.4$ 

```

## taxi@taxi-HP-ProBook-4540s:~/Downloads$ sudo tar zxvf Python-3.9.4.tgz -C /home/taxi/



## sudo apt install gobjc++


## this worked ::


This is Python version 3.9.4
============================

.. image:: https://travis-ci.org/python/cpython.svg?branch=3.9
   :alt: CPython build status on Travis CI
   :target: https://travis-ci.org/python/cpython

.. image:: https://github.com/python/cpython/workflows/Tests/badge.svg
   :alt: CPython build status on GitHub Actions
   :target: https://github.com/python/cpython/actions

.. image:: https://dev.azure.com/python/cpython/_apis/build/status/Azure%20Pipelines%20CI?branchName=3.9
   :alt: CPython build status on Azure DevOps
   :target: https://dev.azure.com/python/cpython/_build/latest?definitionId=4&branchName=3.9

.. image:: https://codecov.io/gh/python/cpython/branch/3.9/graph/badge.svg
   :alt: CPython code coverage on Codecov
   :target: https://codecov.io/gh/python/cpython

.. image:: https://img.shields.io/badge/discourse-join_chat-brightgreen.svg
   :alt: Python Discourse chat
   :target: https://discuss.python.org/


Copyright (c) 2001-2021 Python Software Foundation.  All rights reserved.

See the end of this file for further copyright and license information.

.. contents::

General Information
-------------------

- Website: https://www.python.org
- Source code: https://github.com/python/cpython
- Issue tracker: https://bugs.python.org
- Documentation: https://docs.python.org
- Developer's Guide: https://devguide.python.org/

Contributing to CPython
-----------------------

For more complete instructions on contributing to CPython development,
see the `Developer Guide`_.

.. _Developer Guide: https://devguide.python.org/

Using Python
------------

Installable Python kits, and information about using Python, are available at
`python.org`_.

.. _python.org: https://www.python.org/

Build Instructions
------------------

On Unix, Linux, BSD, macOS, and Cygwin::

    ./configure
    make
    make test
    sudo make install

This will install Python as ``python3``.

You can pass many options to the configure script; run ``./configure --help``
to find out more.  On macOS case-insensitive file systems and on Cygwin,
the executable is called ``python.exe``; elsewhere it's just ``python``.

Building a complete Python installation requires the use of various
additional third-party libraries, depending on your build platform and
configure options.  Not all standard library modules are buildable or
useable on all platforms.  Refer to the
`Install dependencies <https://devguide.python.org/setup/#install-dependencies>`_
section of the `Developer Guide`_ for current detailed information on
dependencies for various Linux distributions and macOS.

On macOS, there are additional configure and build options related
to macOS framework and universal builds.  Refer to `Mac/README.rst
<https://github.com/python/cpython/blob/3.9/Mac/README.rst>`_.

On Windows, see `PCbuild/readme.txt
<https://github.com/python/cpython/blob/3.9/PCbuild/readme.txt>`_.

If you wish, you can create a subdirectory and invoke configure from there.
For example::

    mkdir debug
    cd debug
    ../configure --with-pydebug
    make
    make test

(This will fail if you *also* built at the top-level directory.  You should do
a ``make clean`` at the top-level first.)

To get an optimized build of Python, ``configure --enable-optimizations``
before you run ``make``.  This sets the default make targets up to enable
Profile Guided Optimization (PGO) and may be used to auto-enable Link Time
Optimization (LTO) on some platforms.  For more details, see the sections
below.

Profile Guided Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^

PGO takes advantage of recent versions of the GCC or Clang compilers.  If used,
either via ``configure --enable-optimizations`` or by manually running
``make profile-opt`` regardless of configure flags, the optimized build
process will perform the following steps:

The entire Python directory is cleaned of temporary files that may have
resulted from a previous compilation.

An instrumented version of the interpreter is built, using suitable compiler
flags for each flavour. Note that this is just an intermediary step.  The
binary resulting from this step is not good for real life workloads as it has
profiling instructions embedded inside.

After the instrumented interpreter is built, the Makefile will run a training
workload.  This is necessary in order to profile the interpreter execution.
Note also that any output, both stdout and stderr, that may appear at this step
is suppressed.

The final step is to build the actual interpreter, using the information
collected from the instrumented one.  The end result will be a Python binary
that is optimized; suitable for distribution or production installation.


Link Time Optimization
^^^^^^^^^^^^^^^^^^^^^^

Enabled via configure's ``--with-lto`` flag.  LTO takes advantage of the
ability of recent compiler toolchains to optimize across the otherwise
arbitrary ``.o`` file boundary when building final executables or shared
libraries for additional performance gains.


What's New
----------

We have a comprehensive overview of the changes in the `What's New in Python
3.9 <https://docs.python.org/3.9/whatsnew/3.9.html>`_ document.  For a more
detailed change log, read `Misc/NEWS
<https://github.com/python/cpython/blob/3.9/Misc/NEWS.d>`_, but a full
accounting of changes can only be gleaned from the `commit history
<https://github.com/python/cpython/commits/3.9>`_.

If you want to install multiple versions of Python, see the section below
entitled "Installing multiple versions".


Documentation
-------------

`Documentation for Python 3.9 <https://docs.python.org/3.9/>`_ is online,
updated daily.

It can also be downloaded in many formats for faster access.  The documentation
is downloadable in HTML, PDF, and reStructuredText formats; the latter version
is primarily for documentation authors, translators, and people with special
formatting requirements.

For information about building Python's documentation, refer to `Doc/README.rst
<https://github.com/python/cpython/blob/3.9/Doc/README.rst>`_.


Converting From Python 2.x to 3.x
---------------------------------

Significant backward incompatible changes were made for the release of Python
3.0, which may cause programs written for Python 2 to fail when run with Python
3.  For more information about porting your code from Python 2 to Python 3, see
the `Porting HOWTO <https://docs.python.org/3/howto/pyporting.html>`_.


Testing
-------

To test the interpreter, type ``make test`` in the top-level directory.  The
test set produces some output.  You can generally ignore the messages about
skipped tests due to optional features which can't be imported.  If a message
is printed about a failed test or a traceback or core dump is produced,
something is wrong.

By default, tests are prevented from overusing resources like disk space and
memory.  To enable these tests, run ``make testall``.

If any tests fail, you can re-run the failing test(s) in verbose mode.  For
example, if ``test_os`` and ``test_gdb`` failed, you can run::

    make test TESTOPTS="-v test_os test_gdb"

If the failure persists and appears to be a problem with Python rather than
your environment, you can `file a bug report <https://bugs.python.org>`_ and
include relevant output from that command to show the issue.

See `Running & Writing Tests <https://devguide.python.org/runtests/>`_
for more on running tests.

Installing multiple versions
----------------------------

On Unix and Mac systems if you intend to install multiple versions of Python
using the same installation prefix (``--prefix`` argument to the configure
script) you must take care that your primary python executable is not
overwritten by the installation of a different version.  All files and
directories installed using ``make altinstall`` contain the major and minor
version and can thus live side-by-side.  ``make install`` also creates
``${prefix}/bin/python3`` which refers to ``${prefix}/bin/pythonX.Y``.  If you
intend to install multiple versions using the same prefix you must decide which
version (if any) is your "primary" version.  Install that version using ``make
install``.  Install all other versions using ``make altinstall``.

For example, if you want to install Python 2.7, 3.6, and 3.9 with 3.9 being the
primary version, you would execute ``make install`` in your 3.9 build directory
and ``make altinstall`` in the others.


Issue Tracker and Mailing List
------------------------------

Bug reports are welcome!  You can use the `issue tracker
<https://bugs.python.org>`_ to report bugs, and/or submit pull requests `on
GitHub <https://github.com/python/cpython>`_.

You can also follow development discussion on the `python-dev mailing list
<https://mail.python.org/mailman/listinfo/python-dev/>`_.


Proposals for enhancement
-------------------------

If you have a proposal to change Python, you may want to send an email to the
comp.lang.python or `python-ideas`_ mailing lists for initial feedback.  A
Python Enhancement Proposal (PEP) may be submitted if your idea gains ground.
All current PEPs, as well as guidelines for submitting a new PEP, are listed at
`python.org/dev/peps/ <https://www.python.org/dev/peps/>`_.

.. _python-ideas: https://mail.python.org/mailman/listinfo/python-ideas/


Release Schedule
----------------

See :pep:`596` for Python 3.9 release details.


Copyright and License Information
---------------------------------

Copyright (c) 2001-2021 Python Software Foundation.  All rights reserved.

Copyright (c) 2000 BeOpen.com.  All rights reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.  All
rights reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum.  All rights reserved.

See the file "LICENSE" for information on the history of this software, terms &
conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

This Python distribution contains *no* GNU General Public License (GPL) code,
so it may be used in proprietary projects.  There are interfaces to some GNU
code but these are entirely optional.

All trademarks referenced herein are property of their respective holders.



## simply this worked::


## execution time 8 seconds..

```js
./configure
make
make test
sudo make install
```

## output::

```js

Total duration: 7 min 27 sec
Tests result: SUCCESS
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ ls
aclocal.m4          config.status  Grammar         LICENSE          Misc          PC              pyconfig.h     python-config.py      Tools
build               config.sub     Include         Mac              Modules       PCbuild         pyconfig.h.in  python-gdb.py
CODE_OF_CONDUCT.md  configure      install-sh      Makefile         netlify.toml  platform        python         readmeArefinApril.md
config.guess        configure.ac   Lib             Makefile.pre     Objects       Programs        Python         README.rst
config.log          Doc            libpython3.9.a  Makefile.pre.in  Parser        pybuilddir.txt  python-config  setup.py
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ python --V
bash: python: command not found
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ python -V
bash: python: command not found
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ ./python -V
Python 3.9.4
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ 

```

## pip3::

```js

taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ grep -inr "pip3"
Doc/whatsnew/3.4.rst:228:   only the versioned ``pip3`` and ``pip3.4`` commands are bootstrapped by
Misc/HISTORY:2240:  command in addition to the versioned ``pip3`` and ``pip3.4`` commands.
Mac/BuildScript/scripts/postflight.ensurepip:15:# bpo-33290: An earlier "pip3 install --upgrade pip" may have installed
Mac/Makefile.in:98:				pip3 \
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ ./pip3 -V
bash: ./pip3: No such file or directory
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ 

```


## pip not found::

## can't decompress data; zlib not available

## taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ ./python -m ensurepip
## sudo apt-get install zlib1g-dev

## sudo apt install zlib1g-dev 
## sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev


yum install zlib-deve



./configure --with-ensurepip[=install|upgrade|no]
make
make test
sudo make install


./configure --with-ensurepip[install]
make
make test
sudo make install



./configure --with-ensurepip
make
make test
sudo make install



## pip installed by this:: taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ sudo apt-get install python3-pip



```js

taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ pip -v
bash: pip: command not found
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ python3-pip -V
bash: python3-pip: command not found
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ python3-pip -V
bash: python3-pip: command not found
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ pip3 -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ 

```

## python version::

```js

taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ pip3 -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ python -V
bash: python: command not found
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ ./python -V
Python 3.9.4
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ pwd
/home/taxi/Python-3.9.4
taxi@taxi-HP-ProBook-4540s:~/Python-3.9.4$ cd ..
taxi@taxi-HP-ProBook-4540s:~$ whereis python
python: /usr/bin/python3.8-config /usr/bin/python3.8 /usr/bin/python2.7 /usr/lib/python3.9 /usr/lib/python3.8 /usr/lib/python2.7 /etc/python3.8 /etc/python2.7 /usr/local/lib/python3.8 /usr/local/lib/python2.7 /usr/include/python3.8 /usr/share/python
taxi@taxi-HP-ProBook-4540s:~$ sudo apt-get remove python
[sudo] password for taxi:             
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'python-is-python2' instead of 'python'
0 upgraded, 0 newly installed, 0 to remove and 428 not upgraded.
taxi@taxi-HP-ProBook-4540s:~$ whereis python
python: /usr/bin/python3.8-config /usr/bin/python3.8 /usr/bin/python2.7 /usr/lib/python3.9 /usr/lib/python3.8 /usr/lib/python2.7 /etc/python3.8 /etc/python2.7 /usr/local/lib/python3.8 /usr/local/lib/python2.7 /usr/include/python3.8 /usr/share/python
taxi@taxi-HP-ProBook-4540s:~$ sudo apt-get remove python2
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  python-cairo python-crypto python-gi python-gobject-2 python-xdg python2
0 upgraded, 0 newly installed, 6 to remove and 428 not upgraded.
After this operation, 3,779 kB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 318449 files and directories currently installed.)
Removing python-cairo:amd64 (1.16.2-2ubuntu2) ...
Removing python-crypto (2.6.1-13ubuntu2) ...
Removing python-gi (3.36.0-1) ...
Removing python-gobject-2 (2.28.6-14ubuntu1) ...
Removing python-xdg (0.26-1ubuntu1) ...
Removing python2 (2.7.17-2ubuntu4) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9) ...
taxi@taxi-HP-ProBook-4540s:~$ whereis python2
python2: /usr/bin/python2 /usr/bin/python2.7 /usr/lib/python2.7 /etc/python2.7 /usr/local/lib/python2.7 /usr/share/man/man1/python2.1.gz
taxi@taxi-HP-ProBook-4540s:~$ whereis python
python: /usr/bin/python3.8-config /usr/bin/python3.8 /usr/bin/python2.7 /usr/lib/python3.9 /usr/lib/python3.8 /usr/lib/python2.7 /etc/python3.8 /etc/python2.7 /usr/local/lib/python3.8 /usr/local/lib/python2.7 /usr/include/python3.8 /usr/share/python
taxi@taxi-HP-ProBook-4540s:~$ python -V
bash: python: command not found
taxi@taxi-HP-ProBook-4540s:~$ D

```


## python get-pip.py

## python -m pip -V
#### pip 21.0.1 from /home/taxi/.local/lib/python3.9/site-packages/pip (python 3.9)


## new ultimate solution::

```js

Python 3.9.4
taxi@taxi-HP-ProBook-4540s:~$ python get-pip.py
Defaulting to user installation because normal site-packages is not writeable
Collecting pip
  Downloading pip-21.0.1-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 1.1 MB/s 
Collecting setuptools
  Downloading setuptools-56.0.0-py3-none-any.whl (784 kB)
     |████████████████████████████████| 784 kB 8.9 MB/s 
Collecting wheel
  Downloading wheel-0.36.2-py2.py3-none-any.whl (35 kB)
Installing collected packages: wheel, setuptools, pip
  WARNING: The script wheel is installed in '/home/taxi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts pip, pip3 and pip3.9 are installed in '/home/taxi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-21.0.1 setuptools-56.0.0 wheel-0.36.2
taxi@taxi-HP-ProBook-4540s:~$ pip3 -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
taxi@taxi-HP-ProBook-4540s:~$ pip -V
bash: /usr/lib/python3/dist-packages/pip: Is a directory
taxi@taxi-HP-ProBook-4540s:~$ python -m pip

Usage:   
  /home/taxi/Python-3.9.4/python -m pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING,
                              ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM
                              format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download.
                              Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
taxi@taxi-HP-ProBook-4540s:~$ python -m pip -V
pip 21.0.1 from /home/taxi/.local/lib/python3.9/site-packages/pip (python 3.9)
taxi@taxi-HP-ProBook-4540s:~$ 

```

## final output:

```js

taxi@taxi-HP-ProBook-4540s:~$ python -V
Python 3.9.4
taxi@taxi-HP-ProBook-4540s:~$ python -m pip -V
pip 21.0.1 from /home/taxi/.local/lib/python3.9/site-packages/pip (python 3.9)
taxi@taxi-HP-ProBook-4540s:~$ 

```

## readme dir::

```js

# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# export ANDROID_HOME=$HOME/Android/Sdk 
# export PATH=$PATH:$ANDROID_HOME/tools
# export PATH=$PATH:$ANDROID_HOME/platform-tools
# export PATH=$PATH:$JAVA_HOME/bin
# export PATH=$PATH:$ANDROID_HOME/emulator
# export PATH=$PATH:$ANDROID_HOME/tools/bin
# export REACT_EDITOR=/opt/WebStorm-191.6183.63/bin/webstorm.sh

# export JAVA_HOME ="/opt/jdk-14.0.2/"
export PATH=$PATH:$JAVA_HOME/bin
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools

# export PATH=$PATH:/opt/gradle-5.4/bin

# export PATH=$JAVA_HOME/bin 
#// uncomment above for react native development. and comment below line also run source $HOME/.profile.
# also python stufss. like alias.
# export PATH=$PATH:/opt/jdk-14.0.2/bin
# export REACT_EDITOR=/opt/WebStorm-192.7142.35/bin/webstorm.sh
export PATH=$PATH:/opt/android-studio/bin/studio.sh
export PATH=$PATH:/home/taxi/flutter/bin
export PATH=$PATH:/home/taxi/flutter/bin/cache/dart-sdk/bin
export PATH=$PATH:/home/taxi/Python-3.9.4/
# export PATH=$PATH:/usr/lib/python3/dist-packages/pip
# alias python='/usr/bin/python3' 
# alias pip='/usr/bin/pip3' 
# alias pip='/usr/lib/python3/dist-packages/pip'
# alias python='/home/taxi/Python-3.9.4'
# /usr/bin/python3

# command -v pip3 /usr/bin/pip3

# export PATH=$PATH:/home/taxi/.local/bin
# export PATH=$PATH:/opt/WebStorm-192.7142.35/bin
# export PATH=$PATH:/opt/PhpStorm-193.5662.63/bin/phpstorm.sh
# export PATH=$PATH:/home/taxi/.meteor
# export PATH=$PATH:/opt/lampp/bin # FOR PHP VERSION
# export PATH=$PATH:/usr/bin/cake

# export NVM_DIR="${XDG_CONFIG_HOME/:-$HOME/.}nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

# export NVM_DIR="${XDG_CONFIG_HOME/:-$HOME/.}nvm" 
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```