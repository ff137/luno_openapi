# Generating the client

To generate the client, download the OpenAPI generator and build the JAR yourself.

## Prerequisites: Build OpenAPI generator

```sh
# Clone project
git clone https://github.com/OpenAPITools/openapi-generator.git

# Build OpenAPI generator JAR
cd openapi-generator
git checkout v7.7.0

mvn -B --no-snapshot-updates clean package -DskipTests=true -Dmaven.javadoc.skip=true -Djacoco.skip=true
```

## Download the Luno OpenAPI Specification

This script requires `playwright`:

```sh
pip install playwright # / conda install playwright
python -m playwright install
```

Then, run the download script:

```sh
python scripts/download_luno_api.py
```

## Generate the Luno OpenAPI Client

```sh
cd luno_openapi

# Assuming openapi-generator is in directory up from luno_openapi
java -ea -server -Duser.timezone=UTC -jar "$(pwd)/../openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar" generate -c ./specs/openapi-generator-config.yml --skip-validate-spec
```
