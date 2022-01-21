# circuitpython-text_menu
Simple text menu for running CircuitPython modules from a serial monitor.

To use this utility, simply place the `code.py` file at the root of your CircuitPython drive. Any CircuitPython modules you want to be able to run from the menu (.py files) must be placed in the root (not in sub-directories).

When the modules are listed, type the letter next to the module you want followed by `<enter>`. The selected module will run.

A few notes:

1. Requires CircuitPython 7.0+
2. Only files with `.txt`, `.py`, and `.mpy` extensions will be listed
3. `code.py` and `menu.py` and any files beginning with "`.`" or "`_`" will not be listed
4. The menu will list a maximum of 26 modules (a-z). If you have more modules in your CircuitPython root, "more..." will be displayed following the "z" choice to indicate there are more items on the drive. But, the additional files won't show in the menu.
5. `ctrl+C`, `ctrl+D` will exit the current module and restart the menu. If a module ends normally, `ctrl+D` will re-run the menu.
