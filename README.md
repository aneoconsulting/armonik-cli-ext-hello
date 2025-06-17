# ArmoniK.CLI Hello Extension

This repository is an example implementation of a simple ArmoniK.CLI extension. It implements the `say` command under the `hello` command group.

```sh
armonik hello say
```

This project uses `uv` for tooling and `hatchling` for builds, but you're free to use whatever you're comfortable with as long as you respect the guidelines outlined in the ArmoniK.CLI Extensions documentation.

# Installation:

Since this is an example extension, we don't publish it to PyPI.

## From Source

1. Clone this repository
2. Install it in the **same (virtual) environment** as your ArmoniK.CLI installation. So if you installed it from pip you'd typically do.
```sh
pip install <path-to-this-repo> -e
```

or for a uv virtual environment (working with the ArmoniK.CLI source)

```sh
uv pip install <path-to-this-repo> -e
```

3. Edit away!
