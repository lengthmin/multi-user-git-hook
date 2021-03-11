# multi-email-git-hook

## setting git init template

> **TEMPLATE DIRECTORY**
> Files and directories in the template directory whose name do not start with a dot will be copied to the $GIT_DIR(default: .git) after it is created.

[git-init Documentation](http://git-scm.com/docs/git-init)

The files which are copied from the template directory are placed in your GIT_DIR which defaults to the .git directory under your repo's root directory.

so we can put hooks in the template dir, and it will be copied to the newly created projects.

```sh
mkdir -p ~/.config/git/template/hooks
git config --global init.templateDir ~/.config/git/template
```

## put hook file

first of all, pls read: [githooks Documentation](http://git-scm.com/docs/githooks)

```sh
cp -i pre-commit.py ~/.config/git/template/hooks/pre-commit
```

## set email

example:

put this in your `~/.gitconfig`

`dismatch` is glob-style pattern.

```ini
[multi "ant"]
	has=0Ant
	user-email=xxxxxxx@xx.com
	user-name=xx
	user-signingkey = xxxx
[multi "gmail"]
	has=0Workspace
	user-email = xxxxx@xxx.com
	user-name = xxxxxx
	user-signingkey = xxxxx
```

use dash(`-`) to separate the different parts, for example: `user.email` -> `user-email`.

because `.gitconfig` can not use dash as the key.
