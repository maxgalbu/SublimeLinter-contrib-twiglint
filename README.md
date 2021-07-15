SublimeLinter-contrib-twiglint
================================

[![Build Status](https://travis-ci.org/maxgalbu/SublimeLinter-contrib-twiglint.svg?branch=master)](https://travis-ci.org/maxgalbu/SublimeLinter-contrib-twiglint)

This linter plugin for [SublimeLinter][docs] provides an interface to [twig-lint](https://github.com/asm89/twig-lint). It will be used with files that have the “twig” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. If SublimeLinter is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `twig-lint` is installed on your system. To install `twig-lint`, type the following in a terminal:

```
composer global require "asm89/twig-lint" "@stable"
```

**Note:** This plugin requires `twiglint` 1.0.1 or later.

### Linter configuration
In order for `twig-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

To make sure that `twig-lint` works, you have two choices:

- Add `~/.composer/vendor/bin` to your PATH
- Add the path to the folder where `twig-lint` is installed in the SublimeLinter user config (Preferences > Package Settings > SublimeLinter > Settings) in the “paths” key, example:

```json
{
    "paths": {
        "linux": ["~/.composer/vendor/bin"],
        "osx": ["~/.composer/vendor/bin"],
        "windows": ["C:\\Users\\yourname\\.composer\\vendor\\bin"]
    }
}
```

Once you have installed and configured `twig-lint`, you can proceed to install the SublimeLinter-contrib-twiglint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `twiglint`. Among the entries you should see `SublimeLinter-contrib-twiglint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

Twig-lint does not have any options.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
