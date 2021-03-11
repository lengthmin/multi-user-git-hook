config:
	mkdir -p ~/.config/git/template/hooks
	git config --global init.templateDir ~/.config/git/template

install: config
	cp pre-commit.py ~/.config/git/template/hooks/pre-commit
	chmod +x ~/.config/git/template/hooks/pre-commit

test: install
	mkdir tests
	cd tests && git init && touch 1.py && git add . && git commit -m "test"

clean:
	rm -rf tests
