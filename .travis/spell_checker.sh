#!/bin/sh

files=$(git diff --name-only $TRAVIS_COMMIT_RANGE)
exec npx cspell --config ./spell_checker/cSpell.json --no-summary -- $files