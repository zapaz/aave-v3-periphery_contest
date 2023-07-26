// function rewardsAssetLength() returns uint256 {
//   address[] rewardsAsset = getRewardsByAsset(AToken);
//   return rewardsAsset.length;
// }
// function rewardsAsset(uint256 index) returns address {
//   address[] rewardsAsset = getRewardsByAsset(AToken);
//   return rewardsAsset[index];
// }

// invariant rewardByAssetIsInList(uint256 index)
//   index < rewardsAssetLength() => inArray(rewardsAsset(index), getRewardsList());



rule rewardsByAssetAreInList(method f, env e, calldataarg arg) {
  require oneAssetMultiRewards(AToken, Reward, RewardB);

  f(e,arg);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
  assert rewardsByAsset_[1] == rewardsList_[1];
}

