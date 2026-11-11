# OCM Python client — regenerate from live clusters_mgmt OpenAPI spec.
# Requires: openapi-generator 7.27.x (see openapitools.json), Java runtime.

OPENAPI_GENERATOR ?= openapi-generator
SPEC_URL := https://api.openshift.com/api/clusters_mgmt/v1/openapi
SPEC_FILE := api_openshift_com.json
GEN_CONFIG := openapi-generator-config.yaml

.PHONY: help download-spec generate-sdk upgrade test clean

help:
	@echo "targets:"
	@echo "  upgrade         download spec + regenerate SDK (default path)"
	@echo "  download-spec   curl latest clusters_mgmt OpenAPI to $(SPEC_FILE)"
	@echo "  generate-sdk    openapi-generator with $(GEN_CONFIG)"
	@echo "  test            pytest with coverage"
	@echo "  clean           remove .venv, caches, coverage output"

upgrade: download-spec generate-sdk

download-spec:
	curl -fsSL -o $(SPEC_FILE) $(SPEC_URL)
	@echo "Updated $(SPEC_FILE)"

generate-sdk: $(SPEC_FILE)
	$(OPENAPI_GENERATOR) version | head -1
	$(OPENAPI_GENERATOR) generate \
	  -i ./$(SPEC_FILE) \
	  -g python \
	  -o . \
	  -c $(GEN_CONFIG) \
	  --git-user-id rh-mobb \
	  --git-repo-id ocm-python
	@echo "Regeneration complete. Review diff; run 'make test'."

test:
	python -m pytest --cov=ocm_client

clean:
	rm -rf .venv .pytest_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

$(SPEC_FILE):
	@echo "Missing $(SPEC_FILE). Run 'make download-spec'."
	@exit 1
