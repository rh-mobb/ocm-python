# Changelog

## 0.4.0

**Breaking:** regenerate entire SDK with OpenAPI Generator **7.27.0** (modern `python` generator).

- Pydantic v2 models, Python **3.11+**, `urllib3` 2.x, PEP 561 `py.typed`
- Fresh `clusters_mgmt` OpenAPI spec (expanded schema vs legacy tree)
- Pinned generator metadata (`openapitools.json`, `openapi-generator-config.yaml`, `Makefile`, GitHub Actions)
- Auto-generated tests import `ocm_client` consistently (642 model unit tests)

Removes support for the Generator 4.x / `six` client emitted by earlier MOBB releases.
