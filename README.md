[![Snakemake](https://img.shields.io/badge/snakemake-≥3.1-brightgreen.svg?style=flat-square)](https://bitbucket.org/johanneskoester/snakemake)

# The Snakemake Workflow Repository

The Snakemake Workflow Repository is a collection of reusable and modularized [Snakemake](https://bitbucket.org/johanneskoester/snakemake) rules and workflows.
The provided code should also serve as a best-practices guide of how to build production ready workflows with Snakemake.

## Structure

Rules can be found under

```
<discipline>/<subject>/rules/<analysis_step>/<name>.rules
```

The general strategy is to include these into your workflow via the [include](https://bitbucket.org/johanneskoester/snakemake/wiki/Documentation#markdown-header-includes) directive.
This can also happen via https urls (in this case make sure, that you trust the source).
Example workflows following this strategy can be found under::

```
<discipline>/<subject>/workflows/<name>/Snakefile
```

## Content

### Next Generation Sequencing

So far, this repository contains rules for the read mappers BWA and PEANUT, general samtools
rules for manipulating SAM/BAM files, rules for the variant callers GATK and Freebayes and two
example variant calling workflows (based on GATK and Freebayes).

### Contribute

We invite anybody to contribute to the Snakemake Workflow Repository.
If you want to contribute we suggest the following procedure:

* fork the repository
* develop your contribution
* perform a pull request

The pull request will be reviewed and included as fast as possible.
Thereby, contributions should follow the coding style of the already present examples, i.e.

* start with a docstring describing the usage and purpose,
* define author with email address and a license,
* follow the python [style guide](http://legacy.python.org/dev/peps/pep-0008),
* be customizable via a json config file parsed into a variable CONFIG,
* use 4 spaces for indentation,
* specify reasonable default values for threads and resources.