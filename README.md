# multi-user-git-hook

DEPRECATED: Switch git user based on the name of the directory.

as `@crea1` said in [stackoverflow](https://stackoverflow.com/questions/8801729/is-it-possible-to-have-different-git-configuration-for-different-projects):

As of git version 2.13, git supports [conditional configuration includes](https://git-scm.com/docs/git-config#_conditional_includes). In this example we clone Company A's repos in ~/company_a directory, and Company B's repos in ~/company_b.

In your `.gitconfig` you can put something like this.

```ini
[includeIf "gitdir:~/company_a/"]
  path = .gitconfig-company_a
[includeIf "gitdir:~/company_b/"]
  path = .gitconfig-company_b
```

Example contents of `.gitconfig-company_a`

```ini
[user]
name = John Smith
email = john.smith@companya.net
```

Example contents of `.gitconfig-company_b`

```ini
[user]
name = John Smith
email = js@companyb.com
```

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

the key `has` means `$(pwd)` has `$(value)`, for example, `~/0Workspace/multi-user-git-hook` has `0Workspace`.

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
