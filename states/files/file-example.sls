# make simple file with some content
make_a_file:
  file.managed:
    - name: /tmp/salt-psu/file_to_manage
    - makedirs: True
    - contents:
      - We made a file with this string on the first line
      - That was pretty easy! right?!?
  cmd.run:
    - name: echo "we just ran a sweet command"
    - onchanges:
      - file: /tmp/salt-psu/file_to_manage
