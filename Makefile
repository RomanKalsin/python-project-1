install:
	uv sync

brain-games:
	uv run brain-games

build: install 
	uv build

package-install: build
	uv tool install dist/*.whl

.PHONY: braint-games
