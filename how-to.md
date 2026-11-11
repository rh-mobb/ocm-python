# Regenerating ocm-client

## Prerequisites

- **Java** runtime (Homebrew `openapi-generator` bundles OpenJDK)
- **OpenAPI Generator 7.27.0** — match [`openapitools.json`](openapitools.json)
  - macOS: `brew install openapi-generator`
  - Or: `npx @openapitools/openapi-generator-cli` with the same pinned version

## One-shot (recommended)

```bash
make upgrade
make test
```

## Manual steps

1. Download the live spec:

   ```bash
   curl -fsSL -o api_openshift_com.json \
     https://api.openshift.com/api/clusters_mgmt/v1/openapi
   ```

2. Generate:

   ```bash
   openapi-generator generate \
     -i ./api_openshift_com.json \
     -g python \
     -o . \
     -c openapi-generator-config.yaml \
     --git-user-id rh-mobb \
     --git-repo-id ocm-python
   ```

3. Confirm `.openapi-generator/VERSION` matches the pinned release.

4. Run tests:

   ```bash
   pip install -r requirements.txt -r test-requirements.txt
   pip install -e .
   pytest --cov=ocm_client
   ```

## Preserved files

Non-generated files are listed in [`.openapi-generator-ignore`](.openapi-generator-ignore) (`README.md`, `AGENTS.md`, `Makefile`, CI under `.github/`, etc.). Update that list if you add hand-maintained paths.

## Version bumps

Edit `packageVersion` in [`openapi-generator-config.yaml`](openapi-generator-config.yaml) before regenerating, or bump `__version__` / `setup.py` / `pyproject.toml` after generation if you are cutting a release without a full regen.
