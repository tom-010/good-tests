#!/bin/bash

# switch (and create) to tcr branch to protect the git history
(git checkout -b tcr || git checkout tcr) || exit 1

# commit resets tcr branch and add the canges of it with a nice message -> update to it
git merge master || exit 1

# step tcr on every detected change
./scripts/watch.sh ./scripts/step_tcr.sh