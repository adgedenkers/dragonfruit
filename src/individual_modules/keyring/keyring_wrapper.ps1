param (
    [string]$action,
    [string]$namespace,
    [string]$name,
    [string]$secret
)

# Define the path to your Python script
$PYTHON_SCRIPT_PATH = "keyring_manager.py"

# Function to validate the parameters and execute the Python script
function Invoke-KeyringManager {
    if (-not $action -or -not $namespace -or -not $name) {
        Write-Error "Insufficient arguments provided."
        Write-Host "Usage: "
        Write-Host "  .\wrapper.ps1 -action [set|get|delete] -namespace [namespace] -name [name] [-secret [secret]]"
        exit
    }

    $arguments = @($action, $namespace, $name)

    if ($action -eq "set" -and $secret) {
        $arguments += $secret
    }

    python.exe $PYTHON_SCRIPT_PATH $arguments
}

# Invoke the function with the provided parameters
Invoke-KeyringManager
