# etcd-raft-example

a simple etcd raft example

## usage

```sh
go mod download
go test

go install github.com/mattn/goreman@latest
goreman start

go test -benchmem -run=^$ -bench ^BenchmarkCommit$ github.com/117503445/etcd-raft-example

./build-run.sh
```

## doc

<https://github.com/etcd-io/etcd/tree/main/contrib/raftexample>

<https://github.com/etcd-io/etcd/tree/main/raft>

## License

most code from <https://github.com/etcd-io/etcd/tree/main/contrib/raftexample>

etcd-raft-example is under the Apache 2.0 license. See the LICENSE file for details.
