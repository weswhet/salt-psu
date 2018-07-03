# Salt Top File.

base:
  'os:MacOS':  # Target everything running MacOS.
    - match: grain
    - states
