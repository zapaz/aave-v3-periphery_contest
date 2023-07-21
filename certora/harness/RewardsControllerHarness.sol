// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.10;

import {RewardsController} from '../../contracts/rewards/RewardsController.sol';

contract RewardsControllerHarness is RewardsController {

    constructor(address emissionManager) RewardsController(emissionManager) {}

    function getAssetsList() external view returns (address[] memory) {
        return _assetsList;
    }

    // returns an asset's reward index
    function getAssetRewardIndex(address asset, address reward) external view returns (uint256) {
        return _assets[asset].rewards[reward].index;
    }

    function getAvailableRewardsCount(address asset) external view returns (uint128) {
        return _assets[asset].availableRewardsCount;
    }
}