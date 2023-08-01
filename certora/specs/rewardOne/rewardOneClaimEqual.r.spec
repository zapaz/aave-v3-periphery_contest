function rewardCalculation(
  uint32 currentTimestamp,
  uint32 lastUpdateTimestamp,
  uint88 emissionPerSecond,
  uint104 index,
  uint104 userIndex,
  uint128 userAccrued,
  uint256 userBalance,
  uint256 totalSupply,
  uint256 assetUnit
  ) returns uint256 {
    uint256 userPendingIndex = require_uint256(index - userIndex);
    uint256 userPending = require_uint256(userBalance * userPendingIndex / assetUnit);

    uint256 deltaTime     = require_uint256( currentTimestamp - lastUpdateTimestamp );
    uint256 deltaEmission = require_uint256( emissionPerSecond * deltaTime * assetUnit );
    uint256 deltaIndex    = require_uint256( deltaEmission / totalSupply );

    uint256 claimable    = require_uint256( userPending + userAccrued + userBalance * deltaIndex * assetUnit );

    return claimable;
}


rule rewardOneClaimEqual(env e, address user) {
    require rewardsOneAssetOne(AToken, Reward);

    uint256 _claimable = getUserRewards(e, getAssetsList(), user, Reward);

    uint256 totalSupply = AToken.scaledTotalSupply(e);
    uint8 decimals = getAssetDecimals(AToken);
    uint256 assetUnit = require_uint256(10^decimals);

    uint256 _index; uint256 _emissionPerSecond; uint256 _lastUpdateTimestamp; uint256 _distributionEnd;
    _index, _emissionPerSecond, _lastUpdateTimestamp, _distributionEnd =  getRewardsData(e, AToken, Reward);

    uint104 index = require_uint104(_index);
    uint88 emissionPerSecond = require_uint88(_emissionPerSecond);
    uint32 lastUpdateTimestamp = require_uint32(_lastUpdateTimestamp);
    uint32 distributionEnd = require_uint32(_distributionEnd);
    uint32 currentTimestamp = require_uint32(e.block.timestamp);

    uint128 userAccrued = require_uint128(getUserAccruedRewards(user, Reward));
    uint104 userIndex = require_uint104(getUserAssetIndex(user, AToken, Reward));
    uint256 userBalance = AToken.balanceOf(e, user);

    require userBalance > 0;
    require totalSupply > userBalance;
    require currentTimestamp < distributionEnd;
    require currentTimestamp > lastUpdateTimestamp;

    uint256 claimable = rewardCalculation(currentTimestamp, lastUpdateTimestamp, emissionPerSecond,
                                           index, userIndex, userAccrued, userBalance , totalSupply, assetUnit);


    assert claimable == _claimable;
}


