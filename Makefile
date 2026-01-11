install:
	uv sync

brain-games:
	uv run brain-games

build: install 
	uv build

package-install: build
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

.PHONY: braint-games

