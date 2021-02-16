git add .
git reset master --soft || exit 1
git commit || exit 1
git checkout master || exit 1
git merge tcr || exit 1