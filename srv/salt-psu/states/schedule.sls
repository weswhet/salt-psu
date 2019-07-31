# schedule for the highstate run
minion_highstate_schedule:
  schedule.present:
    - name: highstate
    - run_on_start: True
    - function: state.highstate
    - minutes: 5
    - maxrunning: 1
    - enabled: True
    - returner: rawfile_json
    - splay: 0
