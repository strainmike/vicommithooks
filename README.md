# vicommithooks
A set of common LabVIEW project requirements to prevent checking unshippable code into the repo.

# Usage

    pip install vicommithooks
    vicommithooks --help
    usage: vicommithooks [-h] [-r] [--source-only] [--min-version MIN_VERSION]
                         [--max-version MAX_VERSION] [--not-prerelease]
                         file
    
    positional arguments:
      file
    
    optional arguments:
      -h, --help            show this help message and exit
      -r, --recursive       Recursively searched the path for all VIs.
      --source-only         Asserts the VI(s) are set to source only
      --min-version MIN_VERSION
                            Asserts that the major version of LabVIEW the VI was
                            saved with is greater than or equal to this value
      --max-version MAX_VERSION
                            Asserts that the major version of LabVIEW the VI was
                            saved with is less than or equal to this value
      --not-prerelease      Asserts that the version of LabVIEW the VI was saved
                            with is not a prerelease version
    
# Contributing

Feel free to post PRs to improve this.
