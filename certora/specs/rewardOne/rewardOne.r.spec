
rule rewardOneByAssetIsInList(method f, env e, calldataarg args) filtered {
    f -> !f.isView && !harnessFunction(f)
} {
  require rewardsOneAssetOne(AToken, Reward);

  f@withrevert(e,args);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
}

