#!/bin/bash

(git checkout -b tcr || git checkout tcr) || exit 1

./scripts/watch.sh ./scripts/tcr_now.sh