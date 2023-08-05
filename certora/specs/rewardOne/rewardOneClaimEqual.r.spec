function rewardCalculationCVL(
  uint32 currentTimestamp,
  uint32 lastUpdateTimestamp,
  uint88 emissionPerSecond,
  uint104 assetIndex,
  uint104 userIndex,
  uint128 userAccrued,
  uint256 userBalance,
  uint256 totalSupply,
  uint256 assetUnit
  ) returns uint256 {
    uint256 userPendingIndex = require_uint256(assetIndex - userIndex);
    //  2 - 2 = 0
    //  9 - 5 = 4
    // 0xffffffffffffffffffffffffff - 0xfffffffffffffffffffffffff3 = 12

    uint256 userPending = require_uint256(userBalance * userPendingIndex / assetUnit);
    //  0 * x = 0
    // 2 250 000 * 4 / 1 000 000 = 9
    // 1 000 000 * 12 / 1 000 000 = 12

    uint256 deltaTime     = require_uint256( currentTimestamp - lastUpdateTimestamp );
    // 13 - 0 = 0
    //  9 - 0 = 9
    // 12 - 0 = 12

    uint256 deltaEmission = require_uint256( emissionPerSecond * deltaTime * assetUnit );
    // 1 * 13 * 10 gwei = 130 gwei
    // 1 * 9 * 1 000 000 = 9 000 000
    // 1 * 12 * 1 000 000 = 12 000 000

    uint256 deltaIndex    = require_uint256( deltaEmission / totalSupply );
    // 130 gwei / (130 gwei -1) = 1
    // 9 000 000 / 4 499 999 = 2
    // 12 000 000 / 1 090 909 = 11

    uint256 claimable    = require_uint256( userPending + userAccrued + userBalance );
    // uint256 claimable    = require_uint256( userPending + userAccrued + userBalance * deltaIndex / assetUnit );
    // 0 + 1 + 3 * 1 * 10 gwei = 30 gwei + 1
    // 9 + 6 + 2 250 000 * 2 / 1 000 000 = 15 + 4 = 19
    // 12 + 3 + 1 000 000 * 11 / 1 000 000 = 15 + 11 = 26

    return claimable;
    // 30 gwei + 1
    // 35 === 15
}


rule rewardOneClaimEqual(env e, address user) {
    require rewardsOneAssetOne(AToken, Reward);

    address[] assets;
    require assets[0] == AToken;
    require assets.length == 1;

    uint256 _claimable = getUserRewards(e, assets, user, Reward);

    uint256 totalSupply = AToken.scaledTotalSupply(e);
    uint8 decimals = getAssetDecimals(AToken);
    uint256 assetUnit = require_uint256(10^decimals);

    uint256 __assetIndex; uint256 _emissionPerSecond; uint256 _lastUpdateTimestamp; uint256 _distributionEnd;
    __assetIndex, _emissionPerSecond, _lastUpdateTimestamp, _distributionEnd =  getRewardsData(e, AToken, Reward);

    uint256 _assetIndex; uint256 _assetIndexOld;
    _assetIndexOld, _assetIndex = getAssetIndex(e, AToken, Reward);
    assert _assetIndexOld == __assetIndex;

    uint104 assetIndex = require_uint104(_assetIndex);
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

    uint256 claimable_ = rewardCalculation(e, currentTimestamp, lastUpdateTimestamp, emissionPerSecond,
                                           assetIndex, userIndex, userAccrued, userBalance , totalSupply, assetUnit);

    assert claimable_ == _claimable;
}


