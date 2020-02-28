#!/bin/sh

files=$(git diff --name-only HEAD^)
exec npx cspell --no-summary -- $files