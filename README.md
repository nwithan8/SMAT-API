# SMAT
A Python API wrapper for the [Social Media Analysis Toolkit](https://www.smat-app.com/timeline)

# Installation:
- Clone this repo with ``git clone https://github.com/nwithan8/SMAT-API.git`` or install from PyPi with ``pip install smat``
- Import into your project with ``from smat import API``

# Usage:
This library currently supports the three main methods of [SMAT's API](https://api.smat-app.com/docs#):

- ``get_content``: Get a list of posts from a specific outlet
- ``get_activity``: Aggregate based on a particular field on a specific outlet
- ``get_time_series``: Get a time series for a specific outlet

- ``term`` is a required parameter for each field. All other parameters are optional or have preset defaults.
- Default outlet is ``reddit``

Docs coming soon. PRs welcome.
