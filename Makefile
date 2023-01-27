install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

package-install:
	python3 -m pip install --user dist/*.whl

flake:
	poetry run flake8 brain_games
