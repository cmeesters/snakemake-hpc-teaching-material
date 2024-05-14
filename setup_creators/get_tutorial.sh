#!/bin/bash

# 1. with this command we ensure that
#    we are working in your HOME directory:
cd

# 2. we are going to work in a dedicated directory:
mkdir snakemake-tutorial && cd snakemake-tutorial

# 3. download the sample data
curl -L https://api.github.com/repos/snakemake/snakemake-tutorial-data/tarball -o snakemake-tutorial-data.tar.gz

# 4. unpack the sample data
tar --wildcards -xf snakemake-tutorial-data.tar.gz --strip 1 "*/data" "*/environment.yaml"

