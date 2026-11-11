# ocm-client

Python SDK for the Red Hat **OpenShift Cluster Manager (OCM)** [clusters management API](https://api.openshift.com/api/clusters_mgmt/v1/openapi) (`/api/clusters_mgmt/v1`).

- **PyPI / setuptools name:** `ocm-client`
- **Import package:** `ocm_client`
- **Current release:** `0.4.0` (OpenAPI Generator **7.27**, **Pydantic v2**, **Python ≥ 3.11**)

Maintained by [rh-mobb/ocm-python](https://github.com/rh-mobb/ocm-python).

## Install

```bash
pip install "git+https://github.com/rh-mobb/ocm-python.git"
```

Or from a checkout:

```bash
pip install -e .
```

## Quick start

```python
from ocm_client import ApiClient, Configuration, DefaultApi

configuration = Configuration(
    host="https://api.openshift.com",
    access_token="<Bearer JWT from `ocm` login or offline token>",
)

with ApiClient(configuration) as api_client:
    api = DefaultApi(api_client)
    clusters = api.api_clusters_mgmt_v1_clusters_get()
    for item in clusters.items or []:
        print(item.id, item.name)
```

Use `https://api.integration.openshift.com` for integration/stage when appropriate.

### Models

API objects are **Pydantic v2** models (`model_validate`, `model_dump`). Example:

```python
from ocm_client.models.cluster import Cluster

payload = {"name": "my-cluster", "managed": True, ...}  # see API docs / spec
cluster = Cluster.model_validate(payload)
```

Full method and model reference lives under [`docs/`](docs/) (generated).

## Regenerating the client

See [`how-to.md`](how-to.md) or run:

```bash
make upgrade   # download spec + regenerate
make test
```

Generator version is pinned in [`openapitools.json`](openapitools.json); options in [`openapi-generator-config.yaml`](openapi-generator-config.yaml).

## Breaking changes in 0.4.0

This release is a **full regeneration** on the modern OpenAPI Generator `python` target. It is **not** API-compatible with pre-0.4.0 `ocm-python` builds (Generator 4.x / `six` / plain model classes).

| Before (≤ 0.3.x style) | After (0.4.0+) |
|------------------------|----------------|
| `Cluster(...)` dict-like objects | `Cluster.model_validate({...})` |
| `obj.to_dict()` | `obj.model_dump(by_alias=True)` |
| Python 2.7 / 3.4+ | **Python 3.11+** |
| `six`, legacy `openapi_types` | **Pydantic v2**, `py.typed` |
| Optional typed method args | Typed parameters on `DefaultApi` methods |

## Related tools

- **[`ocm` CLI](https://github.com/openshift-online/ocm-cli)** — day-to-day operator workflows
- **[terraform-provider-rhcs](https://github.com/terraform-redhat/terraform-provider-rhcs)** — Terraform for ROSA/OCM
- **[openshift-cluster-management-python-client](https://github.com/RedHatQE/openshift-cluster-management-python-client)** — alternate generated client layout (Red Hat QE)

## License

Apache 2.0 — see [LICENSE.txt](LICENSE.txt).
