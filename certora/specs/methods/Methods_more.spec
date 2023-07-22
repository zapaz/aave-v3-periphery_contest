using DummyERC20_rewardToken as Reward;

methods {
  // More RewardsController
  function getAssetDecimals(address)          external returns (uint8)      envfree;
  function getRewardsByAsset(address)         external returns (address[])  envfree;
  function getRewardsList()                   external returns (address[])  envfree;
  function getTransferStrategy(address)       external returns (address)    envfree;
  // More RewardsControllerHarness
  function getAssetsList()                    external returns (address[])  envfree;
  function getAvailableRewardsCount(address)  external returns (uint128)    envfree;
}
