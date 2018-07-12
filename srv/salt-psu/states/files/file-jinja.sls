# make file with
make_a_file_from_jinja:
  file.managed:
    {% if 13 in grains['osrelease_info'] %}
    - name: /tmp/salt-psu/macos_13_file
    {% elif 12 in grains['osrelease_info'] %}
    - name: /tmp/salt-psu/macos_12_file
    {% else %}
    - name: /tmp/salt-psu/macos_we_dont_know_file
    {% endif %}
    - makedirs: True
    - replace: False
  cmd.run:
    - name: echo "we made a file so we should run this command."
    - onchanges:
      - file: make_a_file_from_jinja