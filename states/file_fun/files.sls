# make sure a file exits

create_fun_file:
  file.managed:
    - name: /tmp/fun_file

create_fun_file_and_directory:
  file.managed:
    - name: /tmp/salt-psu/fun_file
    - makedirs: True