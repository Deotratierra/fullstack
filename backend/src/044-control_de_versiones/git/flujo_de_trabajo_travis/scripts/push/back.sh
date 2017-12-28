#!/bin/bash

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

git checkout -b master
git add .
git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"

git push --quiet --set-upstream origin master