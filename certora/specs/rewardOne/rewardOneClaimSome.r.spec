/////////////////////////////////////////////////////////////////////////////////
// Ensure you can get rewards when all requirements are met
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimSome(env e, address user) {
    require rewardsOneAssetsOne(AToken, Reward);

    mathint currentTimestamp = e.block.timestamp;
    mathint totalSupply = AToken.totalSupply(e);
    mathint balance = AToken.balanceOf(e, user);
    mathint userIndex = getUserAssetIndex(user, AToken, Reward);
    mathint assetIndex;
    mathint emissionPerSecond;
    mathint lastUpdateTimestamp;
    mathint distributionEnd;
    assetIndex, emissionPerSecond, lastUpdateTimestamp, distributionEnd = getRewardsData(e, AToken, Reward);

    require balance > 0;
    require totalSupply >= balance;
    require assetIndex >= userIndex;
    require currentTimestamp < distributionEnd;
    require emissionPerSecond * (e.block.timestamp - lastUpdateTimestamp) > totalSupply;

    assert getUserRewards(e, getAssetsList(), user, Reward) > 0;
}
