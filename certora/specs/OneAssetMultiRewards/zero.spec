rule zeroAddressAssetUnchanged(method f, env e, calldataarg args) filtered {
   f -> !f.isView
}{
  require e.msg.sender != 0;

  uint _balance = AToken.balanceOf(e, 0);
  f(e, args);
  uint balance_ = AToken.balanceOf(e, 0);

  assert balance_ == _balance;
}

rule zeroAddressRewardUnchanged(method f, env e, calldataarg args) filtered {
   f -> !f.isView
}{
  require e.msg.sender != 0;

  uint _balance = Reward.balanceOf(e, 0);
  f(e, args);
  uint balance_ = Reward.balanceOf(e, 0);

  assert balance_ == _balance;
}

rule cannotSetTransferStrategyToZero(method f, env e, calldataarg args) filtered {
   f -> !f.isView
}{
  address _transferStrategy = getTransferStrategy(Reward);
  f(e, args);
  address transferStrategy_ = getTransferStrategy(Reward);

  assert _transferStrategy != 0 => transferStrategy_ != 0 ;
}
