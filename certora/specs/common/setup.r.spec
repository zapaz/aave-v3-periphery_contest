rule setupAssetImmutable(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    address[] _assetsList = getAssetsList();
    uint256 _assetsListLength = _assetsList.length;
    uint256 index;
    require index < _assetsListLength;

    address _asset = _assetsList[index];

    f@withrevert(e, args);

    address[] assetsList_ = getAssetsList();
    uint256 assetsListLength_ = assetsList_.length;
    address asset_ = assetsList_[index];

    assert asset_ == _asset;
    assert assetsListLength_ >= _assetsListLength;
}

rule setupAssetsAdded(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    address[] _assetsList = getAssetsList();
    mathint _assetsListLength = _assetsList.length;

    f@withrevert(e, args);

    address[] assetsList_ = getAssetsList();
    mathint assetsListLength_ = assetsList_.length;

    assert assetsListLength_ != _assetsListLength
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector );
}

rule setupAssetsImmutable(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    address[] _assetsList = getAssetsList();
    mathint _assetsListLength = _assetsList.length;
    uint256 index;
    require index < _assetsListLength;

    address _asset = _assetsList[index];

    f@withrevert(e, args);

    address[] assetsList_ = getAssetsList();
    mathint assetsListLength_ = assetsList_.length;
    address asset_ = assetsList_[index];

    assert assetsListLength_ >= _assetsListLength;
}

rule setupRewardModified(method f, env e, calldataarg args, address asset, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    uint256 _index; uint256 _emissionPerSecond; uint256 _lastUpdateTimestamp; uint256 _distributionEnd;
    _index, _emissionPerSecond, _lastUpdateTimestamp, _distributionEnd =  getRewardsData(e, asset, reward);

    f@withrevert(e, args);

    uint256 index_; uint256 emissionPerSecond_; uint256 lastUpdateTimestamp_; uint256 distributionEnd_;
    index_, emissionPerSecond_, lastUpdateTimestamp_, distributionEnd_ =  getRewardsData(e, asset, reward);

    assert emissionPerSecond_ != _emissionPerSecond
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||   (  ( f.selector == sig:setEmissionPerSecond(address,address[],uint88[]).selector )
           && ( _lastUpdateTimestamp != 0 ) );

    assert distributionEnd_ != _distributionEnd
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setDistributionEnd(address,address,uint32).selector             ) );
}

rule setupTransferStrategy(method f, env e, calldataarg args, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _transferStrategy = getTransferStrategy(reward);
    f@withrevert(e, args);
    address transferStrategy_ = getTransferStrategy(reward);

    assert transferStrategy_ != _transferStrategy
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   transferStrategy_ != 0
      &&   isContract(transferStrategy_)
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setTransferStrategy(address,address).selector                   ) );
}

rule setupRewardOracle(method f, env e, calldataarg args, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _rewardOracle = getRewardOracle(reward);
    f@withrevert(e, args);
    address rewardOracle_ = getRewardOracle(reward);

    assert rewardOracle_ != _rewardOracle
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setRewardOracle(address,address).selector                       ) );
}

rule setupClaimer(method f, env e, calldataarg args, address user) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _claimer = getClaimer(user);
    f@withrevert(e, args);
    address claimer_ = getClaimer(user);

    assert claimer_ != _claimer
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:setClaimer(address,address).selector );
}

