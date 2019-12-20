# Adwaita Thin

## Sources

### gtk

* https://gitlab.gnome.org/GNOME/gtk.git
* Branch: `gtk-3-24`
* Tag: `3.24.13`
* Path: `gtk/theme/Adwaita`

Relevant files:

* `_common.scss`

Relevant variables (with values):

* `$_headerbar_height: 30px;`
* `$_entry_height: 16px;`
* `$_btn_pad: 2px 6px;`
* `$_hb_btn_pad:  5px;`
* `$_img_btn_pad: 2px;`
* `$_sel_menu_pad: 4px 10px;`
* `$_circ_btn_pad: 2px;`
* `$_switch_margin: 7px;`

Relevant attributes:

* `min-height`
    * Used vars: `$_entry_height $_headerbar_height $_slider_min_length $_marks_length`
* `padding-*`
    * Used vars: `$_img_btn_pad $_sel_menu_pad $_hb_btn_pad`

Elements to skip (retain `min-height`):

* `switch` (`switch.slider.min-height: 24px`)

# gnome-shell

* https://gitlab.gnome.org/GNOME/gnome-shell.git
* Branch: `gnome-3-34`
* Tag: `3.34.2`
* Path: `data/theme`

# gnome-themes-extra (gtk2 theme)

* https://gitlab.gnome.org/GNOME/gnome-themes-extra.git (optional)
* Branch: `gnome-3-28`
* Tag: `3.28`
