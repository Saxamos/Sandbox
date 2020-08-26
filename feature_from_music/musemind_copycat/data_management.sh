# recursively lowercase
rename --lower-case --force ./feature_from_music/musemind_copycat/data/**/*

# replace space by underscore
find ./feature_from_music/musemind_copycat/data -depth -name "* *" -execdir rename 's/ /_/g' "{}" \;