rule setupConfig(env e, calldataarg args) {
    address[] _assets = getAssetsList();

    require EMISSION_MANAGER() == currentContract;   // must be emmission manager to call external function harnessed
    require getlastUpdateTimestamp(AToken,Reward) == 0;
    require getAvailableRewardsCount(AToken) == 0;
    require getAssetDecimals(AToken) == 0;
    require AToken.decimals(e) > 0;
    require _assets.length == 0;
    require isRewardEnabled(Reward) == false;

    configureAsset(AToken, Reward, TransferStrategy);

    address[] assets_ = getAssetsList();
    address asset_     = assets_[0];
    address[] rewards_ = getRewardsByAsset(asset_);
    address reward_    = rewards_[0];

    assert getTransferStrategy(Reward) == TransferStrategy;
    assert getRewardOracle(Reward) == rewardOracle();
    assert assets_.length == 1;
    assert rewards_.length == 1;
    assert asset_ == AToken;
    assert reward_ == Reward;
    assert getAvailableRewardsCount(AToken) == 1;
    assert getAssetDecimals(AToken) == AToken.decimals(e);
    assert isRewardEnabled(Reward) == true;
}

rule setupAssetsAdded(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    address[] _assets = getAssetsList();
    uint256 _assetsLength = _assets.length;

    f(e, args);

    address[] assets_ = getAssetsList();
    uint256 assetsLength_ = assets_.length;

    assert assetsLength_ != _assetsLength
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector );
}

rule setupRewardModified(method f, env e, calldataarg args, address asset, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    address[] _assets = getAssetsList();

    uint256 _index; uint256 _emissionPerSecond; uint256 _lastUpdateTimestamp; uint256 _distributionEnd;
    _index, _emissionPerSecond, _lastUpdateTimestamp, _distributionEnd =  getRewardsData(e, asset, reward);

    f(e, args);

    uint256 index_; uint256 emissionPerSecond_; uint256 lastUpdateTimestamp_; uint256 distributionEnd_;
    index_, emissionPerSecond_, lastUpdateTimestamp_, distributionEnd_ =  getRewardsData(e, asset, reward);

    assert emissionPerSecond_ != _emissionPerSecond
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||   ( f.selector == sig:setEmissionPerSecond(address,address[],uint88[]).selector );

    assert distributionEnd_ != _distributionEnd
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setDistributionEnd(address,address,uint32).selector             ) );
}

rule setupTransferStrategy(method f, env e, calldataarg args, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _transferStrategy = getTransferStrategy(reward);
    f(e, args);
    address transferStrategy_ = getTransferStrategy(reward);

    assert transferStrategy_ != _transferStrategy
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setTransferStrategy(address,address).selector                   ) );
}

rule setupRewardOracle(method f, env e, calldataarg args, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _rewardOracle = getRewardOracle(reward);
    f(e, args);
    address rewardOracle_ = getRewardOracle(reward);

    assert rewardOracle_ != _rewardOracle
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setRewardOracle(address,address).selector                       ) );
}
