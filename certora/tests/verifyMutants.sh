#!/bin/bsh

min=${1:-0}
max=${2:-$min}

CONTRACT=contracts/rewards/RewardsController.sol
cp $CONTRACT /tmp/RewardsController.sol

echo Verifying MUTANTS $min to $max

for m in certora/tests/gambit/mutants/*
do
    n=`basename $m`

    if [ $n -ge $min ] && [ $n -le $max ]; then

      cp $m/contracts/rewards/RewardsController.sol $CONTRACT

      for conf in certora/conf/*_verified.conf
      do
          MSG="MUTANT `basename $m` with `basename $conf`"
          echo Verifying $MSG
          certoraRun $conf --msg "$MSG"
      done

    fi
done

cp /tmp/RewardsController.sol $CONTRACT

