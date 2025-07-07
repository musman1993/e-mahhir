# E-Mahhir

lock uv.lock file again using: uv pip compile pyproject.toml --all-extras --generate-hashes

build the docker: docker build -t e-mahhir-be .

run the container: docker run -d -p 8000:8000 e-mahhir-be
