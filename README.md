# etcd-raft-example

a simple etcd raft example

## usage

```sh
go mod download
go test

go install github.com/mattn/goreman
goreman start

go test -benchmem -run=^$ -bench ^BenchmarkCommit$ github.com/117503445/etcd-raft-example
```

## License

etcd-raft-example is under the Apache 2.0 license. See the LICENSE file for details.
