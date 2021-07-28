# Ansible Role: goquorum

### Description
Ansible role that will install, configure and runs GoQuorum

### Table of Contents
  - [Supported Platforms](#supported-platforms)
  - [Dependencies](#dependencies)
  - [Role Variables](#role-variables)
  - [Example Playbook](#example-playbook)
  - [License](#license)
  - [Author Information](#author-information)

### Supported Platforms
```
* Debian
* Ubuntu
* Redhat(CentOS/Fedora)
* Amazon
```

### Dependencies

* Go 1.13.x or greater

### Role Variables:

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file. By and large these variables are configuration options. Please refer to the GoQuorum [docs](https://docs.goquorum.consensys.net/en/latest/) for more information

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `goquorum_version` | ___unset___ |  Version of GoQuorum to install and run. All available versions are listed on our GoQuorum [releases](https://github.com/ConsenSys/doc.goquorum/releases) page |
| `goquorum_user` | goquorum | GoQuorum user |
| `goquorum_group` | goquorum | GoQuorum group |
| `goquorum_download_url` | https://artifacts.consensys.net/public/go-quorum/raw/versions/{{ goquorum_version }}/geth_{{ goquorum_version }}_{{ goquorum_architecture }}_amd64.tar.gz | The download tar.gz file used. You can use this if you need to retrieve goquorum from a custom location such as an internal repository. |
| `goquorum_install_dir` | /opt/goquorum | Path to install to  |
| `goquorum_config_dir` | /etc/goquorum | Path for default configuration |
| `goquorum_node_private_key_file` | "" | Path for node private key, if supplied. This needs to include the node key file name and path like so `/home/me/me_node/myPrivateKey`. If not supplied GoQuorum will create one automatically |
| `goquorum_data_dir` | /opt/goquorum/data | Path for data directory|
| `goquorum_log_dir` | /var/log/goquorum | Path for logs |
| `goquorum_profile_file` | /etc/profile.d/goquorum-path.sh | Path to allow loading GoQuorum into the system PATH |
| `goquorum_managed_service` | true | Enables a systemd service |
| `goquorum_systemd_dir` | /etc/systemd/system/ | The default systemd directory |
| `goquorum_systemd_state` | restarted | The default option for the systemd service state |
| `goquorum_node_identity` | GoQuorumNode  | Identity of the node |
| `goquorum_host_ip` | "" | The host IP that GoQuorum uses for the P2P network. This specifies the host on which P2P listens |
| `goquorum_discovery_public_ip` | false | Spefies whether the node should use the public IP of the host in cloud (AWS,Azure,GCP). In private networks, the private IP is more secure and faster for traffic to route  |
| `goquorum_max_peers` | 50 | The maximum number of P2P connections you can establish |
| `goquorum_genesis_path` | "" | The path to the genesis file |
| `goquorum_network_id` | 1337 | The id of the network, also specified in the genesis file |
| `goquorum_sync_mode` | full | Specifies the synchronization mode. Other values are 'fast' |
| `goquorum_log_verbosity` | 3 | The log level to use. Other log levels are 0=silent, 1=error, 2=warn, 3=info, 4=debug, 5=detail |
| `goquorum_miner_enabled` | false | Enables mining when the node is started |
| `goquorum_miner_threads` | 1 | Number of CPU threads to use for mining |
| `goquorum_miner_etherbase` | 0 | Public address for block mining rewards (default = first account)  |
| `goquorum_min_gas` | 0 | Minimum gas price for mining a transaction |
| `goquourm_gas_ceil` | 800000000 | Target gas ceiling for mined blocks |
| `goquourm_gas_floor` | 700000000 | Target gas floor for mined blocks  |
| `goquorum_metrics_enabled` | true | Enable collection of prometheus metrics |
| `goquorum_metrics_host` | 0.0.0.0 | pprof HTTP server listening interface |
| `goquorum_metrics_port` | 9545 | pprof HTTP server listening port |
| `goquorum_p2p_port` | 30303 | Specifies the P2P listening ports (UDP and TCP). Ports must be exposed appropriately |
| `goquorum_http_enabled` | true | Enabled the HTTP JSON-RPC service |
| `goquorum_http_host` | 127.0.0.1 | Specifies the host on which HTTP JSON-RPC listens |
| `goquorum_http_port` | 8545 | Specifies the port on which HTTP JSON-RPC listens |
| `goquorum_http_api` | ["admin","db","eth","debug","miner","net","shh","txpool","personal","web3","quorum","istanbul"] | Comma-separated APIs to enable on the HTTP JSON-RPC channel. When you use this option, the `goquorum_rpc_http_enabled` option must also be enabled |
| `goquorum_http_cors_origins` | ["all"] | Comma separated list of domains from which to accept cross origin requests |
| `goquorum_http_virtual_hosts` | ["all"] | Comma separated list of virtual hostnames from which to accept requests |
| `goquorum_ws_enabled` | true | Enabled the WebSockets service |
| `goquorum_ws_api` | ["admin","db","eth","debug","miner","net","shh","txpool","personal","web3","quorum","istanbul"] | Comma-separated APIs to enable on the HTTP JSON-RPC channel. When you use this option, the `goquorum_rpc_ws_enabled` option must also be enabled |
| `goquorum_ws_host` | 0.0.0.0 | Specifies the host on which WebSockets listens |
| `goquorum_ws_port` | 8546 | Specifies Websockets JSON-RPC listening port (TCP). Port must be exposed appropriately |
| `goquorum_ws_origins` | ["all"] | Comma separated list of domains from which to accept websockets requests |
| `goquorum_graphql_enabled` | true | Enabled the HTTP JSON-RPC service |
| `goquorum_graphql_cors_origins` | ["all"] | Comma separated list of domains from which to accept cross origin requests |
| `goquorum_graphql_virtual_hosts` | ["all"] | Comma separated list of virtual hostnames from which to accept requests |
| `goquorum_bootnodes` | [] | List of comma-separated enode URLs for P2P discovery bootstrap |
| `goquorum_no_discovery` | true | Disable P2P discovery |
| `goquorum_enable_node_permissions` | "true" | Enable permissioning. Please note that you must provide the necessary [permissions-config.json file](https://docs.goquorum.consensys.net/en/latest/Concepts/Permissioning/BasicNetworkPermissions/) |
| `goquorum_ptm_enabled` | false | Enable privacy |
| `goquorum_ptm_url` | "http://127.0.0.1:9101" | URL to contact to Tessera on including port eg: `http://localhost:9101` |
| `goquorum_user_cmdline_args` | "" | Command line args that are passed in from the user |
| `goquorum_env_opts` | [] | Settings passed to the JVM through `BESU_OPTS` environment variable. eg: `[-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005]s` |
| `goquorum_unlock` | 0 | Comma separated list of accounts to unlock |
| `goquorum_account_password_file` | "" | Password file to use for non-interactive password input |

### Example Playbook

1. Install via github

```
ansible-galaxy install git+https://github.com/consensys/ansible-role-goquorum.git
```

Create a requirements.yml with the following:
Replace `x.y.z` below with the version you would like to use 
```
---
- hosts: localhost
  connection: local
  force_handlers: True

  roles:
  - role: ansible-role-goquorum
    vars:
      goquorum_version: vX.Y.Z
```

Run with ansible-playbook:
```
ansible-playbook -v /path/to/requirements.yml
```


### License

Apache


### Author Information

Consensys, 2021
