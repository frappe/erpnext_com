#!/bin/sh

files=$(git diff --name-only $TRAVIS_COMMIT_RANGE)
echo $files
exec npx cspell --no-summary -- $files