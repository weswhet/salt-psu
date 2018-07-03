# create just a directory.. easy right :)
create_just_a_directory:
  file.directory:
    - name: /tmp/fun-directory
    - user: root
    - group: root
    - dir_mode: 755
    - file_mode: 644
    - recurse:
      - user
      - group
      - mode