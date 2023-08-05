rule rewardsTwoByAssetAreInList(method f, env e, calldataarg args) filtered {
    f -> !f.isView && !harnessFunction(f)
} {
  require rewardsTwoAssetOne(AToken, Reward, RewardB);

  f@withrevert(e,args);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
  assert rewardsByAsset_[1] == rewardsList_[1];
}
