rule claimRewardsReverts(env e, address[] assets, uint256 amount, address to, address reward){
  uint256 claimed = 0;

  claimed = claimRewards@withrevert(e, assets, amount, to, reward);

  assert ( to == 0 )            => lastReverted;

  assert ( assets.length == 0 ) => claimed == 0;
  assert ( amount == 0 )        => claimed == 0;
  assert ( reward == 0 )        => claimed == 0;
  assert ( ( assets.length == 1 ) && ( assets[0] == 0 )  ) => claimed == 0;
}

rule claimRewardsOnBehalfReverts(env e, address[] assets, uint256 amount, address user, address to, address reward){
  claimRewardsOnBehalf@withrevert(e, assets, amount, user, to, reward);

  assert ( to == 0   )          => lastReverted;
  assert ( user == 0 )          => lastReverted;
}

rule claimAllRewardsReverts(env e, address[] assets, address to){
  claimAllRewards@withrevert(e, assets, to);

  assert ( to == 0 )            => lastReverted;
}

rule claimAllRewardsOnBehalfReverts(env e, address[] assets, address user, address to){
  claimAllRewardsOnBehalf@withrevert(e, assets, user, to);

  assert ( to == 0 )            => lastReverted;
  assert ( user == 0 )          => lastReverted;
}
