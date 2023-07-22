import "methods/Methods_base.spec";
import "methods/Methods_more.spec";

using DummyERC20_rewardTokenB as RewardB;

///////////////// Properties ///////////////////////

rule zeroAddressAssetUnchanged(method f, env e, calldataarg args) {
  require e.msg.sender != 0;

  uint _balance = AToken.balanceOf(e, 0);
  f(e, args);
  uint balance_ = AToken.balanceOf(e, 0);

  assert balance_ == _balance;
}

rule zeroAddressRewardUnchanged(method f, env e, calldataarg args) {
  require e.msg.sender != 0;

  uint _balance = Reward.balanceOf(e, 0);
  f(e, args);
  uint balance_ = Reward.balanceOf(e, 0);

  assert balance_ == _balance;
}

rule cannotSetTransferStrategyToZero(method f, env e, calldataarg args) {
  address _transferStrategy = getTransferStrategy(Reward);
  f(e, args);
  address transferStrategy_ = getTransferStrategy(Reward);

  assert _transferStrategy != 0 => transferStrategy_ != 0 ;
}

rule cannotSetRewardOracleWithoutPrice(method f, env e, calldataarg args) {
  address _rewardOracle = getRewardOracle(e, Reward);
  f(e, args);
  address rewardOracle_ = getRewardOracle(e, Reward);

  assert _rewardOracle != 0  => rewardOracle_ != 0 ;
}
