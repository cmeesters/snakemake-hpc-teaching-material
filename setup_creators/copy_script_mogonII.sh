#!/bin/bash

# This script is used to teach on the cluster "Mogon II"

CLUSTER_ALIAS="mogon_nox" # nox stands for "no X11 forwarding"
BASEPATH="/lustre/project/hpckurs/workflows" # repeated used

# creating remote directory:
ssh ${CLUSTER_ALIAS} "mkdir -p ${BASEPATH}"

scp condarc_mogon "${CLUSTER_ALIAS}:${BASEPATH}/condarc"
scp get_tutorial.sh "${CLUSTER_ALIAS}:${BASEPATH}/get_tutorial.sh"
scp install_micromamba.sh "${CLUSTER_ALIAS}:${BASEPATH}/install_micromamba.sh"
scp environment.yaml "${CLUSTER_ALIAS}:${BASEPATH}/environment.yaml"

rsync -rtlv --chmod=D755 "tutorial" "${CLUSTER_ALIAS}:${BASEPATH}"
rsync -rtlv --chmod=D755 "solutions" "${CLUSTER_ALIAS}:/lustre/project/hpckurs"
