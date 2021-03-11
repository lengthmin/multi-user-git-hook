# multi-user-git-hook

Switch git user based on the name of the directory.

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

then next time you create a git project, the hook will be active.

## set email

the key `has` means the `pwd` result has this part, for example, `~/0Workspace/multi-user-git-hook` has `0Workspace`.

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

set this in your `~/.gitconfig`

use dash(`-`) to separate the different parts, for example: `user.email` -> `user-email`.

because `.gitconfig` can not use dash as the key.

## make install

you can use `make install` to place the `pre-commit` file, and change the `.gitconfig` mannualy.

## Thanks

Thanks to [pgils/multi-email-git-hook](https://github.com/pgils/multi-email-git-hook), the project has helped me a lot.

## References

- [pgils/multi-email-git-hook](https://github.com/pgils/multi-email-git-hook)
- [git-init Documentation](http://git-scm.com/docs/git-init)
- [githooks Documentation](http://git-scm.com/docs/githooks)
