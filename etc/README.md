# Bash

Run as `root` in this directory:

```
ln -s $(pwd)/bash.* /private/etc/
```

Add at the bottom of `/private/etc/bashrc`

```
source /private/etc/bash.bashrc.append
```
