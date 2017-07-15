# Bash

Run as `root` in this directory:

```
ln -s $(pwd)/bash.* /etc/
```

Add at the bottom of `/etc/bash.bashrc`

```
if [ -f /etc/bash.functions ]; then
    source /etc/bash.functions
fi

if [ -f /etc/bash.aliases ];then
    source /etc/bash.aliases
fi
```
