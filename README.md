# python-blueprint

My bootstrap for python stuff - tweaked from a variety of sources.

---

## Usage

Clone and update references to `blueprint` with your own app name. It pops up in around a dozen places - manageable to update these without being worth a script to flip them.

Makefile is available for convenience. Some particular options:

- `make docker-build` will build the docker image using the APP name by default, but can be overridden with e.g. `make docker-build IMAGE=eu.gcr.io/your-gcp-project/app`
- `make docker-run` is there for convenience - rebuilding the docker image and then running it with a bash shell entrypoint

When building the docker image, note that it picks the latest git-sha as the version unless you specify otherwise (or use a git tag), and the last commit email address as the maintainer to label in the image.
