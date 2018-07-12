# ensure catalog is default
set_catalog_to_default:
  softwareupdate.set_catalog:
    - name: Default

# make sure scheduled updates are on.
turn_on_them_updates:
  softwareupdate.schedule:
    - name: 'on'