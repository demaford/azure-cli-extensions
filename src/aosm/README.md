# Microsoft Azure CLI 'aosm' Extension

This package is for the 'aosm' extension to support Azure Operator Service Manager 
functions.
i.e. `az aosm`

## Background

The `az aosm` extension is intended to provide support for working with AOSM
resources and definitions. Currently it only implements commands which aid the
process of publishing Network Function Definitions and Network Service Designs to
use with Azure Operator Service Manager or Network Function Manager.

## Installation

`az extension add --name aosm`

For CNFs you will also need helm, and possibly docker installed. See [CNFs](#cnfs) below for details.

# nfd and nsd commands

These commands help with the publishing of Network Function Definition and Network
Service Design resources.

## Overview of function
A generic workflow of using the tool would be:
- Find the pre-requisite items you require for your use-case
- Run a `generate-config` command to output an example JSON config file for subsequent commands
- Fill in the config file
- Run a `build` command to output one or more bicep templates for your Network Function Definition or Network Service Design
- Review the output of the build command, edit the output as necessary for your requirements
- Run a `publish` command to:
    * Create all pre-requisite resources such as Resource Group, Publisher, Artifact Stores, Groups
    * Deploy those bicep templates
    * Upload artifacts to the artifact stores

### Pre-requisites

#### VNFs

For VNFs, you will need a single ARM template which would create the Azure resources
for your VNF, for example a Virtual Machine, disks and NICs. You'll also need a VHD
image that would be used for the VNF Virtual Machine.

#### CNFs

For CNFs you must have these packages installed on the machine you are running the CLI from:
-  `helm` package installed . Instructions on how to do this can be found [here](https://helm.sh/docs/intro/install/).
-  `docker` installed only in some circumstances, those being if the source image is in your local docker repository, or you do not have subscription-wide permissions required to push charts and images. See the remainder of this section for further details. Docker provides packages that easily configure docker on [Windows](https://docs.docker.com/docker-for-windows/), or [Linux](https://docs.docker.com/engine/install/#supported-platforms) systems.

For CNFs, you must provide:
* Helm packages with an associated schema. These files must be on your disk and will be referenced in the `cnf-input.jsonc` config file. 
* A reference to an existing Azure Container Registry which contains the images for your CNF. Currently, only one ACR and namespace is supported per CNF. The images to be copied from this ACR are populated automatically based on the helm package schema. You must have Reader/AcrPull permissions on this ACR. To use this, fill in `source_registry` and optionally `source_registry_namespace` in the cnf-input.jsonc file.
* Optionally, you can provide a file (on disk) path_to_mappings which is a copy of values.yaml with your chosen values replaced by deployment parameters, thus exposing them as parameters to the CNF.
* When filling in the cnf-input.jsonc file, you must list helm packages in the order they are to be deployed. For example, if A must be deployed before B, your cnf-input.jsonc should look something like this:

        "helm_packages": [
            {
                "name": "A",
                "path_to_chart": "Path to package A",
                "path_to_mappings": "Path to package A mappings",
                "depends_on": [
                    "Names of the Helm packages this package depends on"
                ]
            },
            {
                "name": "B",
                "path_to_chart": "Path to package B",
                "path_to_mappings": "Path to package B mappings",
                "depends_on": [
                    "Names of the Helm packages this package depends on"
                ]
            },

##### Permissions for publishing CNFs
If sourcing the CNF images from an existing ACR, you need to have `Reader`/`AcrPull` permissions
from this ACR, and ideally, `Contributor` role + `AcrPush` role (or a custom role that allows the `importImage` action and `AcrPush`) over the whole subscription in order to be able to import to the new Artifact store. If you have these, you 
do not need docker to be installed locally, and the image copy is very quick.

If you do not have the subscription-wide permissions then you can run the `az aosm nfd publish` command using the `--no-subscription-permissions` flag to pull the image to your local machine and then push it to the Artifact Store using manifest credentials scoped only to the store. This requires docker to be installed locally.

#### NSDs
For NSDs, you will need to have a Resource Group with a deployed Publisher, Artifact Store, Network Function Definition and Network Function Definition Version. You can use the `az aosm nfd` commands to create all of these resources.


### Command examples

#### Before you start
`az login` to login to the Azure CLI.
`az account set --subscription <subscription>` to choose the subscription you will work on.

#### NFDs

Get help on command arguments

`az aosm -h`
`az aosm nfd -h`
`az aosm nfd build -h`
etc...

All these commands take a `--definition-type` argument of `vnf` or `cnf`

Create an example config file for building a definition

`az aosm nfd generate-config`

This will output a file called `cnf-input.jsonc` which must be filled in. 
Once the config file has been filled in the following commands can be run.

Build an nfd definition locally

`az aosm nfd build --config-file cnf-input.jsonc`

Publish a pre-built definition

`az aosm nfd publish --build-output-folder cnf-cli-output`


#### NSDs

Get help on command arguments

`az aosm -h`
`az aosm nsd -h`
`az aosm nsd build -h`
etc...

Create an example config file for building a definition

`az aosm nsd generate-config`

This will output a file called `nsd-input.jsonc` which must be filled in. 
Once the config file has been filled in the following commands can be run.

Build an nsd locally

`az aosm nsd build --config-file nsd-input.jsonc`

Publish a pre-built design

`az aosm nsd publish --build-output-folder nsd-cli-output`


## Bug Reporting

It would be much appreciated if you could report these so that we're aware of them!

Please see [Logging](#logging) for how to view and collect logs. 

Please describe what you are doing and if possible provide the input and output files.

The (Microsoft internal) process for bug reporting during development is here:
https://eng.ms/docs/strategic-missions-and-technologies/strategic-missions-and-technologies-organization/azure-for-operators/aiops/aiops-orchestration/aosm-product-docs/processes/bug_process

CLI issues should be tagged and triaged as UX bugs.

## Logging

The CLI uses the standard Azure CLI logging mechanism. To enable logging to the console, you can use the following flags depending on the desired level of logging:
- `--verbose` - This flag changes the logging level to Info and above.
- `--debug` - This flag changes the logging level to Debug and above.
- `--only-show-errors` - This flag changes the logging level to Error only, suppressing Warning.

It is also possible to enable logging to file by running the following command:
```
az config set logging.enable_log_file=true
```
This will create a log file in the `~/.azure/logs` directory. 

**Note:** The above command will enable logging for all Azure CLI commands until the logging is disabled again by the user. Not disabling file logging could slow down the performance of the CLI. To disable file logging, run the following command:
```
az config set logging.enable_log_file=false
```

## Development
Information about setting up and maintaining a development environment for this extension can be found [here](https://eng.ms/docs/strategic-missions-and-technologies/strategic-missions-and-technologies-organization/azure-for-operators/aiops/aiops-orchestration/aosm-product-docs/processes/cli_contributing).
