#!/bin/bash

# Please note: if your ssh-configuration contains "ForwardX11 yes" rsync
# might not return. In this case, use a config without X11 forwarding.

CLUSTER_ALIAS=<cluster_name>

scp condarc "${CLUSTER_ALIAS}:/path/to/setup/dir"
scp get_tutorial.sh "${CLUSTER_ALIAS}:/path/to/setup/dir"

rsync -rtlv --chmod=D755 "tutorial" "${CLUSTER_ALIAS}:/path/to/tutorial"
rsync -rtlv --chmod=D755 "solutions" "${CLUSTER_ALIAS}:/path/to/tutorial"
