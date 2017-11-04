# Bash aliases

Run as `root` in this directory:

```
ln -s $(pwd)/bash_aliases ~/.bash_aliases
```

# Scripts

Run as `root` in this directory:

```
ln -s $(pwd)/*.py ~/
ln -s $(pwd)/*.sh ~/
```

# Show update info when login to root

Make sure you have `apt`, `pip2` and `pip3` installed.

If you don't have all of them, you can modify `check/update.sh` and `check/show.sh` to suit your own needs.

Run as `root` in this directory:

```
ln -s $(pwd)/bash_login ~/.bash_login
ln -s $(pwd)/check ~/
```

Add at the end of `~/.bashrc`:

```
if [ -f ~/.bash_login ]; then
    . ~/.bash_login
fi
```

Add to `cron` using `crontab -e`:

```
0 * * * * /root/check/update.sh
```

# Update pip packages

`pip-upgrade-all.py` has been moved to project [mkpipU](https://githu.com/MichaelKim0407/mk-pip-upgrade-all).
