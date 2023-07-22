function rewardsAssetLength() returns uint256 {
  address[] rewardsAsset = getRewardsByAsset(AToken);
  return rewardsAsset.length;
}
function rewardsAsset(uint256 index) returns address {
  address[] rewardsAsset = getRewardsByAsset(AToken);
  return rewardsAsset[index];
}

invariant rewardByAssetIsInList(uint256 index)
  index < rewardsAssetLength() => inArray(rewardsAsset(index), getRewardsList());

