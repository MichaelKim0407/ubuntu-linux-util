parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

PS1='\[\033[01;35m\][\D{%a %F %T}]\[\033[00m\] ${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]@\[\033[01;36m\]\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\n\[\033[01;33m\](\[\033[01;31m\]>\[\033[01;36m\]◠‿◠\[\033[01;33m\] )\[\033[01;31m\]>\[\033[00m\] \[\033[01;34m\]====)\[\033[00m\] '
