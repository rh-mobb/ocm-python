# Agent Guide — ocm-python

Python client for **OCM clusters_mgmt** (`https://api.openshift.com`, `/api/clusters_mgmt/v1`). PyPI/setuptools name **`ocm-client`**; import **`ocm_client`**.

**Release 0.4.0+** is generated with **OpenAPI Generator 7.27** (`python` target, **Pydantic v2**, **Python ≥ 3.11**). Pre-0.4.0 legacy Generator 4.x output is obsolete — do not copy patterns from old checkouts.

## Where rules live

| Source | Use it for |
|--------|------------|
| `README.md` | Install, quick start, 0.4.0 breaking changes |
| `how-to.md` / `Makefile` | Regenerating the SDK (procedural authority) |
| `openapi-generator-config.yaml` | Generator additional properties (package name, version, library) |
| `openapitools.json` | Pinned OpenAPI Generator CLI version |
| `CHANGELOG.md` | Release notes |
| `AGENTS.md` | Boundaries for agents |

## Product boundaries (OCM)

- Scope is **clusters_mgmt** only — not accounts, subscriptions, or other OCM OpenAPI roots.
- Prefer **`ocm` CLI** skills for operator command syntax; this repo is for **Python SDK** usage.
- **terraform-provider-rhcs** for Terraform — not this package.
- Spec source: `https://api.openshift.com/api/clusters_mgmt/v1/openapi` (cached as `api_openshift_com.json`).

## Repository layout

```
openapi-generator-config.yaml  # MOBB generator options (edit before regen)
openapitools.json                # Pin generator 7.27.0
Makefile                         # make upgrade / make test
api_openshift_com.json           # Cached OpenAPI input
ocm_client/                      # Generated package (Pydantic models, DefaultApi)
docs/                            # Generated Markdown reference
test/                            # Generated model tests (stubs; pytest passes)
pyproject.toml, setup.py         # Generated packaging (version 0.4.0)
.github/workflows/python.yml     # CI (3.11–3.13)
```

No Ansible content — directory name `ansible/ocm-python` is incidental.

## Generated code policy

Almost all of `ocm_client/`, `docs/`, and `test/` is generated.

- **Regenerate** for API changes: `make upgrade` or steps in `how-to.md`.
- **Do not** hand-edit `default_api.py` or bulk models.
- Preserve hand-written files via `.openapi-generator-ignore`.

## Using the client

```python
from ocm_client import ApiClient, Configuration, DefaultApi

with ApiClient(Configuration(host="https://api.openshift.com", access_token="…")) as client:
    api = DefaultApi(client)
    page = api.api_clusters_mgmt_v1_clusters_get()
```

- Models: `from ocm_client.models.cluster import Cluster` → `Cluster.model_validate(data)`.
- Errors: `ocm_client.exceptions.ApiException`.
- Never commit tokens.

## Tests

```bash
pip install -r requirements.txt -r test-requirements.txt && pip install -e .
pytest --cov=ocm_client
```

Tests are generator stubs (no live API). CI: `.github/workflows/python.yml`.

## Regeneration checklist

1. Bump `packageVersion` in `openapi-generator-config.yaml` when releasing.
2. `make download-spec` and review spec diff size.
3. `make generate-sdk` with generator version matching `openapitools.json`.
4. `make test` — expect hundreds of generated tests to pass.
5. Update `CHANGELOG.md` and `README.md` if behavior or breaking notes changed.

## Human review triggers

- OpenAPI Generator major upgrade.
- Switching HTTP library (`library: httpx` vs `urllib3` in config).
- Consumer-breaking renames of `ocm_client` package.
