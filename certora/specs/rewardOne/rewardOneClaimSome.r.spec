rule rewardOneClaimSome(env e, address user) {
    require rewardsOneAssetsOne(AToken, Reward);

    mathint currentTimestamp = e.block.timestamp;
    mathint totalSupply = AToken.totalSupply(e);
    mathint balance = AToken.balanceOf(e, user);
    mathint userIndex = getUserAssetIndex(user, AToken, Reward);
    require balance > 0;
    require totalSupply >= balance;

    mathint index;
    mathint emissionPerSecond;
    mathint lastUpdateTimestamp;
    mathint distributionEnd;
    index, emissionPerSecond, lastUpdateTimestamp, distributionEnd = getRewardsData(e, AToken, Reward);

    require index >= userIndex;
    require currentTimestamp < distributionEnd;
    require emissionPerSecond * (e.block.timestamp - lastUpdateTimestamp) > totalSupply;

    assert getUserRewards(e, getAssetsList(), user, Reward) > 0;
}
