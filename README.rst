The Snakemake Workflow Repository
=================================

The Snakemake Workflow Repository is a collection of reusable and modularized Snakemake rules and workflows.

Structure
---------
Rules can be found under::

<discipline>/<subject>/rules/<analysis_step>/<name>.rules

The general strategy is to include these into your workflow via the include_ command.
This can also happen via https urls (in this case make sure that you trust the source).
Example workflows following this strategy can be found under:: 

<discipline>/<subject>/workflows/<name>/Snakefile

Contribute
----------

We invite anybody to contribute to the Snakemake Workflow Repository.
If you want to contribute we suggest forking the repository and doing a pull request once your ontribution is ready for release.
It will be reviewed and included as fast as possible.

.. _include: https://bitbucket.org/johanneskoester/snakemake/wiki/Documentation#markdown-header-includes
