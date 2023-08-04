function rewardsCount (address asset) returns uint256 {
    address[] rewards = getRewardsByAsset(asset);
    return rewards.length;
}

function rewardsOne(address reward) returns bool {
    address[] rewardsList = getRewardsList();

    return  rewardsList.length == 1
        && rewardsList[0] == reward;
}

function rewardsOneAssetOne(address asset, address reward) returns bool {
    address[] rewardsByAsset = getRewardsByAsset(asset);

    return assetsOne(asset)
        && rewardsOne(reward)
        && rewardsByAsset.length == 1
        && rewardsByAsset[0] == reward
        && getAvailableRewardsCount(asset) == 1;
}

function rewardsMulti(address reward1, address reward2) returns bool {
    address[] rewardsList = getRewardsList();

    return rewardsList.length == 2
        && rewardsList[0] == reward1
        && rewardsList[1] == reward2;
}

function rewardsMultiAssetOne(address asset, address reward1, address reward2) returns bool {
    address[] rewardsByAsset = getRewardsByAsset(asset);

    return assetsOne(asset)
        && rewardsMulti(reward1, reward2)
        && rewardsByAsset.length == 2
        && rewardsByAsset[0] == reward1
        && rewardsByAsset[1] == reward2
        && getAvailableRewardsCount(asset) == 2;
}


rule availableRewardsCountIncrease(method f, env e, calldataarg args, address asset)  filtered { f -> !f.isView } {
    uint256 _availableRewardsCount = getAvailableRewardsCount(asset);
    f@withrevert(e, args);
    uint256 availableRewardsCount_ = getAvailableRewardsCount(asset);

    assert availableRewardsCount_ >= _availableRewardsCount;
}

invariant indexIncreaseWithSomeAvailableReward(address asset, address reward)
    getAssetIndex(asset, reward) > 0 => getAvailableRewardsCount(asset) > 0;

invariant userIndexIncreaseWithSomeAvailableReward(address user, address asset, address reward)
    getUserAssetIndex(user, asset, reward) > 0 => getAvailableRewardsCount(asset) > 0;



