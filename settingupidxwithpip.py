# Create a shell.nix File
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

