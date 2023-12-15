#!/bin/bash

# This script is used to teach on the cluster "Mogon II"

CLUSTER_ALIAS="mogon_nox" # nox stands for "no X11 forwarding"
BASEPATH="/lustre/project/hpckurs/workflows" # repeated used

# creating remote directory:
ssh mogon_nox "mkdir -p ${BASEPATH}"

scp condarc "${CLUSTER_ALIAS}:/lustre/project/hpckurs/workflows/condarc"
scp get_tutorial.sh "${CLUSTER_ALIAS}:/lustre/project/hpckurs/workflows/get_tutorial.sh"

rsync -rtlv --chmod=D755 "tutorial" "${CLUSTER_ALIAS}:/lustre/project/hpckurs/workflows"
rsync -rtlv --chmod=D755 "solutions" "${CLUSTER_ALIAS}:/lustre/project/hpckurs"
