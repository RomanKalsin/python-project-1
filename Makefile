install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

build: install 
	uv build

package-install: build
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

.PHONY: braint-games

