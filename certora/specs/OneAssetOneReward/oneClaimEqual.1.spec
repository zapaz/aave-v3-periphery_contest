rule oneClaimEqual(env e, address user, address to) {
    require oneAssetOneReward(AToken, Reward);
    requireInvariant user_index_LEQ_index(AToken, Reward, user);
    require getTransferStrategy(Reward) != to;

    uint256 totalSupply = AToken.scaledTotalSupply(e);
    uint256 balance = AToken.balanceOf(e, user);
    uint8 decimals = getAssetDecimals(AToken);
    uint256 assetUnit = require_uint256(10^decimals);
    require balance > 0;
    require totalSupply >= balance;

    uint128 __userAccrued = require_uint128(getUserAccruedRewards(user, Reward));
    uint104 __userIndex = require_uint104(getUserAssetIndex(user, AToken, Reward));

    handleAction(e, user, totalSupply, balance);

    uint128 _userAccrued = require_uint128(getUserAccruedRewards(user, Reward));
    uint104 _userIndex = require_uint104(getUserAssetIndex(user, AToken, Reward));

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + _amount);

    uint256 _index; uint256 _emissionPerSecond; uint256 _lastUpdateTimestamp; uint256 _distributionEnd;
    _index, _emissionPerSecond, _lastUpdateTimestamp, _distributionEnd =  getRewardsData(e, AToken, Reward);
    uint104 index = require_uint104(_index);
    uint88 emissionPerSecond = require_uint32(_emissionPerSecond);
    uint32 lastUpdateTimestamp = require_uint32(_lastUpdateTimestamp);
    uint32 distributionEnd = require_uint32(_distributionEnd);

    require require_uint32(e.block.timestamp) < distributionEnd;
    require require_uint32(e.block.timestamp) > lastUpdateTimestamp;

    uint104 deltaUserIndex = require_uint104(index - _userIndex);
    uint256 _indexClaimable = require_uint256(_balance * deltaUserIndex / assetUnit);

    uint32 deltaTime     = require_uint32( e.block.timestamp - lastUpdateTimestamp );
    uint256 deltaEmission = require_uint256( emissionPerSecond * deltaTime * assetUnit );
    uint104 deltaIndex    = require_uint104( deltaEmission / totalSupply );

    uint256 _claimable    = require_uint256( _indexClaimable + _userAccrued + balance * deltaIndex * assetUnit );

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, getAssetsList(), user, to);
    uint256 claimable_ = amounts_[0];

    uint128 userAccrued_ = require_uint128(getUserAccruedRewards(user, Reward));
    uint104 userIndex_ = require_uint104(getUserAssetIndex(user, AToken, Reward));
    uint256 balance_ = Reward.balanceOf(e, to);

    assert rewards_[0] == Reward;
    assert claimable_ == _amount;
    assert balance_ == _balancePlusAmount;
    assert _claimable == claimable_;
}


