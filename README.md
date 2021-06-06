# SublimeText

This is my personal SublimeText settings.

## Prerequisites

- SublimeText with Package Control

## Installation

```sh
git clone git@github.com:ninth-dev/SublimeText.git "${HOME}/Library/Application Support/Sublime Text/Packages/User"
```

### Scala 3 Syntax Support

This is a **temporary measure** until there are updates in the [Official Default Packages]((https://github.com/sublimehq/Packages/issues/2795)).

Ported over Scala 3 from [vscode-scala-syntax](https://github.com/scala/vscode-scala-syntax) and slightly modified.

- See [Scala.sublime-syntax](./Scala3/Scala.sublime-syntax)
- The `Mariana.sublime-color-scheme` has also been extended.

#### How to convert `.tmLanguage` to `.sublime-syntax` ?

**Prerequisites**

- `PackageDev` plugin

1. Open a `.tmLanguage.json` or `.tmLanguage.yaml` file.

   - If you already have the `.tmLanguage` file, then skip to step 5.

1. Press `Cmd` + `Shift` + `P`
1. Search for `PackageDev: Convert (YAML, JSON, PList) to and select Convert to: Property List`
1. Rename the file to just `.tmLanguage` instead of `.tmLanguage.plist`
1. Open the `.tmLanguage` file, press `Cmd` + `Shift` + `P`
1. Search for `Plugin Development: Convert Syntax to .sublime-syntax`

** Source: https://github.com/slimsag/Packages#adding-a-new-language **

## License

[MIT](https://choosealicense.com/licenses/mit/)
