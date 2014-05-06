The Snakemake Workflow Repository
=================================

The Snakemake Workflow Repository is a collection of reusable and modularized Snakemake_ rules and workflows.
The provided code should also serve as a best-practices guide of how to build production ready workflows with Snakemake.

Structure
---------
Rules can be found under::

<discipline>/<subject>/rules/<analysis_step>/<name>.rules

The general strategy is to include these into your workflow via the include_ command.
This can also happen via https urls (in this case make sure, that you trust the source).
Example workflows following this strategy can be found under:: 

<discipline>/<subject>/workflows/<name>/Snakefile

Contribute
----------

We invite anybody to contribute to the Snakemake Workflow Repository.
If you want to contribute we suggest the following procedure:

* fork the repository
* develop your contribution
* perform a pull request

The pull request will be reviewed and included as fast as possible.
Thereby, contributions should follow the coding style of the already present examples, i.e.

* start with a docstring describing the usage and purpose,
* define author with email address and a license,
* follow the python style guide_,
* be customizable via a json config file parsed into a variable CONFIG,
* use 4 spaces for indentation,
* specify reasonable default values for threads and resources.

.. _Snakemake: https://bitbucket.org/johanneskoester/snakemake
.. _include: https://bitbucket.org/johanneskoester/snakemake/wiki/Documentation#markdown-header-includes
.. _guide: http://legacy.python.org/dev/peps/pep-0008
