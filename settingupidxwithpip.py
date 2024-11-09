er# Create a shell.nix File
# Open or create a file named shell.nix in your project directory:

nano shell.nix

# 2. Add the Following Content to shell.nix

{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.flask
  ];
}

# CTRL + O
# enter
# CTRL + X
# Y

# 3. Activate the Nix Shell
# After saving the file, activate the Nix environment by running:

nix.shell

pip --version
python -m flask --version


# This command will download and set up the specified packages (python311, pip, flask).

# 4. Verify Installation
# Check if pip and flask are available:

pip --version
python -m flask --version

# 5. Run Your Flask Application
# Now, you can run your Flask app:

python -m flask --app main run -p $PORT --debug

# Explanation:
# shell.nix File: This file declares the environment dependencies for your project.
# pkgs.mkShell: Sets up a development shell with the specified inputs (python311, pip, and flask).
# nix-shell: Activates the environment, pulling in the dependencies specified in shell.nix.



