# The Snakemake Teaching Alliance

## Purpose

This repository contains (better: will contain) teaching material to teach for

- workflow creators
- workflow users
- administrators

all tailored for HPC systems.

## Getting started / Onboarding

If you want to participate in the development: Just notify us (issue) and we will add your github account. Alternatively, you may fork the repo and create PRs from there.

Workflow for pull requests:

- create or take an issue to work on (you may assign others or no one). Issues ought to be as specific as possible. We may break "big issues" into smaller ones
- create a branch `"<shortname>_<issue_number>"`. Only in rare case (closely related issues) bundle the work on issues into one branch. The parent branch should always be "main"
- commit your work to branch
- push to origin (your own fork of the snakemake-hpc-teaching-material repository)
- create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) 
- assign arbitrary reviewer (or wait until someone takes on this pull reqeust)
- (s.o. else) perform review (switch to branch and try; check the quality)
- merge and delete source branch


## Progress

Currently, the LaTeX code contains TODO and FIXME items. They should all be removed and become githug issues. In order to list TODO items, run the `todo` script, e.g.

```bash
$ todo slides/
``` 

Otherwise, create issue reports. 

## LaTeX specialities

This repo contains some unique commands:

- `altverb` to include in-line listings code, e.g. `\altverb{filename}` or `\altverb{--flag}`. Use `\texttt{Name}` for project names, so: `\texttt{Snakemake}`, but `\altverb{snakemake --slurm}` to distinguish the project from the software.
- to include parameters from the config file, use the `\configparam{<name>}` command

## For Teachers

You can get in touch with us, if you want to host a course at your site. If possible, we are happy to teach a course at your site and teach you teaching (teach the teacher).

Everyone who wants to teach the course will find more information [here](https://github.com/cmeesters/snakemake-hpc-teaching-material/Teaching_Elsewhere.md).
