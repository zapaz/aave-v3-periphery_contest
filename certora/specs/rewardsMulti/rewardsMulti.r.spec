rule rewardsMultiByAssetAreInList(method f, env e, calldataarg arg) {
  require rewardsMultiAssetOne(AToken, Reward, RewardB);

  f@withrevert(e,arg);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
  assert rewardsByAsset_[1] == rewardsList_[1];
}
