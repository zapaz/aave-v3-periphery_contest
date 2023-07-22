import "./oneFunctions.spec";

function oneClaimRewardExpectedAmount(env e, address user, address asset, address reward) returns uint256 {
    require oneAssetOneReward(asset, reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, getAssetsList(), user);

    assert rewards[0] == reward;

    return amounts[0];
}

function oneClaimFirstRewardExpectedAmount(env e, address user) returns uint256 {
    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, getAssetsList(), user);

    return amounts[0];
}


