function oneAsset(address asset) returns bool {
    address[] assetsList = getAssetsList();
    uint256 decimals = getAssetDecimals(asset);
    require getAvailableRewardsCount(asset) == 1;

    return assetsList.length == 1
        && assetsList[0] == asset
        && decimals <= 18
        && decimals >= 6;
}

function oneReward(address reward) returns bool {
    address[] rewardsList = getRewardsList();
    address[] rewardsByAsset = getRewardsByAsset(AToken);

    return rewardsByAsset.length == 1
        && rewardsByAsset[0] == reward
        && rewardsList.length == 1
        && rewardsList[0] == reward
        && getAvailableRewardsCount(AToken) == 1;
}

function oneAssetOneReward(address asset, address reward) returns bool {
  return oneAsset(asset) && oneReward(reward);
}
