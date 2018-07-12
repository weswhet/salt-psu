## Install salt

Download latest macos salt package [here](https://repo.saltstack.com/#osx).

### configure
Clone the repo then.
``` bash
$ cd salt-psu
```
copy minion file

``` bash
$ cp minion /etc/salt/minion
```

make /srv directory

``` bash
$ sudo mkdir /srv
```

``` bash
$ sudo cp -R srv/ /srv/
```

``` bash
$ sudo launchctl stop com.saltstack.salt.minion
```

``` bash
$ sudo launchctl start com.saltstack.salt.minion
```

run some states

``` bash
sudo salt-call state.apply states/files/file-example
```

``` run the highstate
sudo salt-call state.highstate
```

