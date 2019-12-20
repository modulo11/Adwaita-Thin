#!/usr/bin/env bash

set -o nounset
set -o errexit
set -o pipefail
set -o xtrace

ROOT=$PWD
TMP_DIR="$ROOT/tmp"
THEME_DIR="$TMP_DIR/Adwaita-Thin"

REPO_GTK="https://gitlab.gnome.org/GNOME/gtk.git"
REPO_GTK_TAG="3.24.13"

SASSC_OPT="-M -t compact"

# init
rm -rf $TMP_DIR && mkdir -p $TMP_DIR

# gtk

git clone --branch $REPO_GTK_TAG --depth 1 $REPO_GTK $TMP_DIR/gtk

echo "Generating css..."

sassc -M -t compact $TMP_DIR/gtk/gtk/theme/Adwaita/gtk-contained.scss $TMP_DIR/gtk.css
sassc -M -t compact $TMP_DIR//gtk/gtk/theme/Adwaita/gtk-contained-dark.scss $TMP_DIR/gtk-dark.css

# apply scaling

mkdir -p $THEME_DIR/gtk-3.0
python scale.py $TMP_DIR/gtk.css >| $THEME_DIR/gtk-3.0/gtk.css
python scale.py $TMP_DIR/gtk-dark.css >| $THEME_DIR/gtk-3.0/gtk-dark.css

# copy assets

cp -R $TMP_DIR/gtk/gtk/theme/Adwaita/assets $THEME_DIR/gtk-3.0/assets
