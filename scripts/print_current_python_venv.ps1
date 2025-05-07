<#
    .DESCRIPTION
    This is just a helper script you can run to easily determine which python virtual environment you're currently in.
    This is especially useful when using newer versions of vscode where the terminal prompt no longer shows the venv name in parenthesis, like `(venv)`.

    Usage:
    From your terminal (or whatever terminal or shell you want to check your env), just call this powershell script by calling its path.

    For example:
    .\scripts\print_current_python_venv.ps1
#>
echo $env:VIRTUAL_ENV