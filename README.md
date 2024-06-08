# RedLabs CLI


## Deploy the Infrastructure



## Command Help

```console
rfs@debian:~$ redlabs --help

redlabs --help
redlabs --install
redlabs --config

- c2-cs
- c2-mythic

redlabs --local

- Vmware
- ProxMox
- Linux Box (Any)

```

## C2 Servers


### Install Locally

#### Install a Cobalt Strike C2 Locally
1 - Install it
```console
rfs@debian:~$ redlabs --install c2-cs --local
```

#### Config a Cobalt Strike C2 Locally
2- Then configure it!
```console
rfs@debian:~$ redlabs --config c2-cs
```

### Cloud Install
```console
rfs@debian:~$ redlabs --config web --aws
```
