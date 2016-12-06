MicroStrategyIServerScripts
====================================

MicroStrategyIServerScripts provide different scripts for the MicroStrategy Intelligence Server:
-isstate.py:	Script to show the MicroStrategy Intelligence Server's status
-isversion.py:	Script to show the MicroStrategy Intelligence Server's version
-isstart.py:	Script to start the MicroStrategy Intelligence Server and check the state afterwards
-isstop.py:		Script to stop the MicroStrategy Intelligence Server and check the state afterwards

The assembly was written and tested in Python 2.6.8 but runs as well in Python 2.7.9.

## Basic usage:
To add those scripts, copy the py-Files to your server under the /root-Folder and change the mode
to be executable via:
```bash
chmod +x isstate.py
chmod +x isstart.py
chmod +x isstop.py
chmod +x isversion.py
```

## To execute the scripts:
```python
python isstate.py
python isstart.py
python isstop.py
python isversion.py
```

## To define the aliases for the current user:
Create a new file (if it doesn’t already exist) in the /<username> folder (e.g. /root) called .bashrc and add the aliases from above.
Or copy the file Bash.basrc to the server and rename it to .bashrc.

## Change the paths in the scripts:
You will need to change the paths in the scripts to your MicroStrategy Intelligence Server's installation file

Change history
--------------

* **Version 1.0.0.0 (2016-12-06)** : 1.0 release.
