#!/bin/sh
set -e
GITHUB_TOKEN="2"
INPUT_BRANCH=${INPUT_BRANCH:-$GITHUB_TOKEN}
INPUT_FORCE=${INPUT_FORCE:-false}
INPUT_TAGS=${INPUT_TAGS:-false}
INPUT_DIRECTORY=${INPUT_DIRECTORY:-'.'}
_FORCE_OPTION=''
REPOSITORY=${INPUT_REPOSITORY:-$GITHUB_REPOSITORY}

echo "Push to branch $INPUT_BRANCH";
GITHUB_TOKEN="2"
echo 'Missing input "github_token: ${{ GITHUB_TOKEN }}".';