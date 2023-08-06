// function assetsOne2(address asset) returns bool {
//     address[] assets = getAssetsList();
//     mathint decimals = getAssetDecimals(asset);

//     return assets.length == 1
//         && assets[0] == asset
//         && decimals <= 18
//         && decimals >= 6;
// }

// function rewardsOne2(address reward) returns bool {
//     address[] rewardsList = getRewardsList();

//     return  rewardsList.length == 1
//         && rewardsList[0] == reward;
// }

// function rewardsOneAssetOne(address asset, address reward) returns bool {
//     require assets[0] == AToken;
//     address[] rewardsByAsset = getRewardsByAsset(asset);

//     return assetsOne2(asset)
//         && rewardsOne(reward)
//         && rewardsByAsset.length == 1
//         && rewardsByAsset[0] == reward
//         && getAvailableRewardsCount(asset) == 1;
// }

rule rewardOneByAssetIsInList(method f, env e, calldataarg args) filtered {
    f -> !f.isView && !harnessFunction(f)
} {
  require rewardsOneAssetsOne(AToken, Reward);

  f@withrevert(e,args);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
}

