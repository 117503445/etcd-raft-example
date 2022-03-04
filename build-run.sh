rm -r ./data

set -e # exit when fail

go build
goreman start

