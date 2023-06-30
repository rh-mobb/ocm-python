1. Download the spec

    ```
    curl https://api.openshift.com/api/clusters_mgmt/v1/openapi > api_openshift_com.json
    ```

2. Run openapi-generator

    ```
    openapi-generator generate -i ./api_openshift_com.json -g python --package-name ocm_client --git-repo-id ocm-python --git-user-id rh-mobb
    ```
