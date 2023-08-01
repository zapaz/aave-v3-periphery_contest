
rule rewardOneByAssetIsInList(method f, env e, calldataarg arg) {
  require rewardsOneAssetOne(AToken, Reward);

  f@withrevert(e,arg);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
}

