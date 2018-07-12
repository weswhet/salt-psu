#!py

def run():
    # make an empty dictionary to add our states too
    config = {}
    # a list of file names.
    files_to_make = ['foo', 'bar', 'baz', 'bat', 'ball', 'banana']
    # loop through our list of files to make and add each state to the config
    # dictionary
    for file in files_to_make:
        config['make_file_{}'.format(file)] = {
            'file.managed': [
                {'name': '/tmp/salt-psu/{}'.format(file)},
                {'makedirs': True},
                {'contents': [
                    'We made a file {}, this string is on the first line'.format(file),
                    'That was pretty easy! right?!??'
                    ]
                },
            ],
        }
    # return our config dictionary of all our states
    return config