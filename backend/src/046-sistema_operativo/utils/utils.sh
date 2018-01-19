#!/bin/bash

# ====================================================

# Saber si existe un comando
command_exists() {
	command -v "$@" > /dev/null 2>&1
}

if command_exists docker; then
  echo "El comando 'docker' existe en tu sistema."
else
  echo "El comando 'docker no existe en tu sistema."
fi

# ====================================================

# Saber el usuario
id -un 2>/dev/null || true

# ====================================================

# Saber si el usuario puede loguearse como root

user="$(id -un 2>/dev/null || true)"

sh_c='sh -c'
if [ "$user" != 'root' ]; then
	if command_exists sudo; then
		sh_c='sudo -E sh -c'
	elif command_exists su; then
		sh_c='su -c'
	else
		cat >&2 <<-'EOF'
		Error: this installer needs the ability to run commands as root.
		We are unable to find either "sudo" or "su" available to make this happen.
		EOF
		exit 1
	fi
fi

# ====================================================